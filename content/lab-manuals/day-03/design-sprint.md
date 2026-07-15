---
title: "Lab: 3D Design Sprint Challenge"
description: "Design, model, and prepare a functional enclosure for your Arduino project using FreeCAD and OrcaSlicer."
date: 2025-01-01
publish_date: "2026-07-28"
session: "3F"
---

> **Session:** 3F â€” Design Sprint Challenge
> **Duration:** 45 minutes
> **Team:** Record your team name and Creation Station number in your notebook
> **Prerequisites:** Session 3B (First Part in FreeCAD), Session 3C (Design for Your Device) completed

---

## Safety

> **SAFETY:** This lab uses only computers and 3D printers. Follow standard 3D printer safety: do not touch the print head or heated bed while printing. Do not pull filament during a print. Report any burning smell or unusual noises to the instructor immediately.

---

## Objective

Design, model, and prepare for printing a functional enclosure or sensor mount for your team's device. You will create a parametric model in FreeCAD that fits your Arduino Uno Q and breadboard, then export it as an STL file ready for slicing and printing.

> **EXPECTED RESULT:** By the end of this lab, your team will have an STL file queued in OrcaSlicer for printing. The design must fit within the SOVOL SV06 ACE build volume (220 Ã— 220 Ã— 250 mm).

---

## Parts List

| Part | Qty | How to Identify |
| :--- | :--- | :--- |
| Computer with FreeCAD installed | 1 | Per team, pre-installed |
| OrcaSlicer installed | 1 | Per team, pre-installed |
| Arduino Uno Q board | 1 | Your team's board (for measurement) |
| Breadboard (830-point) | 1 | Your team's breadboard (for measurement) |
| Digital calipers | 1 | Shared resource (request from instructor) |
| Ruler (metric) | 1 | Backup if calipers unavailable |
| Team notepad + pen | 1 | For recording measurements |

---

## Procedure

### Part 1: Measure Your Hardware (10 min)

Before designing, you need accurate measurements. Use calipers (or a ruler) to measure:

| Component | Dimension | Record in your notebook |
| :--------- | :--------- | :-------------- |
| **Arduino Uno Q** | Length (long edge) | Measure and record |
| | Width (short edge) | Measure and record |
| | Height (including headers) | Measure and record |
| | USB port protrusion (back edge) | Measure and record |
| | Mounting hole spacing (horizontal) | Measure and record |
| | Mounting hole spacing (vertical) | Measure and record |
| **Breadboard (830-point)** | Length | Measure and record |
| | Width | Measure and record |
| | Height (including rails) | Measure and record |
| **LDR sensor** | Diameter | Measure and record |
| **MAX7219 matrix** | Width | Measure and record |
| | Height | Measure and record |

> **TIP:** Add 2-3 mm clearance to each dimension for easy insertion/removal. For example, if the Arduino is 70 mm wide, design the compartment as 72-73 mm wide.

---

### Part 2: Design Your Enclosure in FreeCAD (25 min)

#### Step 1: Create a new document

1. Open FreeCAD
2. File â†’ New Document
3. Save immediately: File â†’ Save As â†’ `Station__[TeamName]_Enclosure.FCStd`

#### Step 2: Create the base plate

1. Switch to **Part Design** workbench
2. In the tree view, right-click the body â†’ New Pad
3. Sketch on XY plane: draw a rectangle for the base plate
   - Suggested size: 200 Ã— 90 mm (fits Arduino + breadboard side by side)
4. Set pad thickness: **3 mm**

#### Step 3: Add walls

1. Create a new pad on top of the base plate
2. Sketch the wall outline (rectangle with slightly smaller inner dimensions)
3. Set wall height: **40-60 mm** (adjust based on your component heights)
4. Wall thickness: **1.2 mm** (standard wall for FFF printing)

#### Step 4: Add cutouts for components

Use **Pocket** or **Cut** operations to create openings:

| Cutout | Purpose | Suggested Size |
| :------ | :------- | :-------------- |
| USB port | Program and power | 12 Ã— 8 mm at back edge |
| Serial port | Debugging | 6 Ã— 4 mm near USB |
| Matrix display | Visible output | Match your matrix measurements + 2 mm |
| LDR sensor | Light exposure | Match LDR diameter + 4 mm |
| Power LED | Status indicator | 4 Ã— 4 mm |

> **TIP:** Place cutouts BEFORE adding complex features. It's easier to cut a hole in a simple box than in a detailed enclosure.

#### Step 5: Add mounting features (optional but recommended)

- **Standoff holes:** 4.5 mm diameter holes at Arduino mounting hole positions
- **Breadboard clips:** Small tabs or channels to hold the breadboard in place
- **Snap-fit lid:** Design a separate lid piece that snaps or screws on

#### Step 6: Verify dimensions

Before exporting, check your design:

| Check | Status |
| :----- | :---- |
| Total width â‰¤ 220 mm (SOVOL SV06 ACE limit) | Verify |
| Total depth â‰¤ 220 mm | Verify |
| Total height â‰¤ 250 mm | Verify |
| Wall thickness â‰¥ 1.0 mm | Verify |
| Text (if any) depth â‰¥ 0.8 mm | Verify |
| All cutouts present and correctly sized | Verify |

---

### Part 3: Export and Prepare for Printing (10 min)

#### Export as STL

1. In FreeCAD, select your enclosure body in the tree view
2. File â†’ Export
3. Choose format: **STL Mesh (*.stl)**
4. Save as: `Station__[TeamName]_Enclosure.stl`

#### Import into OrcaSlicer

1. Open OrcaSlicer
2. Select printer profile: **SOVOL SV06 ACE**
3. Drag and drop your STL file into the build plate
4. Rotate and position the model on the build plate

#### Slicing settings (instructor-approved defaults)

| Setting | Value | Reason |
| :------- | :----- | :------ |
| Quality (layer height) | 0.2 mm | Standard quality |
| Walls (perimeters) | 2 | Strength |
| Top/Bottom shells | 3 | Solid surfaces |
| Infill density | 15% | Balance of strength and speed |
| Infill pattern | Grid | Simple, reliable |
| Supports | As needed | Only where overhangs > 45Â° |
| Print speed | 60 mm/s | Reliable default |
| Raft | No | Adhesion to bed is sufficient |
| Brim | Yes (optional) | Extra edge adhesion |

#### Estimate print time

1. Click **Slice** in OrcaSlicer
2. Note the estimated print time
3. Record below:

| Team | Record in your notebook | Status |
| :--- | :------------------- | :------ |
| Our team | Record hours and minutes | Is it under 4 hours? |

> **EXPECTED RESULT:** If print time exceeds 4 hours, simplify the design: reduce wall height, reduce infill to 10%, or remove decorative features. The goal is to have prints complete by end of Day 3 or early Day 4.

---

## Verification Checklist

- [ ] Hardware measurements recorded in table above
- [ ] FreeCAD model saved as `.FCStd` file (parametric source)
- [ ] STL file exported successfully
- [ ] Model imported into OrcaSlicer
- [ ] Design fits within SOVOL SV06 ACE build volume (220 Ã— 220 Ã— 250 mm)
- [ ] Print time â‰¤ 4 hours
- [ ] Instructor approved for printing
- [ ] File named correctly: `Station__[TeamName]_Enclosure.stl`

---

## Challenge Extensions

### Challenge 1: Team Name on Enclosure (10 min)

Add your team name or logo to the enclosure using raised text:

1. In FreeCAD, use the **Draft** workbench â†’ Text tool
2. Write your team name on the top surface
3. Use **Boolean Union** to merge text with the enclosure body
4. Minimum text height: 5 mm for readability

### Challenge 2: Cable Management Channel (10 min)

Add a channel or hole for the USB cable to exit cleanly:

1. Design a routed channel on the bottom or back edge
2. Width: 8 mm, Depth: 5 mm
3. This keeps the cable from pulling on the board connectors

### Challenge 3: Sensor Extension Port (10 min)

Design a port that allows you to run sensor wires out of the enclosure:

1. Create a 6 mm diameter hole on one wall
2. Add a grommet-style raised ring around the hole
3. This simulates real industrial sensor cable entries

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
| :------- | :------------ | :--- |
| FreeCAD crashes when adding cutout | Cutout is larger than the face, or wrong reference face | Make sure the sketch is on the correct face. Cutout must be smaller than the wall. |
| Export to STL fails | Model has invalid geometry | Use Part â†’ Validate Shape in FreeCAD. Fix errors before exporting. |
| OrcaSlicer says "model not on build plate" | Model is positioned outside the print area | Use the move tool to place the model on the green build plate area. |
| Print time > 4 hours | Design too complex or infill too high | Reduce infill to 10%. Reduce wall height. Remove unnecessary internal features. |
| Walls too thin (printer won't print) | Wall thickness < 0.8 mm | Increase wall thickness to at least 1.2 mm (2 perimeters at 0.6 mm each). |
| Cutout too small for component | Didn't add clearance | Add 2-3 mm clearance to all cutout dimensions. Re-slice. |
| Model exceeds build volume | Design too large | Scale down. Check SOVOL SV06 ACE limits: 220 Ã— 220 Ã— 250 mm. |

---

## Key Concept Summary

**This is the DESIGN â†’ PROTOTYPE â†’ TEST â†’ ITERATE cycle that real engineers use.** Your first design will rarely be perfect. The goal is to learn from the physical prototype and improve.

Your STL file will be queued for printing after instructor approval. Prints should start by end of Day 3 afternoon. In Session 3E (Day 3 Wrap-Up), you'll collect your printed parts and verify fit. If the fit is not right, you'll iterate on the design in Session 4H (Day 4 Morning: Print Queue Review + Fit Iteration).

---

## Next Up

Continue to [Day 4 Lab Manuals](/lab-manuals/day-04/) â†’