---
title: "Lab: Sensor Scavenger Hunt Challenge"
description: "Design and build a sensor-based device that reacts to its environment."
date: 2026-07-28
publishDate: 2026-07-28
session: "2F"
---

> **Session:** Session 2F â€” Sensor Scavenger Hunt Challenge
> **Audience:** All teams (student-facing)
> **Time Allotted:** 90 minutes
> **Team Size:** 3 students per station
> **Prerequisites:** Sessions 2B, 2C, 2D completed (LDR, potentiometer, hysteresis)
>
> Design and build a sensor-based device that reacts to its environment in a creative way. Use everything learned today: voltage dividers, analog readings, `map()`, thresholds, and hysteresis. This is an open-ended challenge â€” there is no single correct answer.

---

## SAFETY

> **SAFETY:** All components operate at 5V DC. Safe to touch. Never short 5V to GND. Ask an instructor before adding new components to your breadboard.

---

## Objective

Design and build a sensor-based device that reacts to its environment in a creative way. Your device must satisfy **at least two** of the following requirements:

- [ ] **Uses a sensor input** â€” LDR, potentiometer, or both
- [ ] **Makes a decision** â€” uses `if/else` with a threshold or hysteresis
- [ ] **Produces visible output** â€” LED brightness, color, or pattern changes
- [ ] **Produces audible output** â€” buzzer triggered by sensor condition
- [ ] **Maps sensor range** â€” uses `map()` to translate values
- [ ] **Combines two inputs** â€” responds to both light AND knob position

---

## Parts Available Per Station

| Part | Qty | Notes |
| :--- | :--- | :--- |
| 2004 I2C LCD display | 1 | Already connected at your station |
| LDR (light-dependent resistor) | 2 | Use one or both |
| 10kÎ© resistors | 3 | Voltage dividers |
| Potentiometer (10kÎ©) | 1 | Analog control |
| Red LED (5mm) | 2 | Output |
| Green LED (5mm) | 1 | Output |
| RGB LED (common cathode) | 1 | Color output |
| 220Î© resistors | 4 | Current-limiting |
| Buzzer (active, 5V) | 1 | Audio output |
| Jumper wires | 15 | Assorted |

> Teams may request additional components from roaming instructors.

---

## Procedure

### Step 1 â€” Brainstorm (10 min)

**Complete as a team.**

**Our device name:** _________________________________________________

**What it does (one sentence):** _______________________________________
_________________________________________________________________________

**Sensors used:**
- [ ] LDR (light)
- [ ] Potentiometer (knob)
- [ ] Both

**Outputs used:**
- [ ] LED(s)
- [ ] Buzzer
- [ ] Both

### Step 2 â€” Sketch the Behavior (10 min)

Describe what happens at different sensor values:

| Sensor Condition | What the Device Does |
| :---------------- | :--------------------- |
| Very low reading | ______________________ |
| Medium reading | ______________________ |
| Very high reading | ______________________ |
| Rapid change | ______________________ |

### Step 3 â€” Plan the Wiring (5 min)

| Component | Connected To |
| :--------- | :------------ |
| LDR | Pin _______ (analog) |
| Potentiometer wiper | Pin _______ (analog) |
| LED 1 | Pin _______ |
| LED 2 | Pin _______ |
| Buzzer | Pin _______ |

---

### Step 4 â€” Build Your Circuit (15 min)

**Hardware Tech leads.**

Build your circuit based on the wiring plan above. Test each sensor individually before combining them.

> **TIP:** Get one sensor reading working on the LCD display BEFORE writing the decision logic. Verify inputs before combining with outputs. The LCD is your primary debugging tool â€” use lines 2â€“4 to display sensor values and state variables.

---

### Step 5 â€” Write the Code (25 min)

**Coder types. Observer reads and checks off steps.**

Start with this skeleton structure, then fill in the logic:

```cpp
/*
 * Day 2 Scavenger Hunt: [Device Name]
 * Team ___ â€” Creation Station #___
 * Team members: ________, ________, ________
 * Purpose: [One-sentence description]
 * Expected result: [What happens when sensors are stimulated]
 */

// Pin definitions
const int LDR_PIN = A0;
const int POT_PIN = A1;
// Add output pins here

// Thresholds (adjust based on testing)
const int THRESHOLD_HIGH = 550;
const int THRESHOLD_LOW = 450;

// State tracking
bool currentState = false;

void setup() {
  // LCD initialized (LiquidCrystal_I2C or LCDHelper library)
  // Set output pin modes here
}

void loop() {
  // 1. Read sensors
  int ldrValue = analogRead(LDR_PIN);
  int potValue = analogRead(POT_PIN);

  // 2. Make decisions (thresholds, hysteresis, map())
  // Your logic here

  // 3. Drive outputs
  // Your output code here

  // 4. Debug output on LCD
  // lcd.setCursor(0, 0);
  // lcd.print("LDR:");
  // lcd.print(ldrValue);
  // lcd.setCursor(0, 1);
  // lcd.print("POT:");
  // lcd.print(potValue);

  delay(100);
}
```

---

### Step 6 â€” Test and Refine (15 min)

1. Test each sensor at extreme values (minimum and maximum)
2. Adjust thresholds based on actual readings
3. Try edge cases: what happens at the boundary of your hysteresis band?
4. Polish: make the behavior smooth and intentional

---

### Step 7 â€” Demo (15 min)

Each team demonstrates their device to a roaming instructor. Be prepared to explain:

1. **What your device does** (1 sentence)
2. **What sensors and thresholds you used**
3. **One thing that didn't work the way you expected and how you fixed it**

---

## Verification Checklist

Complete before demo:

- [ ] Brainstorming sheet filled out (device name, behavior table, wiring plan)
- [ ] Circuit wired and tested
- [ ] Code compiles and uploads without errors
- [ ] Device satisfies at least 2 challenge requirements (check boxes above)
- [ ] All team members can explain how the device works
- [ ] Sketch saved as `Station__Scavenger_Hunt` with team names in header comment

---

## Inspiration Ideas (If You're Stuck)

| Idea | Sensors | Output | Concept |
| :---- | :------- | :------ | :------- |
| Mood lamp | LDR + potentiometer | RGB LED | Ambient light sets brightness, knob sets color |
| Panic button | Potentiometer (turn fast = panic) | Buzzer + LED | Rapid knob movement triggers alarm |
| Light chase | LDR | Multiple LEDs | LEDs "run away" from light |
| Volume knob simulator | Potentiometer | Buzzer pitch + LED | Knob controls tone and brightness |
| Day/night cycle | LDR | RGB LED + buzzer | Bright = blue LED + no sound. Dark = red LED + soft beep |
| Reaction game | LDR | LED | Cover sensor, wait for signal, uncover as fast as possible |

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
| :------- | :------------ | :--- |
| Buzzer always on | Active buzzer connected to 5V without pin control | Connect buzzer + to digital pin, - to GND through resistor. Control with `digitalWrite()` |
| RGB LED only shows one color | Common cathode not grounded, or only one channel driven | Connect common cathode to GND. Drive R, G, B pins separately |
| Two sensors on same pin | LDR and potentiometer both on A0 | Use separate analog pins (A0 and A1) |
| Code works in parts but not combined | `delay()` blocking sensor reads | Reduce delay values. Read all sensors at top of `loop()` before any delays |
| Device behaves randomly | Unconnected analog pin floating | Always connect analog pin to a voltage divider. Unconnected pins read random values |

---

## Team Roles for This Session

During the scavenger hunt, rotate roles so all 3 team members participate:

| Role | Responsibilities |
| :---- | :---------------- |
| **Coder** | Types code, manages onboard editor, uploads sketches |
| **Hardware Tech** | Wires breadboard, manages components, checks connections |
| **Observer/Documenter** | Fills out brainstorming sheet, records threshold values, tracks what works |

> **Rotate roles at least once during the building phase.**

---

## Next Up

â† [Session 2D: Hysteresis](/lab-manuals/day-02/hysteresis/) | [Day 3: 3D Design and Actuation](/lab-manuals/day-03/) â†’