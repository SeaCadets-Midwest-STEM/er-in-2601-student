---
title: "TMP36 Temperature Sensor"
description: "Reads the ambient temperature and outputs a voltage that Arduino can read easily."
date: 2026-07-20
categories: ["sensor", "temperature"]
---

## What Is It?

The TMP36 is a tiny analog temperature sensor. It outputs a voltage that changes with temperature, and the Arduino reads that voltage with `analogRead()`. Think of it as a thermometer that speaks in voltage instead of numbers.

**Range:** −40°C to +125°C (−40°F to +257°F)  
**Output:** 0.0V to 1.75V (safe for Arduino's analog pins)

## When to Use It

- Room temperature monitoring
- Weather station projects
- Overheat warnings
- Any project that needs to react to hot or cold conditions

## Pinout

The TMP36 is a small 3-pin component (TO-92 package, looks like a transistor):

| Pin | Connect To |
|---|---|
| Pin 1 (left, facing the flat side) | Arduino `5V` |
| Pin 2 (center) | Arduino analog pin (e.g., `A0`) |
| Pin 3 (right) | Arduino `GND` |

## How It Works (Simple)

The sensor outputs a voltage that increases as temperature rises:

- **−40°C** → 0.0V (Arduino reads 0)
- **25°C** (room temp) → 0.75V (Arduino reads ~153)
- **125°C** → 1.75V (Arduino reads ~357)

Arduino's analog input reads 0–1023 (representing 0–5V). The formula to convert:

```
voltage = reading × (5.0 / 1024.0)
tempC   = (voltage − 0.5) / 0.01
tempF   = tempC × 1.8 + 32
```

## Example Code

```cpp
const int tempPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int reading = analogRead(tempPin);

  // Convert to voltage
  float voltage = reading * (5.0 / 1024.0);

  // Convert to temperature
  float tempC = (voltage - 0.5) / 0.01;
  float tempF = tempC * 1.8 + 32.0;

  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.print(" °C  /  ");
  Serial.print(tempF);
  Serial.println(" °F");

  delay(1000);
}
```

## Common Pitfalls

- **Your finger warms it up:** Touching the sensor will raise the reading. Let it settle for a few seconds before reading.
- **Pin order:** Make sure you're facing the flat side of the sensor with the text toward you. Pin 1 is on the left.
- **Slow response:** The TMP36 takes a moment to adjust to temperature changes. Don't expect instant updates.