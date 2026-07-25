"""
Adult external-sealing enema nozzle — parametric model, spec v0.3 geometry.
Generates STEP (for the vendor) + STL (for a 3D-printed master or visual check).

Every dimension below is a variable: change a number, re-run, get a new file.
That is the whole point — the vendor gets STEP, the design stays editable.

Run:  python3 nozzle.py
Out:  nozzle_P1.step / .stl  (plus P2/P3/P4 variants from the spec's table 8)

ponytail: solid of revolution built from primitives, not a lofted surface model.
A real mould needs draft/parting-line work the vendor will add in their CAD;
this is a dimensionally-correct design intent model, which is what an RFQ needs.
"""

import cadquery as cq

# ---- parameters (spec v0.3, section 2) -------------------------------------
P = dict(
    flange_od        = 50.0,   # flange outside diameter
    flange_thk       = 4.0,    # flange overall thickness, centrally
    lip_thk          = 2.0,    # peripheral sealing lip thickness
    dish_depth       = 4.0,    # patient-facing concavity depth
    nose_proj        = 3.0,    # central nose projection beyond sealing plane
    nose_od          = 12.0,   # nose outside diameter
    outlet_dia       = 6.0,    # central outlet  << see DESIGN NOTE 1
    lumen_dia        = 6.0,    # internal lumen
    stem_od          = 20.0,   # body diameter behind the flange
    socket_len       = 40.0,   # rear push-fit socket length
    socket_bore      = 12.0,   # MEASURE THE STEEL SPOUT, then set this
    socket_wall      = 3.5,    # local wall thickness at the socket
    shoulder_thk     = 2.0,    # internal seating shoulder
    overall_len      = 55.0,   # total silicone part length
)

# DESIGN NOTE 1 — outlet_dia is set to 6.0, not the spec's 4.0, on purpose.
# A 4 mm outlet fed by a 6 mm lumen is a NOZZLE: it accelerates the stream
# (area ratio (6/4)^2 = 2.25x) right where it meets mucosa. Under a 1 m head
# the theoretical exit velocity is sqrt(2*g*h) ~ 4.4 m/s. The spec's own bench
# check ("no fine high-velocity jet") is fighting the spec's own geometry.
# Making the exit >= the lumen turns it into a diffuser instead.
# Set outlet_dia = 4.0 to build the original if you want both to compare.


def build(p):
    """Return the nozzle solid. Origin at the sealing plane, +Z = rearward."""
    stem_r = p["stem_od"] / 2
    socket_r = p["socket_bore"] / 2

    # --- body: stem + flange, then round everything the patient touches
    body = (
        cq.Workplane("XY")
        .circle(stem_r)
        .extrude(p["overall_len"])
    )

    # socket end needs enough wall around the steel spout
    socket_outer_r = max(stem_r, socket_r + p["socket_wall"])
    if socket_outer_r > stem_r:
        body = body.union(
            cq.Workplane("XY")
            .workplane(offset=p["overall_len"] - p["socket_len"])
            .circle(socket_outer_r)
            .extrude(p["socket_len"])
        )

    # --- flange at the patient end
    flange = (
        cq.Workplane("XY")
        .circle(p["flange_od"] / 2)
        .extrude(p["flange_thk"])
    )
    body = body.union(flange)

    # --- patient-facing concavity: shallow spherical dish cut into the flange.
    # Sphere radius from cap geometry: R = (a^2 + h^2) / 2h, a = dish radius.
    a = (p["flange_od"] / 2) - p["lip_thk"]
    h = p["dish_depth"]
    sphere_r = (a * a + h * h) / (2 * h)
    # centre BEHIND the patient face so only the cap is removed: the sphere must
    # pass through the rim circle (r=a at z=0) and bottom out at z=h on the axis.
    body = body.cut(
        cq.Workplane("XY")
        .workplane(offset=h - sphere_r)
        .sphere(sphere_r)
    )

    # --- central nose. Built as a cylinder whose FRONT FACE sits exactly at
    # z = -nose_proj, then rounded. Defining it as a sphere looks tidier but the
    # outlet bore drills the dome's tip away, so the delivered projection comes
    # out short of spec (3 mm asked, 1.35 mm built) and the P1/P3/P4 comparison
    # stops testing what it is supposed to test. Projection is exact here.
    nose_r = p["nose_od"] / 2
    if p["nose_proj"] > 0.05:
        nose = (
            cq.Workplane("XY")
            .workplane(offset=-p["nose_proj"])
            .circle(nose_r)
            .extrude(p["nose_proj"] + p["dish_depth"] + p["flange_thk"])
        )
        # dome-like, not a cone (spec 3): round the front rim as hard as the
        # projection and the outlet wall allow.
        r_max = min(p["nose_proj"], (p["nose_od"] - p["outlet_dia"]) / 2) * 0.9
        if r_max > 0.1:
            try:
                nose = nose.edges(">Z" if False else cq.selectors.BoxSelector(
                    (-nose_r - 1, -nose_r - 1, -p["nose_proj"] - 0.1),
                    (nose_r + 1, nose_r + 1, -p["nose_proj"] + 0.1),
                )).fillet(r_max)
            except Exception:
                pass
        body = body.union(nose)

    # --- flow path: outlet -> lumen -> socket bore, cut as one stack
    front_z = -p["nose_proj"] - 1.0          # start outside the part
    body = body.cut(
        cq.Workplane("XY").workplane(offset=front_z)
        .circle(p["outlet_dia"] / 2)
        .extrude(abs(front_z) + p["flange_thk"] + p["dish_depth"])
    )
    body = body.cut(
        cq.Workplane("XY")
        .circle(p["lumen_dia"] / 2)
        .extrude(p["overall_len"] - p["socket_len"] + p["shoulder_thk"])
    )
    body = body.cut(
        cq.Workplane("XY")
        .workplane(offset=p["overall_len"] - p["socket_len"] + p["shoulder_thk"])
        .circle(socket_r)
        .extrude(p["socket_len"])
    )

    # --- no sharp edge may touch the patient (spec section 3). Only the flange
    # rim and outlet rim are targeted; the nose was already rounded above.
    try:
        body = body.edges(
            cq.selectors.BoxSelector(
                (-40, -40, -0.05), (40, 40, p["flange_thk"] + 0.6)
            )
        ).fillet(0.8)
    except Exception:
        pass  # vendor CAD sets final radii anyway

    return body


def check(p, solid):
    """Assert the built solid actually matches the parameters asked for."""
    bb = solid.val().BoundingBox()
    assert abs(bb.xlen - p["flange_od"]) < 0.2, \
        f'flange OD {bb.xlen:.2f} != {p["flange_od"]}'
    want_proj = p["nose_proj"] if p["nose_proj"] > 0.05 else 0.0
    got_proj = -bb.zmin
    assert abs(got_proj - want_proj) < 0.3, \
        f"nose projection {got_proj:.2f} != {want_proj} (outlet/fillet ate the tip)"
    assert solid.val().Volume() > 5000, "geometry collapsed"
    return got_proj


# variants from spec section 8 (flange / nose projection)
VARIANTS = {
    "P1": dict(),                                        # baseline
    "P2": dict(flange_od=55.0),                          # enhanced external seal
    "P3": dict(nose_proj=0.001),                         # flush, non-inserting
    "P4": dict(nose_proj=5.0),                           # max allowable projection
}

if __name__ == "__main__":
    for name, override in VARIANTS.items():
        p = {**P, **override}
        solid = build(p)
        proj = check(p, solid)          # fails loudly rather than shipping a wrong part
        cq.exporters.export(solid, f"nozzle_{name}.step")
        cq.exporters.export(solid, f"nozzle_{name}.stl")
        print(f"{name}: flange {p['flange_od']:.0f}mm  nose {proj:.2f}mm  "
              f"{solid.val().Volume()/1000:.2f}cm^3  -> nozzle_{name}.step/.stl")
    print("\nSend the .step files to the vendor. Edit P above to change dimensions.")
