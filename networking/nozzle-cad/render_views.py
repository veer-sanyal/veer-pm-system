"""
Offscreen renders of the nozzle variants: a 2x2 comparison grid and a cut-away
section of P1 showing the internal flow path. Outputs views_grid.png, section.png.

ponytail: vtk + PIL are already installed (cadquery deps). No new tooling.
"""

import vtk
from PIL import Image, ImageDraw

W, H = 620, 520
SIL = (0.91, 0.66, 0.68)          # silicone pink
CUT = (0.78, 0.44, 0.47)          # darker face on the section cut


def render(stl, out, clipped=False, elev=(150, -140, -70), zoom=1.45):
    r = vtk.vtkSTLReader(); r.SetFileName(stl); r.Update()
    src = r

    if clipped:
        plane = vtk.vtkPlane(); plane.SetOrigin(0, 0, 0); plane.SetNormal(0, 1, 0)
        clip = vtk.vtkClipClosedSurface()     # caps the cut so it reads as solid
        clip.SetInputConnection(r.GetOutputPort())
        planes = vtk.vtkPlaneCollection(); planes.AddItem(plane)
        clip.SetClippingPlanes(planes)
        clip.SetScalarModeToColors()
        # BaseColor must be set too: scalar colouring overrides the actor colour,
        # so without it the whole body renders in the default (red) scalar.
        clip.SetBaseColor(*SIL)
        clip.SetClipColor(*CUT)
        clip.GenerateFacesOn()
        clip.Update()
        src = clip

    n = vtk.vtkPolyDataNormals()
    n.SetInputConnection(src.GetOutputPort())
    n.SetFeatureAngle(45); n.Update()

    m = vtk.vtkPolyDataMapper(); m.SetInputConnection(n.GetOutputPort())
    a = vtk.vtkActor(); a.SetMapper(m)
    p = a.GetProperty()
    p.SetColor(*SIL); p.SetInterpolationToPhong()
    p.SetSpecular(0.32); p.SetSpecularPower(28); p.SetDiffuse(0.85); p.SetAmbient(0.18)

    ren = vtk.vtkRenderer(); ren.AddActor(a); ren.SetBackground(1, 1, 1)
    win = vtk.vtkRenderWindow(); win.SetOffScreenRendering(1)
    win.AddRenderer(ren); win.SetSize(W, H)

    cam = ren.GetActiveCamera()
    cam.SetPosition(*elev); cam.SetFocalPoint(0, 0, 22); cam.SetViewUp(0, 0, -1)
    ren.ResetCamera(); cam.Zoom(zoom)

    for pos, inten in (((160, -160, -160), 0.95), ((-140, 90, -60), 0.45),
                       ((0, 40, 160), 0.3)):
        l = vtk.vtkLight(); l.SetPosition(*pos); l.SetIntensity(inten)
        l.SetLightTypeToSceneLight(); ren.AddLight(l)

    win.Render()
    wif = vtk.vtkWindowToImageFilter(); wif.SetInput(win); wif.Update()
    w = vtk.vtkPNGWriter(); w.SetFileName(out)
    w.SetInputConnection(wif.GetOutputPort()); w.Write()
    return out


LABELS = {
    "P1": "P1  flange 50 mm  ·  nose 3.0 mm  (baseline)",
    "P2": "P2  flange 55 mm  ·  nose 3.0 mm  (enhanced seal)",
    "P3": "P3  flange 50 mm  ·  nose 0 mm  (flush)",
    "P4": "P4  flange 50 mm  ·  nose 5.0 mm  (max projection)",
}

if __name__ == "__main__":
    tiles = []
    for v in ("P1", "P2", "P3", "P4"):
        tiles.append((v, render(f"nozzle_{v}.stl", f"_v_{v}.png")))

    grid = Image.new("RGB", (W * 2, H * 2), "white")
    d = ImageDraw.Draw(grid)
    for i, (v, f) in enumerate(tiles):
        x, y = (i % 2) * W, (i // 2) * H
        grid.paste(Image.open(f), (x, y))
        d.text((x + 22, y + 18), LABELS[v], fill=(60, 60, 70))
        d.rectangle([x, y, x + W - 1, y + H - 1], outline=(224, 224, 230))
    grid.save("views_grid.png")
    print("wrote views_grid.png", grid.size)

    render("nozzle_P1.stl", "section.png", clipped=True,
           elev=(120, -150, -95), zoom=1.15)
    print("wrote section.png")
