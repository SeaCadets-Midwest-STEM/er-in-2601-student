---
title: "Lab: Sensor Thresholds and Hysteresis"
description: "Discover why sensor readings near a threshold cause flickering and learn hysteresis to fix it."
date: 2025-01-01
publish_date: "2026-07-27"
session: "2D"
---

> **Session:** 2D â€” Lab: Sensor Thresholds and Hysteresis
> **Duration:** 45 minutes
> **Prerequisites:** Sessions 2B and 2C completed

---

## Safety

> **SAFETY:** All components operate at 5V DC. Safe to touch. Never short 5V directly to GND.

---

## Objective

Discover why sensor readings near a threshold cause flickering and learn the technique called **hysteresis** that fixes it. Implement hysteresis using a light sensor and observe the difference.

---

## Parts List

| Part | Qty | Notes |
| :--- | :--- | :--- |
| 2004 I2C LCD display | 1 | Already connected |
| LDR + 10kÎ© resistor | 1 | Voltage divider on Pin A0 |
| Red LED + 220Î© resistor | 1 | Output indicator on Pin 9 |
| Jumper wires | 5 | As needed |

---

## Procedure

### Part 1: The Problem â€” Flickering at the Threshold

Wire the LDR voltage divider (5V â†’ LDR â†’ A0 â†’ 10kÎ© â†’ GND) and an LED on Pin 9. Type this sketch into your editor:

```cpp
/*
 * Day 2 Lab: Hysteresis - The Flickering Problem
 * Team ___ â€” Creation Station #___
 * Purpose: Demonstrate threshold flickering problem
 * Expected result: LED flickers when light level hovers near threshold
 */

#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);

const int SENSOR_PIN = A0;
const int LED_PIN = 9;
const int THRESHOLD = 500;

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Threshold Problem  ");
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int reading = analogRead(SENSOR_PIN);

  lcd.setCursor(0, 1);
  lcd.print("Sensor: " + String(reading) + "         ");

  lcd.setCursor(0, 2);
  lcd.print("Threshold: " + String(THRESHOLD) + "     ");

  // Single threshold - PROBLEMATIC!
  if (reading > THRESHOLD) {
    digitalWrite(LED_PIN, HIGH);
    lcd.setCursor(0, 3);
    lcd.print("LED: ON (BRIGHT)          ");
  } else {
    digitalWrite(LED_PIN, LOW);
    lcd.setCursor(0, 3);
    lcd.print("LED: OFF (DARK)           ");
  }

  delay(100);
}
```

#### Observe the problem

1. Partially cover the LDR with your finger so the reading hovers near 500
2. Watch what happens to the LED
3. Watch the LCD line 4 â€” it rapidly switches between ON and OFF

> **EXPECTED RESULT:** When the sensor reading hovers near the threshold value (500), the LED flickers rapidly, switching between ON and OFF. The LCD shows the state changing back and forth. This is the **threshold flickering problem**.

**Why this happens:** Real-world sensor readings are never perfectly stable. Even when light levels seem constant, small variations cause the reading to jitter above and below the threshold. With a single threshold, the decision flips every time the reading crosses the line.

---

### Part 2: The Solution â€” Hysteresis

Now type the hysteresis version:

```cpp
/*
 * Day 2 Lab: Hysteresis - The Solution
 * Team ___ â€” Creation Station #___
 * Purpose: Use hysteresis to eliminate threshold flickering
 * Expected result: LED switches cleanly, no flickering near threshold
 */

#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);

const int SENSOR_PIN = A0;
const int LED_PIN = 9;
const int THRESHOLD_HIGH = 550;  // Turn ON above this
const int THRESHOLD_LOW = 450;   // Turn OFF below this

bool ledState = false;  // Track current state

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Hysteresis Fix!   ");
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int reading = analogRead(SENSOR_PIN);

  lcd.setCursor(0, 1);
  lcd.print("Sensor: " + String(reading) + "         ");

  lcd.setCursor(0, 2);
  lcd.print("ON@550  OFF@450       ");

  // Hysteresis - TWO thresholds
  if (reading > THRESHOLD_HIGH && ledState == false) {
    digitalWrite(LED_PIN, HIGH);
    ledState = true;
  } else if (reading < THRESHOLD_LOW && ledState == true) {
    digitalWrite(LED_PIN, LOW);
    ledState = false;
  }

  lcd.setCursor(0, 3);
  if (ledState) {
    lcd.print("LED: ON               ");
  } else {
    lcd.print("LED: OFF              ");
  }

  delay(100);
}
```

#### Key concept: How hysteresis works

Hysteresis uses **two thresholds** instead of one:

| Light Level | Single Threshold (500) | Hysteresis (450/550) |
| :---------- | :--------------------- | :-------------------- |
| Reading > 550 | ON | ON |
| Reading 500â€“550 | **Flickering!** | **Stays ON** (won't turn off until < 450) |
| Reading 450â€“500 | **Flickering!** | **Stays OFF** (won't turn on until > 550) |
| Reading < 450 | OFF | OFF |

The "dead zone" between 450 and 550 is where hysteresis prevents flickering. Once the LED turns ON (reading > 550), it won't turn OFF until the reading drops below 450. Once OFF (reading < 450), it won't turn ON until the reading rises above 550.

#### Verify

| Action | Single Threshold | Hysteresis |
| :------ | :--------------- | :---------- |
| Light hovers near threshold | LED flickers rapidly | LED stays stable |
| Gradually cover LDR | Clean transition (but flickers at threshold) | Clean transition (no flicker) |
| Gradually uncover LDR | Clean transition (but flickers at threshold) | Clean transition (no flicker) |

> **EXPECTED RESULT:** With hysteresis, the LED switches cleanly between ON and OFF with no flickering. Line 3 of the LCD always shows "ON@550 OFF@450" as a reminder of the two thresholds. Line 4 shows the stable LED state.

---

## Verification Checklist

- [ ] Observed flickering problem with single threshold
- [ ] Hysteresis version eliminates flickering
- [ ] LED switches cleanly between ON and OFF
- [ ] Sketch saved as `Station__Hysteresis` with station number

---

## Challenge Extensions

### Challenge 1: Adjustable Hysteresis Band (10 min)

Add a potentiometer on Pin A1. Use the potentiometer value to control the size of the hysteresis "dead zone." Knob CCW = narrow band (495/505), knob CW = wide band (300/700).

### Challenge 2: Three-State Indicator (10 min)

Use three LEDs (green, yellow, red) with hysteresis:
- Green: reading > 700 (bright)
- Yellow: reading 300â€“700 (normal, with hysteresis at both boundaries)
- Red: reading < 300 (dark)

This requires **four** thresholds (two for each boundary).

---

## Real-World Examples of Hysteresis

| System | What it prevents | Thresholds |
| :------ | :--------------- | :---------- |
| Thermostat | AC compressor cycling on/off rapidly | Heat at 68Â°F, Cool at 72Â°F |
| Elevator doors | Door open/close flickering when someone stands at the threshold | Close when hall sensor clear for 5s, Open when sensor triggered |
| CPU fan speed | Fan ramping up/down rapidly at idle | Spin up at 75Â°C, Spin down at 60Â°C |
| Smartphone screen | Screen turning on/off when tucked in pocket | Wake at full cover removal, Sleep at full cover |

---

## Previous / Next

â† [Session 2C: Potentiometer](/lab-manuals/day-02/potentiometer-analog/) | [Session 2F: Sensor Scavenger Hunt](/lab-manuals/day-02/sensor-scavenger-hunt/) â†’