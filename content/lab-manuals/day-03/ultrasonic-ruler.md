---
title: "Lab: Ultrasonic Ruler â€” Distance Detection"
description: "Wire an HC-SR04 ultrasonic sensor and build a proximity-warning system with LED and buzzer indicators."
date: 2026-07-28
publishDate: 2026-07-28
session: "3B"
---

> **Session:** 3B â€” Lab: Ultrasonic Ruler
> **Duration:** 60 minutes
> **Team:** Record your team name and Creation Station number in your notebook
> **Prerequisites:** Session 3A (Ultrasonic Distance Sensing) lecture completed

---

## Safety

> **SAFETY:** The HC-SR04 ultrasonic sensor operates at 5V DC from the Arduino Uno Q. These voltages are safe to touch. The 40 kHz ultrasonic sound is inaudible to humans but may be uncomfortable for pets. Never short 5V directly to GND.

---

## Objective

Wire an HC-SR04 ultrasonic sensor to your Arduino Uno Q and build an "Ultrasonic Ruler" that displays real-time distance measurements. Then add threshold-based actions: LED indicators and buzzer warnings that respond to proximity â€” just like a car parking sensor.

---

## Parts List

| Part | Qty | How to Identify |
| :--- | :--- | :--- |
| 2004 I2C LCD display | 1 | Already connected at your station |
| HC-SR04 ultrasonic sensor | 1 | Two "eyes" (transmitter and receiver) on blue PCB |
| Red LED (5mm) | 1 | Long leg = anode |
| 220Î© resistor | 1 | Red-red-brown-gold |
| Buzzer (active, 5V) | 1 | Round black component with + and - markings |
| Jumper wires (female-female) | 6 | Assorted colors |

---

## Procedure

### Part 1: Wire the HC-SR04

Connect the ultrasonic sensor to your breadboard and Arduino:

| HC-SR04 Pin | Arduino Connection | Wire Color (suggested) |
| :----------- | :----------------- | :---------------------- |
| VCC (Pin 1) | 5V | Red |
| TRIG (Pin 2) | Digital Pin 7 | Yellow |
| ECHO (Pin 3) | Digital Pin 8 | Green |
| GND (Pin 4) | GND | Black |

> **TIP:** The HC-SR04 pins are tight and may be hard to insert into the breadboard. Press firmly but don't force. If pins bend, straighten with pliers before retrying.

### Part 2: Type the Distance Reader Sketch

```cpp
/*
 * Day 3 Lab: Ultrasonic Ruler â€” Distance Reader
 * Team ___ â€” Creation Station #___
 * Purpose: Read distance from HC-SR04 and display on LCD
 * Expected result: LCD shows distance in cm that tracks hand movement
 */

#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

const int TRIG_PIN = 7;
const int ECHO_PIN = 8;

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Ultrasonic Ruler    ");
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  // Step 1: Send 10us trigger pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Step 2: Measure echo pulse duration
  long duration = pulseIn(ECHO_PIN, HIGH);

  // Step 3: Convert to distance (centimeters)
  float distance = duration * 0.034 / 2;

  // Step 4: Display result on LCD
  lcd.setCursor(0, 1);
  lcd.print("Distance:             ");

  if (duration == 0) {
    lcd.setCursor(0, 1);
    lcd.print("Out of range        ");
  } else {
    lcd.setCursor(0, 1);
    lcd.print("Distance: ");
    lcd.print(distance, 1);
    lcd.print(" cm         ");
  }

  delay(200);
}
```

#### Verify the distance reading

1. Send the sketch to the board
2. Hold a flat object (hand, book) in front of the sensor
3. Move closer and farther â€” watch the LCD values change

> **EXPECTED RESULT:** LCD shows distance in centimeters (2-400 cm range) on line 2. Values decrease as object approaches, increase as object retreats. Display says "Out of range" when nothing is within ~4 meters.

---

### Part 3: Add Proximity Indicators

Add an LED and buzzer that respond to distance thresholds:

| Component | Arduino Connection | Wire Color (suggested) |
| :--------- | :----------------- | :---------------------- |
| LED anode â†’ 220Î© â†’ Pin 9 | Digital Pin 9 | Orange |
| Buzzer + â†’ Pin 10 | Digital Pin 10 | Blue |
| LED cathode | GND | Black |
| Buzzer - | GND | Black |

Type this sketch into your editor:

```cpp
/*
 * Day 3 Lab: Ultrasonic Ruler â€” Proximity Warning
 * Team ___ â€” Creation Station #___
 * Purpose: LED and buzzer respond to distance thresholds like a parking sensor
 * Expected result: LED warns at < 30cm, buzzer activates at < 15cm
 */

#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

const int TRIG_PIN = 7;
const int ECHO_PIN = 8;
const int LED_PIN = 9;
const int BUZZER_PIN = 10;

// Thresholds
const int WARNING_DISTANCE = 30;   // cm â€” LED turns on
const int DANGER_DISTANCE = 15;    // cm â€” buzzer activates

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Proximity Warning   ");
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  // Read distance
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  float distance = duration * 0.034 / 2;

  // Display distance on LCD line 2
  lcd.setCursor(0, 1);
  if (duration == 0) {
    lcd.print("Out of range        ");
  } else {
    lcd.print("Dist: ");
    lcd.print(distance, 1);
    lcd.print(" cm           ");
  }

  // Proximity responses
  if (distance < DANGER_DISTANCE && distance > 0) {
    // Danger zone: LED on + buzzer
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
    lcd.setCursor(0, 2);
    lcd.print(">>> DANGER - STOP!  ");
  } else if (distance < WARNING_DISTANCE && distance > 0) {
    // Warning zone: LED only
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, LOW);
    lcd.setCursor(0, 2);
    lcd.print(">> WARNING - Close  ");
  } else {
    // Safe: nothing active
    digitalWrite(LED_PIN, LOW);
    digitalWrite(BUZZER_PIN, LOW);
    lcd.setCursor(0, 2);
    lcd.print("  SAFE              ");
  }

  delay(200);
}
```

#### Test the proximity system

1. Move object from far to near slowly
2. Observe LED turns on at ~30 cm and LCD shows "WARNING"
3. Observe buzzer activates at ~15 cm and LCD shows "DANGER"
4. Move away â€” both turn off and LCD shows "SAFE"

> **EXPECTED RESULT:** As object approaches: LED illuminates first (warning at 30 cm) with LCD showing "WARNING", then buzzer joins (danger at 15 cm) with LCD showing "DANGER - STOP!". Moving away reverses the behavior and LCD returns to "SAFE".

---

### Part 4: Tune Your Team's Thresholds

Experiment with different threshold values. Record observations:

| Warning Distance | Danger Distance | Record in your notebook |
| :---------------- | :--------------- | :--------------------- |
| 30 cm | 15 cm | Describe the behavior you observe |
| 50 cm | 40 cm | Describe the behavior you observe |
| 20 cm | 5 cm | Describe the behavior you observe |

**Questions to discuss:**
- What thresholds make a good parking sensor?
- What thresholds make a good automatic door trigger?
- How would you adjust thresholds for a baby monitor (cry when baby gets close to crib edge)?

---

## Verification Checklist

- [ ] HC-SR04 wired and distance readings displayed on LCD
- [ ] Distance values correlate to physical hand movement (verified with ruler)
- [ ] Proximity system: LED warns, buzzer activates at set thresholds
- [ ] Team tested at least 3 different threshold combinations
- [ ] Sketches saved with station number in filename

---

## Challenge Extensions

### Challenge 1: Approach Direction Detection (15 min)

Detect whether the object is moving CLOSER or FARTHER by comparing the current reading to the previous reading. Display the direction on the LCD:

```cpp
float previousDistance = 999;  // Start with "far away"

// In loop(), after reading distance:
if (distance < previousDistance && distance > 0) {
  lcd.setCursor(0, 3);
  lcd.print("-> APPROACHING      ");
} else if (distance > previousDistance) {
  lcd.setCursor(0, 3);
  lcd.print("-> MOVING AWAY      ");
}
previousDistance = distance;
```

### Challenge 2: Distance-Based LED Brightness (10 min)

Use `map()` and `analogWrite()` to make LED brightness proportional to distance. Close = bright. Far = dim.

```cpp
int brightness = map(distance, 0, 100, 255, 0);  // 0-100cm â†’ 255-0 brightness
brightness = constrain(brightness, 0, 255);       // Clamp to valid PWM range
analogWrite(LED_PIN, brightness);
```

### Challenge 3: Non-Contact Stopwatch (15 min)

Wave hand past the sensor to start/stop a timer. First pass = start. Second pass = stop. Display elapsed time on the LCD.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
| :------- | :------------ | :--- |
| LCD shows "Out of range" always | TRIG/ECHO pins swapped | Check: Pin 2 -> TRIG (Pin 7), Pin 3 -> ECHO (Pin 8) |
| Distance reads ~0 cm always | Object too close (< 2 cm minimum) | Move object 5+ cm from sensor |
| Distance values jump wildly | Soft/angled reflecting surface | Use flat, hard surface (book, phone, hand) |
| Buzzer always on even with no object nearby | Buzzer + and - reversed, or always HIGH in code | Check buzzer polarity. Verify `digitalWrite(BUZZER_PIN, LOW)` in safe zone |
| `pulseIn()` causes long pauses | Default timeout is 1 second | Add timeout parameter: `pulseIn(ECHO_PIN, HIGH, 30000)` (30ms timeout â‰ˆ 5m range) |
| HC-SR04 pins won't fit in breadboard | Pins too wide for standard spacing | Use female-female jumper wires as adapters |
| LCD shows only blank screen | LCD I2C address wrong or wires disconnected | Check 4 wire connections. Try address 0x3F in code |
| Compilation error: "LiquidCrystal_I2C not found" | Library not pre-installed | Notify instructor â€” library should be pre-installed |

---

## Key Concept Summary

**Ultrasonic sensors measure distance by timing sound echoes.** The Arduino sends a trigger pulse, the sensor emits ultrasonic sound (inaudible to humans), and measures how long the echo takes to return. Distance = (time Ã— speed of sound) / 2.

**Where you'll see this in the real world:**
- Car parking sensors
- Bat and dolphin echolocation
- Industrial level sensors (tank fill measurement)
- Robotic obstacle avoidance
- Automatic door openers

---

## Next Up

Continue to [3D Design Sprint Challenge](/lab-manuals/day-03/design-sprint/) â†’