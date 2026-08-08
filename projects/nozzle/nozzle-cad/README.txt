Adult External-Sealing Enema Nozzle - prototype files
Generated 24 July 2026. Geometry per specification v0.3.

WHAT IS HERE
  nozzle_P1.step / .stl   flange 50 mm, nose 3.00 mm   baseline
  nozzle_P2.step / .stl   flange 55 mm, nose 3.00 mm   enhanced external seal
  nozzle_P3.step / .stl   flange 50 mm, nose 0.00 mm   flush, fully non-inserting
  nozzle_P4.step / .stl   flange 50 mm, nose 5.00 mm   maximum allowable projection

  nozzle_review.pdf       design and materials review
  nozzle.py               parametric source that generates all of the above

WHICH FILE TO SEND WHOM
  STEP  - for a silicone moulder or anyone working in CAD. This is the master
          format: an exact solid model, editable in their software.
  STL   - for a 3D printing bureau. This is what printers consume directly.
  Both describe the same geometry.

BEFORE FINAL PARTS ARE MADE
  The rear socket bore is currently a PLACEHOLDER (12 mm). It must be set from a
  measurement of the actual steel handpiece spout before any silicone part is
  moulded. The files are ready for quoting and for printing rigid masters now;
  the socket dimension is the one outstanding input.

  The central outlet is 6 mm (equal to the lumen) rather than the 4 mm in v0.3,
  to avoid accelerating the stream into a jet. See section 3 of the review.

NOTE FOR THE MANUFACTURER
  These are design-intent models. A production mould additionally needs draft
  angles, parting-line placement and shrinkage compensation, to be added in the
  manufacturer's own CAD.

TO CHANGE A DIMENSION
  Edit the values at the top of nozzle.py and re-run it:
      pip3 install cadquery
      python3 nozzle.py
  It regenerates every STEP and STL file and verifies the result.
