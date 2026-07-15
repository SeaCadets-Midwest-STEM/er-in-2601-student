---
title: "Day 3 - Shaping the Physical World"
date: 2026-07-29
weight: 3
---

## Theme: Parametric 3D Modeling, Slicing, and Additive Manufacturing

On Day 3, your team moves from circuits to physical design. Using FreeCAD on the Arduino Uno Q, you'll create parametric 3D models, slice them for printing, and produce real parts on SOVOL SV06 ACE 3D printers.

### Sessions

- **"The Broken Bracket"** - Hook Demo: A part fails and must be replaced
- **FreeCAD Introduction** - Parametric modeling, Sketcher constraints, and the Part Design workbench
- **Design Sprint** - Create a functional part from scratch: bracket, mount, or enclosure
- **Slicing** - Convert your STL to G-code with Orca Slicer: infill, supports, and print time
- **Print and Inspect** - Start your prints and learn to verify dimensions with calipers
- **Ultrasonic Ruler** - Wire an HC-SR04 ultrasonic sensor and display distance readings on your I2C LCD

### Key Concepts

| Term | Definition |
|------|-----------|
| Parametric Modeling | Design driven by dimensions and constraints that can be edited after the model is built |
| Sketcher | FreeCAD workbench for creating 2D sketches with geometric and dimensional constraints |
| STL | Stereolithography file format - the standard exchange format between CAD and slicers |
| G-code | The instruction language that tells a 3D printer exactly where to move and when to extrude |
| Infill | Internal lattice structure that gives printed parts strength without using solid material |
| Slicer | Software that converts 3D models into G-code the printer can execute |

### What to Bring

- Your team - FreeCAD runs on your station's Arduino Uno Q, calipers are shared at stations
- Your sensor circuits from Day 2 are still wired at your Creation Station

### Lab Manuals

Today's lab manuals are available below. Follow along with the detailed instructions as you work through each session.

- [Ultrasonic Ruler](/lab-manuals/day-03/ultrasonic-ruler/) - Wire an HC-SR04 sensor and display distance on an I2C LCD
- [Design Sprint](/lab-manuals/day-03/design-sprint/) - Create a functional 3D printed part using FreeCAD
