---
title: "Lab: Capstone Device Integration"
description: "Integrate sensors, wireless communication, visual output, and 3D printed enclosure into a complete Hidden Economy device."
date: 2025-01-01
publish_date: "2026-07-31"
session: "5A"
---

> **Session:** 5A -- Capstone Build Block I
> **Duration:** 90 minutes
> **Team:** Record your team name and Creation Station number in your notebook
> **Prerequisites:** Days 1-4 labs completed (sensors, communications, 3D printing)

---

## Safety

> **SAFETY:** All wiring uses 5V DC from the Arduino Uno Q. Safe to touch. Allow boards to cool between firmware transfers.

> **SAFETY:** Hot glue guns (if used for enclosure assembly) reach high temperatures. Use caution with fingers and skin.

> **SAFETY:** Keep walkways clear of cables and components. Two Arduino boards per station may create cable clutter -- organize early.

---

## Objective

Integrate the components you built over the past four days into a single working device that demonstrates a "Hidden Economy" concept. Your device should combine:

- **Sensor input** (LDR, TMP36, ultrasonic, potentiometer, or button)
- **Wireless communication** (MQTT or BLE)
- **Visual output** (MAX7219 matrix, LEDs, or LCD display)
- **3D printed enclosure** (from your Day 3 design)

The goal is integration and demonstration, not perfection. A working pipeline that tells a story is more valuable than a polished device with broken communication.

---

## Parts List

| Part | Qty | Purpose |
| :--- | :--- | :------- |
| Arduino Uno Q board | 2 | Primary board (sensors + output) + secondary board (wireless receiver) |
| USB cable (Micro-B to USB-A) | 2 | Power + programming for both boards |
| Breadboard (830-point) | 1 | Circuit prototyping |
| Jumper wires (assorted) | 20+ | M-M, M-F, F-F connections |
| LDR (photoresistor) | 1 | Light sensor |
| 10K ohm resistor | 2 | Voltage divider for LDR |
| Potentiometer (10K ohm) | 1 | Analog knob input |
| Ultrasonic sensor (HC-SR04) | 1 | Distance measurement |
| TMP36 temperature sensor | 1 | Temperature reading |
| LED (assorted colors) | 3 | Visual output indicators |
| 220 ohm resistors | 3 | LED current limiting |
| Button (momentary) | 1 | Digital input |
| MAX7219 8x8 matrix display | 1 | Visual output |
| 2004 I2C LCD display | 1 | Debug output |
| Day 3 printed enclosure | 1 | Per team (from Day 3 prints) |
| Cable ties/zip ties | 10 | Cable management |
| Tape or velcro strips | Assorted | Secure components |

> **TIP:** Not all teams need every component listed. Refer to your team's scenario card for required parts. Use this list as a catalog of what's available.

---

## Procedure

### Step 1: Review Your Scenario Card (10 minutes)

Each team received a capstone scenario card. Review it together:

| Field | What to Look For |
| :---- | :--------------- |
| **Project Name** | Your team's assigned scenario |
| **Core Requirements** | Sensors needed, communication method, output type |
| **Hidden Economy Connection** | How your device relates to supply chain, logistics, or commerce |
| **Printed Part** | The 3D enclosure component from Day 3 |

**As a team, discuss:**
1. What sensor(s) will we use?
2. Will we use MQTT or BLE for wireless?
3. What will the output look like?
4. How will the printed enclosure house or mount the device?

**Assign roles:**
- **Coder:** Writes and sends firmware to the board
- **Hardware Tech:** Wires circuits, manages enclosure integration
- **Observer/Documenter:** Tracks progress, drafts description card, takes notes

> **INSTRUCTOR NOTE:** Roles rotate every 20 minutes. Instructor calls "Rotate!" and teams shift roles clockwise.

---

### Step 2: Wire the Sensor Circuit (20 minutes)

Based on your scenario, wire the required sensor(s) to the primary Arduino board.

#### LDR (Light Sensor) -- Voltage Divider

| LDR Pin | Arduino Pin |
| :------ | :---------- |
| One side | 5V |
| Other side | A0 (analog input) |
| Also connect 10K ohm resistor from A0 to GND | |

#### TMP36 (Temperature Sensor)

| TMP36 Pin | Arduino Pin |
| :-------- | :---------- |
| Pin 1 (left, flat side facing you) | 5V |
| Pin 2 (center) | A1 (analog input) |
| Pin 3 (right) | GND |

#### Ultrasonic Sensor (HC-SR04)

| HC-SR04 Pin | Arduino Pin |
| :---------- | :---------- |
| VCC | 5V |
| TRIG | Digital 7 |
| ECHO | Digital 8 |
| GND | GND |

#### Button (Digital Input)

| Button Pin | Arduino Pin |
| :--------- | :---------- |
| One side | Digital 2 |
| Other side | GND |
| Also connect 10K ohm resistor from Digital 2 to GND (pull-down) | |

#### Potentiometer

| Potentiometer Pin | Arduino Pin |
| :---------------- | :---------- |
| Pin 1 (left) | GND |
| Pin 2 (center) | A2 (analog input) |
| Pin 3 (right) | 5V |

> **EXPECTED RESULT:** Sensor wired. Team can read raw values on LCD debug display.

---

### Step 3: Write and Send Firmware (30 minutes)

Combine code patterns from previous labs into a single sketch.

#### Sensor Reading Template

```cpp
/*
 * Capstone: [Team Project Name]
 * Team ___ -- Creation Station #___
 * Purpose: [1-sentence description]
 * Expected result: Sensor reads values, sends data wirelessly, output responds
 */

// Include libraries based on communication method
// For MQTT:
#include <WiFiNINA.h>
#include <PubSubClient.h>

// For BLE:
#include <ArduinoBLE.h>

// For display:
#include <LiquidCrystal_I2C.h>
#include <LedControl.h>

// --- Sensor pins ---
const int SENSOR_PIN = A0;  // Change based on your sensor
const int BUTTON_PIN = 2;

// --- Display ---
LiquidCrystal_I2C lcd(0x27, 20, 4);

// --- Communication ---
// MQTT setup (if using MQTT):
// WiFiClient wifiClient;
// PubSubClient mqttClient(wifiClient);
// const char* broker = "192.168.X.X";

void setup() {
  lcd.begin();
  lcd.backlight();

  pinMode(SENSOR_PIN, INPUT);
  pinMode(BUTTON_PIN, INPUT);

  // Initialize communication here
  // mqttClient.setServer(broker, 1883);

  lcd.setCursor(0, 0);
  lcd.print(" [Project Name]       ");
  lcd.setCursor(0, 1);
  lcd.print(" Status: Ready         ");
}

void loop() {
  // Read sensor
  int sensorValue = analogRead(SENSOR_PIN);

  // Display on LCD
  lcd.setCursor(0, 2);
  lcd.print(" Sensor: " + String(sensorValue) + "          ");

   // Send wirelessly (pseudo-code -- replace with your method)
  // sendData(sensorValue);

  // Update output (LED, matrix, etc.)
  updateOutput(sensorValue);

  delay(500);
}

void updateOutput(int value) {
  // Map sensor value to output behavior
  // Example: brighter LED for higher values
  int brightness = map(value, 0, 1023, 0, 255);
  // analogWrite(LED_PIN, brightness);
}

void sendData(int value) {
  // MQTT example:
  // String payload = String(value);
  // mqttClient.publish("station/X/data", payload.c_str());

  // BLE example:
  // characteristic.writeValue(value);
}
```

> **TIP:** Start with the sensor reading working on LCD first. Then add wireless. Then add output. Build one piece at a time.

---

### Step 4: Test End-to-End Data Flow (15 minutes)

Verify the complete pipeline:

1. **Sensor input:** Change the sensor (cover LDR, blow on TMP36, wave hand at ultrasonic). LCD shows changing values.
2. **Wireless transmission:** Check with instructor using MQTT Explorer or BLE scanner that data is being sent.
3. **Output response:** LED, matrix, or dashboard reacts to sensor changes.

> **EXPECTED RESULT:** Touch the sensor -> value changes on LCD -> data appears on wireless receiver -> output device responds.

---

### Step 5: Integrate Printed Enclosure (15 minutes)

Fit your circuit into the 3D printed enclosure from Day 3:

1. Place the Arduino and breadboard inside the enclosure
2. Route sensor cables through designated openings
3. Secure with cable ties or tape
4. Verify the device still functions with enclosure installed

> **TIP:** If the fit is tight, note it on your description card as "Iteration needed: enclosure revision for cable clearance." This is honest engineering documentation.

---

## Verification Checklist

Before the instructor go/no-go check, verify:

- [ ] Sensor reads correct values (confirmed on LCD)
- [ ] Wireless communication active (MQTT connected OR BLE advertising)
- [ ] Output responds to sensor input
- [ ] Printed enclosure houses or mounts the device
- [ ] All team members can explain what the device does
- [ ] Description card drafted (team name, project name, technologies used)

---

## Challenge Extensions

If your team finishes the core requirements early:

### Challenge 1: Add a Second Sensor (10 min)

Combine two sensors for richer data. Example: LDR + TMP36 for "warehouse environment monitoring" that tracks both light and temperature.

### Challenge 2: Add Hysteresis (5 min)

Add threshold logic so the output only changes when the sensor crosses a boundary (prevents flickering). Example: LED turns on only when temperature rises above 25 C and stays on until it drops below 23 C.

### Challenge 3: Improve the Description Card (5 min)

Add technical detail: wiring diagram sketch, data flow description, or lessons learned during build.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
| :------- | :------------ | :--- |
| MQTT not connecting | Wrong broker IP. WiFi credentials incorrect. | Verify broker address (ask instructor). Check WiFiNINA credentials. |
| BLE not pairing | Wrong peripheral address. UUID mismatch. | Verify address shown on LCD. Restart BLE service on both boards. |
| Sensor reads garbage (all 0 or all 1023) | Wrong pin. Voltage divider missing resistor. | Check pin assignment. Verify wiring matches table above. |
| Matrix display blank | VCC/GND reversed. Wrong CS pin. Library not included. | Check MAX7219 wiring. Verify `#include <LedControl.h>`. |
| LCD shows nothing | I2C address wrong. Wires loose. | Try address 0x3F instead of 0x27. Recheck 4-wire connection. |
| Code won't compile | Missing library. Wrong pin definition. Missing semicolon. | Check error message in Arduino IDE. Look for red underline. |
| Enclosure doesn't fit | Tolerance issue. Cable bulk larger than expected. | Note as "iteration needed." Use without full enclosure for demo. |
| Board gets hot during firmware transfer | Normal during transfer. Should cool within 30 seconds. | Allow to cool before continuing. |

---

## Key Concept Summary

**Integration is the hardest part of engineering.** Each component worked individually in earlier labs. Putting them together reveals hidden assumptions, wiring conflicts, and timing issues. This is normal and expected.

**What you're practicing today:**
- **Systems thinking:** How individual components interact as a whole
- **Debugging:** Isolating which part of the pipeline is broken
- **Team coordination:** Three people, one goal, shared ownership
- **Engineering communication:** Explaining your device to others (description card, demo loop)

These skills are more valuable than any single sensor reading or code snippet.

---

## Notes for Demo Day

After lunch, your team will set up a demo station. Practice a 3-minute loop:

1. Show the device in its enclosure (30 sec)
2. Interact with the sensor -- show the input changing (30 sec)
3. Show the wireless output (60 sec)
4. Explain the data flow: "Sensor -> Board -> MQTT/BLE -> Display" (60 sec)
