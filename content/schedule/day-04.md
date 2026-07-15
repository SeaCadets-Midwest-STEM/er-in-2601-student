---
title: "Day 4 - The Connected Hive"
date: 2026-07-30
weight: 4
---

## Theme: IoT Communication, MQTT, BLE, and Real-Time Dashboards

On Day 4, your team's Arduino Uno Q joins a network. You'll publish sensor data over MQTT, control actuators via BLE, and watch your team's telemetry appear live on a Node-RED dashboard.

### Sessions

- **"The Silent Alarm"** - Hook Demo: A sensor detects something but no one knows
- **MQTT Overview** - Publish/subscribe messaging, topics, brokers, and payloads
- **MQTT Board-to-Board** - Connect your station to the local Mosquitto broker and publish temperature from a TMP36 sensor
- **Data Collection Lab** - Log motion patterns (PIR + ultrasonic) to a microSD card as CSV data
- **BLE Control** - Use BLE to wirelessly control a servo motor from another board
- **Node-RED Dashboard** - Watch your station's live telemetry on the instructor dashboard

### Key Concepts

| Term | Definition |
|------|-----------|
| MQTT | Lightweight publish/subscribe messaging protocol designed for IoT devices |
| Topic | A named channel in MQTT - publishers send to topics, subscribers receive from them |
| Broker | The server that routes messages between publishers and subscribers (Mosquitto in our lab) |
| Payload | The actual data sent in a message, often formatted as JSON |
| BLE | Bluetooth Low Energy - short-range wireless communication built into the Arduino Uno Q |
| Node-RED | Visual programming tool for wiring together hardware and APIs, used here for live dashboards |

### Your Station's MQTT Topic

Each team publishes to a unique topic path based on your station number:

```
il2026/stationX/sensor      (sensor readings)
il2026/stationX/temperature  (TMP36 temperature data)
il2026/stationX/control      (BLE actuator commands)
```

Replace `X` with your station number (1-6).

### What to Bring

- Your team - all IoT components (TMP36, PIR, servo, microSD) are at your Creation Station
- Your circuits from Days 1-3 remain at your station

### Lab Manuals

Today's lab manuals are available below. Follow along with the detailed instructions as you work through each session.

- [MQTT Board-to-Board](/lab-manuals/day-04/mqtt-board-to-board/) - Connect to the local Mosquitto broker and publish sensor data
- [Data Collection Lab](/lab-manuals/day-04/data-collection/) - Log motion patterns to microSD as CSV data
