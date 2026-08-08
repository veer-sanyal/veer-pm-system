"""
Extract the true axisymmetric cross-section profile of each nozzle variant.

The part is a solid of revolution, so its whole surface is defined by one closed
2D loop in (radius, z). Cutting the mesh at y=0 and keeping the +x half gives
exactly that loop -- which a viewer can revolve back into an accurate 3D model
without shipping a mesh. Writes profiles.json.

ponytail: reuses the STLs nozzle.py already emits + vtk (already a cadquery dep).
No new deps, no mesh decimation, no hand-built exporter.
"""

import json
import vtk

VARIANTS = ["P1", "P2", "P3", "P4"]


def profile_of(stl_path):
    r = vtk.vtkSTLReader()
    r.SetFileName(stl_path)
    r.Update()

    plane = vtk.vtkPlane()
    plane.SetOrigin(0, 0, 0)
    plane.SetNormal(0, 1, 0)          # slice on y=0

    cut = vtk.vtkCutter()
    cut.SetCutFunction(plane)
    cut.SetInputConnection(r.GetOutputPort())
    cut.Update()

    strip = vtk.vtkStripper()          # join cut segments into polylines
    strip.SetInputConnection(cut.GetOutputPort())
    strip.JoinContiguousSegmentsOn()
    strip.Update()

    out = strip.GetOutput()
    pts, lines = out.GetPoints(), out.GetLines()

    loops = []
    lines.InitTraversal()
    ids = vtk.vtkIdList()
    while lines.GetNextCell(ids):
        loop = [pts.GetPoint(ids.GetId(i)) for i in range(ids.GetNumberOfIds())]
        loops.append(loop)

    # the solid is an annulus in section: two mirror loops. Keep the +x one.
    right = [L for L in loops if sum(p[0] for p in L) / len(L) > 0]
    right.sort(key=len, reverse=True)
    if not right:
        raise RuntimeError(f"no +x loop found in {stl_path}")

    # (radius, z), rounded -- 3 decimals is far finer than any mould tolerance
    return [[round(p[0], 3), round(p[2], 3)] for p in right[0]]


if __name__ == "__main__":
    data = {}
    for v in VARIANTS:
        prof = profile_of(f"nozzle_{v}.stl")
        rs = [p[0] for p in prof]
        zs = [p[1] for p in prof]
        # the loop must be closed for the revolve to produce a watertight surface
        closed = (abs(prof[0][0] - prof[-1][0]) < 0.01
                  and abs(prof[0][1] - prof[-1][1]) < 0.01)
        assert closed, f"{v}: profile loop is not closed"
        assert max(rs) > 20, f"{v}: max radius {max(rs)} looks wrong"
        data[v] = prof
        print(f"{v}: {len(prof):4d} pts  r {min(rs):.2f}..{max(rs):.2f}  "
              f"z {min(zs):.2f}..{max(zs):.2f}  closed={closed}")

    with open("profiles.json", "w") as f:
        json.dump(data, f, separators=(",", ":"))
    print("\nwrote profiles.json")
