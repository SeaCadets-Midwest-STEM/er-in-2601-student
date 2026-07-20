---
title: "HC-SR04 Ultrasonic Distance Sensor"
description: "Measures distance to objects using sound waves, like a bat using echolocation."
date: 2026-07-20
categories: ["sensor", "distance"]
---

## What Is It?

The HC-SR04 measures how far away an object is by sending out an invisible sound pulse and timing how long it takes to bounce back — the same way bats "see" in the dark.

**Range:** 2 cm to 400 cm (about 1 inch to 13 feet)  
**Accuracy:** ±3 mm (about 1/8 inch)

## When to Use It

- Parking-sensor style alerts ("backing up" warnings)
- Measuring water level in a tank
- Motion detection (did the distance just change?)
- Obstacle avoidance for robots

## Pinout

The module has 4 pins:

| Pin | Connect To |
|---|---|
| `VCC` | Arduino `5V` |
| `GND` | Arduino `GND` |
| `TRIG` | Any digital pin (e.g., `D2`) |
| `ECHO` | Any digital pin (e.g., `D3`) |

## How It Works (Simple)

1. Arduino tells the sensor: "send a sound pulse" (sets `TRIG` HIGH)
2. The sensor beeps at a frequency humans can't hear
3. The sound hits an object and bounces back
4. The sensor sets `ECHO` HIGH for the same amount of time the sound was in the air
5. Arduino measures how long `ECHO` stayed HIGH → that time becomes distance

## Example Code

```cpp
const int trigPin = 2;
const int echoPin = 3;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // Send a short pulse on TRIG
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure how long ECHO stays HIGH
  long duration = pulseIn(echoPin, HIGH);

  // Convert to centimeters
  float distanceCm = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.print(distanceCm);
  Serial.println(" cm");

  delay(500);
}
```

## Common Pitfalls

- **Minimum distance:** Objects closer than 2 cm may not register. Don't expect accurate readings up close.
- **Soft surfaces:** Fabric, foam, and curved surfaces absorb sound and can give wrong readings.
- **Angle matters:** Sound bounces straight back. Tilt the sensor too much and the echo is lost.