---
title: "Lab: Motion Pattern Data Collection"
description: "Collect labeled sensor data for different movement patterns using PIR and ultrasonic sensors."
date: 2025-01-01
publish_date: "2026-07-29"
session: "4B"
---

> **Session:** 4B -- Data Collection Lab
> **Duration:** 60 minutes
> **Team:** Record your team name and Creation Station number in your notebook
> **Prerequisites:** Day 4 morning lecture on machine learning fundamentals completed

---

## Safety

> **SAFETY:** All wiring uses 5V DC from the Arduino Uno Q. Safe to touch. Movement activities require clear space around station -- keep walkways unobstructed.

> **SAFETY:** Running or rapid movement near equipment. Designate a "movement zone" at least 3 meters clear of other stations.

---

## Objective

Collect labeled sensor data for different movement patterns. Each team will record approximately 20 examples per movement class using PIR and ultrasonic sensors. This data will be used to train a machine learning model.

---

## Parts List

| Part | Qty | How to Identify |
| :--- | :--- | :--- |
| Arduino Uno Q | 1 | Mounted at station |
| 2004 I2C LCD display | 1 | Already connected at your station |
| PIR sensor (AM312) | 1 | Mounted, facing movement zone |
| HC-SR04 ultrasonic sensor | 1 | Mounted, facing movement zone |
| microSD card (4GB or smaller) | 1 | Format FAT32 |
| microSD card shield/module | 1 | Stacks on Arduino |
| 4x momentary pushbuttons | 1 each | Movement class selection |
| 4x 10k ohm pull-down resistors | 1 each | Button inputs |
| Green LED (5mm) | 1 | Recording indicator |
| 220 ohm resistor | 1 | Current-limiting |
| Jumper wires | As needed | Sensor connections |

---

## Procedure

### Part 1: Wire the Button Panel and SD Card Shield

Stack the microSD card shield on top of your Arduino Uno Q. Insert a formatted microSD card (4GB or smaller, FAT32 format).

#### Button panel

Connect 4 pushbuttons to digital pins 3, 4, 5, and 6:

| Button | Arduino Pin | Movement Class |
| :------ | :---------- | :-------------- |
| Button 1 (Pin 3) | Digital 3 | WALKING |
| Button 2 (Pin 4) | Digital 4 | RUNNING |
| Button 3 (Pin 5) | Digital 5 | STANDING |
| Button 4 (Pin 6) | Digital 6 | WAVING |

Each button connects one side to its digital pin, the other side to GND. Add a 10k ohm pull-down resistor from each pin to GND.

#### Recording LED

Connect green LED (through 220 ohm resistor) to digital pin 9, cathode to GND. LED illuminates during recording.

---

### Part 2: Transfer the Data Logger Sketch

```cpp
/*
 * Day 4 Lab: Motion Pattern Data Collector
 * Team ___ -- Creation Station #___
 * Purpose: Record PIR + ultrasonic readings to SD card for ML training
 * Expected result: LCD shows menu, button press starts 5-second recording saved to SD
 */
#include <LiquidCrystal_I2C.h>
#include <SD.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

// Sensor pins
const int PIR_PIN = 2;
const int TRIG_PIN = 7;
const int ECHO_PIN = 8;

// Button pins (WALKING, RUNNING, STANDING, WAVING)
const int BTN_WALK = 3;
const int BTN_RUN = 4;
const int BTN_STAND = 5;
const int BTN_WAVE = 6;

// Recording LED
const int LED_PIN = 9;

// SD card
const int CHIP_SELECT = 4;

// Recording parameters
const int SAMPLE_INTERVAL = 100;
const int SAMPLES_PER_RECORDING = 50;

// State
int recordingCount = 0;
bool isRecording = false;
File dataFile;

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();

  pinMode(PIR_PIN, INPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(BTN_WALK, INPUT);
  pinMode(BTN_RUN, INPUT);
  pinMode(BTN_STAND, INPUT);
  pinMode(BTN_WAVE, INPUT);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  lcd.setCursor(0, 0);
  lcd.print("Initializing SD...    ");
  if (!SD.begin(CHIP_SELECT)) {
    lcd.setCursor(0, 1);
    lcd.print("SD FAILED! Check card ");
    return;
  }

  dataFile = SD.open("station.csv", FILE_WRITE);
  if (!dataFile) {
    lcd.setCursor(0, 1);
    lcd.print("File open failed!   ");
    return;
  }

  dataFile.println("timestamp,pir,distance,label");

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Motion Data Logger    ");
  lcd.setCursor(0, 1);
  lcd.print(" Records: " + String(recordingCount) + "         ");
  lcd.setCursor(0, 2);
  lcd.print(" [3]Walk [4]Run       ");
  lcd.setCursor(0, 3);
  lcd.print(" [5]Stand [6]Wave     ");
}

void loop() {
  if (isRecording) return;

  if (digitalRead(BTN_WALK) == HIGH) {
    recordSession("WALKING");
  } else if (digitalRead(BTN_RUN) == HIGH) {
    recordSession("RUNNING");
  } else if (digitalRead(BTN_STAND) == HIGH) {
    recordSession("STANDING");
  } else if (digitalRead(BTN_WAVE) == HIGH) {
    recordSession("WAVING");
  }

  delay(300);
}

void recordSession(String label) {
  isRecording = true;
  digitalWrite(LED_PIN, HIGH);

  lcd.setCursor(0, 1);
  lcd.print(">> Recording: " + label + " ");

  for (int i = 0; i < SAMPLES_PER_RECORDING; i++) {
    int pir = digitalRead(PIR_PIN);

    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    long duration = pulseIn(ECHO_PIN, HIGH, 30000);
    int distance = 0;
    if (duration > 0) {
      distance = (duration * 0.034 / 2);
    }

    unsigned long ts = millis();
    dataFile.print(ts);
    dataFile.print(",");
    dataFile.print(pir);
    dataFile.print(",");
    dataFile.print(distance);
    dataFile.print(",");
    dataFile.println(label);

    if (i % 10 == 0) {
      lcd.setCursor(0, 2);
      lcd.print("  Sample " + String(i) + "/" + String(SAMPLES_PER_RECORDING) + "    ");
    }

    delay(SAMPLE_INTERVAL);
  }

  recordingCount++;
  dataFile.flush();

  digitalWrite(LED_PIN, LOW);
  isRecording = false;

  lcd.setCursor(0, 1);
  lcd.print(" Records: " + String(recordingCount) + "         ");
  lcd.setCursor(0, 2);
  lcd.print("  Last: " + label + "          ");
  lcd.setCursor(0, 3);
  lcd.print(" Press button to add   ");

  delay(1000);

  lcd.setCursor(0, 2);
  lcd.print(" [3]Walk [4]Run       ");
  lcd.setCursor(0, 3);
  lcd.print(" [5]Stand [6]Wave     ");
}
```

#### Verify the logger

1. Send the sketch to the board
2. LCD shows "Motion Data Logger" menu with button instructions
3. Press Button 3 (WALKING) -- LED illuminates for 5 seconds, LCD shows recording progress
4. After recording, LCD shows "Records: 1" and "Last: WALKING"

> **EXPECTED RESULT:** LCD displays menu. Pressing a button starts a 5-second recording (green LED on). After recording, the counter increments and LCD confirms the saved class label.

---

### Part 3: Set Up the Movement Zone

1. **Mount sensors consistently:** PIR and ultrasonic sensors should face the same direction, aimed at a clear area at least 3 meters long
2. **Mark the zone:** Use tape on the floor to mark "start" and "end" positions
3. **Clear obstacles:** Ensure the movement zone is free of equipment and people from other teams

---

### Part 4: Collect Training Data

Each team needs **20 recordings per movement class** (80 total recordings).

#### Movement classes

| Class | Movement Description | Duration |
| :----- | :------------------- | :-------- |
| **WALKING** | Walk at normal pace from START to END, then return | ~5 seconds |
| **RUNNING** | Jog quickly from START to END | ~5 seconds |
| **STANDING** | Stand 1 meter from sensors. Remain still | 5 seconds |
| **WAVING** | Stand 1 meter from sensors. Wave one hand side-to-side | 5 seconds |

#### How to record each example

1. **Performer gets into position**
2. **Operator presses button** for movement class
3. **Performer starts movement** immediately after button press (green LED indicates recording)
4. **Recording runs for 5 seconds** (50 samples at 100ms intervals)
5. **LCD confirms** recording saved with class label
6. **Log the recording** and repeat

---

### Part 5: Hand Off Data to Instructor

At the end of the lab, the instructor collects the microSD card from each station and verifies data quality.

---

## Verification Checklist

- [ ] Data logger sketch sent to board and tested
- [ ] SD card initialized successfully
- [ ] Button press starts recording (green LED on for 5 seconds)
- [ ] LCD shows recording count incrementing
- [ ] Movement zone set up with sensors mounted consistently
- [ ] 20 WALKING recordings collected
- [ ] 20 RUNNING recordings collected
- [ ] 20 STANDING recordings collected
- [ ] 20 WAVING recordings collected
- [ ] LCD shows total of 80 records
- [ ] SD card handed to instructor

---

## Challenge Extensions

### Challenge 1: Add a Fifth Class (15 min)

Add a fifth button for a movement class of your choice: "TIPTOING", "DANCING", or "POINTING". Wire the button, update the sketch, and collect 20 recordings.

### Challenge 2: Feature Engineering Preview (10 min)

Compute features BEFORE saving to SD:
- PIR transition count
- Average distance
- Distance range (max - min)

Add a summary line after each recording on the LCD.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
| :------- | :------------ | :--- |
| LCD shows "SD FAILED!" | SD card not inserted, wrong format, or wrong CS pin | Insert card. Format FAT32 (4GB max). Check CS pin |
| Button press does nothing | Button not wired correctly or pull-down resistors missing | Check button connections. Verify 10k ohm resistors to GND |
| Distance readings are 0 | Ultrasonic sensor not wired correctly | Check jumper wires. Verify TRIG=7, ECHO=8 |
| PIR always reads HIGH | Sensor still calibrating | Wait 60 seconds for calibration |
| Recordings look the same | Performer not varying movements enough | Review movement descriptions. Move closer to sensors |

---

## Key Concept Summary

**Data collection is the foundation of machine learning.** The quality of your training data determines the quality of your model -- "garbage in, garbage out" (GIGO).

**What makes good training data:**
- **Quantity:** Enough examples to cover variation (20+ per class)
- **Quality:** Labels accurately describe what was happening
- **Diversity:** Different people, slight variations
- **Consistency:** Same sensor setup, same measurement zone

---

## Previous Labs

[Back to MQTT Board-to-Board Communication](/lab-manuals/day-04/mqtt-board-to-board/)
