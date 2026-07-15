---
title: "Lab: Potentiometer and Analog Reading"
description: "Explore potentiometers as variable resistors and practice using map() to translate sensor ranges."
date: 2026-07-27
publishDate: 2026-07-27
session: "2C"
---

> **Session:** 2C â€” Lab: Potentiometer and Analog Reading
> **Duration:** 45 minutes
> **Prerequisites:** Session 2B (Light Sensor Circuit) completed

---

## Safety

> **SAFETY:** All components operate at 5V DC. Safe to touch. Never short 5V directly to GND.

---

## Objective

Explore how a potentiometer works as a manually controlled variable resistor. Read analog values and practice using `map()` to translate sensor ranges to useful output ranges.

---

## Parts List

| Part | Qty | Notes |
| :--- | :--- | :--- |
| 2004 I2C LCD display | 1 | Already connected at station |
| Potentiometer (10kÎ©, 3-leg) | 1 | Round body, 3 pins, adjustment shaft |
| Red LED + 220Î© resistor | 1 | For PWM output |
| Jumper wires | 5 | Assorted colors |

---

## Procedure

### Part 1: Wire the Potentiometer

#### Wiring

| Pin | Connection | Note |
| :--- | :----------- | :----- |
| Left leg | 5V | Fixed power |
| Middle leg | Pin A0 | Signal output (wiper) |
| Right leg | GND | Fixed ground |

> **TIP:** The potentiometer's middle leg is the "wiper" â€” it slides between the two fixed legs as you turn the shaft. The wiper voltage is what changes.

#### Steps

1. Insert potentiometer on breadboard (3 legs span the center groove)
2. Jumper: left leg â†’ 5V
3. Jumper: middle leg â†’ Pin A0
4. Jumper: right leg â†’ GND

### Part 2: Read and Display Values

```cpp
/*
 * Day 2 Lab: Potentiometer Reading
 * Team ___ â€” Creation Station #___
 * Purpose: Read potentiometer and display on LCD
 * Expected result: LCD shows 0-1023, changes as knob is turned
 */

#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);

const int POT_PIN = A0;

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Potentiometer Lab  ");
}

void loop() {
  int potValue = analogRead(POT_PIN);

  lcd.setCursor(0, 1);
  lcd.print("Knob: " + String(potValue) + "         ");

  lcd.setCursor(0, 2);
  lcd.print("Range: " + String(potValue / 10) + "%         ");

  delay(100);
}
```

#### Verify

| Action | Expected LCD |
| :------ | :------------ |
| Turn knob fully counter-clockwise | Knob: 0â€“20, Range: 0% |
| Turn knob to middle | Knob: ~500, Range: ~50% |
| Turn knob fully clockwise | Knob: 1000â€“1023, Range: 100% |
| Turn knob slowly | Values change smoothly |

> **EXPECTED RESULT:** LCD shows values 0â€“1023 on line 2 and a percentage on line 3 that tracks knob position.

---

### Part 3: Control LED Brightness with the Knob

Wire an LED to Pin 9 (PWM-capable) through a 220Î© resistor. Update the sketch:

```cpp
/*
 * Day 2 Lab: Potentiometer Controls LED
 * Team ___ â€” Creation Station #___
 * Purpose: Knob controls LED brightness via PWM
 * Expected result: LED brightness follows knob position
 */

#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);

const int POT_PIN = A0;
const int LED_PIN = 9;

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Knob -> LED Bright ");
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int potValue = analogRead(POT_PIN);
  int brightness = map(potValue, 0, 1023, 0, 255);
  analogWrite(LED_PIN, brightness);

  lcd.setCursor(0, 1);
  lcd.print("Knob: " + String(potValue) + "         ");

  lcd.setCursor(0, 2);
  lcd.print("Bright: " + String(brightness) + "       ");

  delay(100);
}
```

#### Key concept: `map()` for PWM

The potentiometer reads 0â€“1023 (10-bit ADC). PWM brightness uses 0â€“255 (8-bit). `map()` converts between them:

```
map(potValue, 0, 1023, 0, 255)
```

| Pot Position | ADC Reading | Mapped Brightness | LED Appearance |
| :----------- | :---------- | :---------------- | :------------- |
| Fully CCW | 0 | 0 | OFF |
| 25% CW | ~256 | ~64 | Dim |
| 50% CW | ~512 | ~128 | Medium |
| 75% CW | ~768 | ~192 | Bright |
| Fully CW | 1023 | 255 | Maximum |

> **EXPECTED RESULT:** Turn the knob to smoothly control LED brightness from OFF to maximum. LCD shows both raw knob value (line 2) and brightness (line 3).

---

## Verification Checklist

- [ ] Potentiometer wired (5V â†’ left, A0 â†’ middle, GND â†’ right)
- [ ] Sketch sends to board without errors
- [ ] LCD shows knob values changing 0â€“1023 as turned
- [ ] LED brightness responds to knob position
- [ ] Sketch saved as `Station__Potentiometer` with station number

---

## Challenge Extensions

### Challenge 1: LED Speed Control (10 min)

Combine the chase pattern from Day 1 with the potentiometer: use the knob to control the speed of the chase. Knob CCW = slow, knob CW = fast.

**Hint:** Map the potentiometer to a delay value: `map(potValue, 0, 1023, 500, 10)`

### Challenge 2: Custom Range Mapping (10 min)

Map the potentiometer to a non-linear range. For example, make the bottom 50% of the knob control 0â€“10 brightness, and the top 50% control 10â€“255. This creates a "gentle fade then bright" effect.

### Challenge 3: Two-LED Mixer (10 min)

Add a second LED to Pin 10. Use one half of the knob range (0â€“512) for the first LED and the other half (512â€“1023) for the second LED. As you turn the knob, one LED fades out as the other fades in.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
| :------- | :------------ | :--- |
| Reading stuck at 0 | Middle leg not connected to A0 | Check jumper from wiper to Pin A0 |
| Reading stuck at 1023 | Middle leg connected to 5V instead of A0 | Verify: left=5V, middle=A0, right=GND |
| Values jump erratically | Loose connection | Reseat all jumper wires. Check potentiometer legs are in breadboard holes |
| Knob doesn't affect brightness at extremes | Potentiometer legs reversed (5V and GND swapped) | Works either way, but "full CCW = OFF" direction will be reversed |
| LED doesn't dim smoothly, only ON/OFF | Using `digitalWrite()` instead of `analogWrite()` | Change to `analogWrite(LED_PIN, brightness)` |
| LED flickers | Delay too short (< 50ms) | Increase `delay(100)` to `delay(200)` |

---

## Previous / Next

â† [Session 2B: Light Sensor](/lab-manuals/day-02/light-sensor-circuit/) | [Session 2D: Hysteresis](/lab-manuals/day-02/hysteresis/) â†’