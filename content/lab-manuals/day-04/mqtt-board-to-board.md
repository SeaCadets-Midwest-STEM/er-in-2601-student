---
title: "Lab: MQTT Board-to-Board Communication"
description: "Connect your Arduino Uno Q to the lab MQTT network and share sensor data wirelessly between stations."
date: 2025-01-01
publish_date: "2026-07-29"
session: "4A"
---

> **Session:** 4A -- Lab: MQTT Network Setup
> **Duration:** 60 minutes
> **Team:** Record your team name and Creation Station number in your notebook
> **Prerequisites:** Day 4 morning lecture on IoT communication completed

---

## Safety

> **SAFETY:** All wiring uses 5V DC from the Arduino Uno Q. Safe to touch. Never short 5V to GND. Wi-Fi credentials are provided by the instructor -- do not share outside the lab.

---

## Objective

Connect your Arduino Uno Q to the local MQTT broker network. Then create a publisher/subscriber system where your station's sensor data is shared with other stations wirelessly.

---

## Parts List

| Part | Qty | How to Identify |
| :--- | :--- | :--- |
| 2004 I2C LCD display | 1 | Already connected at your station |
| Arduino Uno Q | 1 | Mounted at station, Wi-Fi capable |
| LDR sensor | 1 | From Day 2 sessions |
| TMP36 temperature sensor | 1 | From Day 2 sessions |
| Red LED (5mm) | 1 | Response indicator |
| 220 ohm resistor | 1 | Current-limiting |
| Jumper wires | 6 | As needed |

---

## Procedure

### Part 1: Verify Wi-Fi Connection

Before adding MQTT, confirm your Arduino can connect to the lab Wi-Fi.

```cpp
/*
 * Day 4 Lab: Wi-Fi Connection Test
 * Team ___ -- Creation Station #___
 * Purpose: Verify Arduino Uno Q connects to lab Wi-Fi
 * Expected result: LCD shows IP address after connection
 */
#include <WiFiNINA.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

const char* ssid = "LAB_WIFI";       // Provided by instructor
const char* password = "LAB_PASSWORD"; // Provided by instructor

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Connecting to WiFi... ");

  WiFi.begin(ssid, password);

  int dots = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    lcd.setCursor(0, 1);
    for (int i = 0; i < dots; i++) {
      lcd.print(".");
    }
    dots++;
    if (dots > 10) {
      lcd.setCursor(0, 2);
      lcd.print("Check credentials   ");
    }
  }

  lcd.setCursor(0, 1);
  lcd.print("WiFi connected!      ");
  lcd.setCursor(0, 2);
  lcd.print("IP: " + WiFi.localIP().toString() + "   ");
}

void loop() {
  // Nothing to do -- connection verified in setup
}
```

1. Replace `LAB_WIFI` and `LAB_PASSWORD` with credentials provided by instructor
2. Send the sketch to the board and watch the LCD for connection progress
3. Wait for connection dots, then IP address display

> **EXPECTED RESULT:** LCD line 2 shows "WiFi connected!" and line 3 shows an IP address like `192.168.X.X`. If stuck on dots with "Check credentials" message, verify Wi-Fi credentials and that the lab network is accessible.

---

### Part 2: Set Up MQTT Publisher

Now connect to the MQTT broker and publish sensor readings.

```cpp
/*
 * Day 4 Lab: MQTT Publisher -- Station Sensor Data
 * Team ___ -- Creation Station #___
 * Purpose: Publish LDR light and TMP36 temperature to MQTT broker
 * Expected result: Sensor data displayed on LCD and published to broker
 */
#include <WiFiNINA.h>
#include <PubSubClient.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

const char* ssid = "LAB_WIFI";
const char* password = "LAB_PASSWORD";
const char* broker = "192.168.X.X";  // Provided by instructor

const int STATION_NUM = 1;  // Change to your station number (1-6)

WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

const int LDR_PIN = A0;
const int TEMP_PIN = A1;

unsigned long lastPublish = 0;

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Connecting WiFi...    ");

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  lcd.setCursor(0, 0);
  lcd.print("Connecting MQTT...    ");

  mqttClient.setServer(broker, 1883);
  String clientID = "Station-";
  clientID += STATION_NUM;

  while (!mqttClient.connected()) {
    if (mqttClient.connect(clientID.c_str())) {
      break;
    }
    delay(1000);
  }

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Station #");
  lcd.print(STATION_NUM);
  lcd.print(" Publisher   ");
  lcd.setCursor(0, 3);
  lcd.print("Pub: lab/" + String(STATION_NUM) + "/#  ");
}

void loop() {
  mqttClient.loop();

  if (millis() - lastPublish > 5000) {
    lastPublish = millis();

    int lightValue = analogRead(LDR_PIN);
    String lightTopic = "lab/";
    lightTopic += STATION_NUM;
    lightTopic += "/light";
    mqttClient.publish(lightTopic.c_str(), String(lightValue).c_str());

    int tempValue = analogRead(TEMP_PIN);
    float voltage = tempValue * (5.0 / 1023.0);
    float temperatureC = (voltage - 0.5) * 100.0;
    String tempTopic = "lab/";
    tempTopic += STATION_NUM;
    tempTopic += "/temperature";
    mqttClient.publish(tempTopic.c_str(), String(temperatureC, 1).c_str());

    lcd.setCursor(0, 1);
    lcd.print("Light: " + String(lightValue) + "        ");
    lcd.setCursor(0, 2);
    lcd.print("Temp: " + String(temperatureC, 1) + " C         ");
  }
}
```

#### Configure your station number

Change `const int STATION_NUM = 1;` to your actual station number (1-6). This determines your MQTT topic prefix:
- Station 1 publishes to `lab/1/light` and `lab/1/temperature`
- Station 3 publishes to `lab/3/light` and `lab/3/temperature`

#### Verify publishing

1. Send the sketch to the board with your station number
2. Watch LCD -- confirm it shows "Station #X Publisher" header
3. LCD lines 2-3 should update with light and temperature readings every 5 seconds
4. Cover the LDR -- verify light values change on the LCD

> **EXPECTED RESULT:** LCD header shows station number and "Publisher". Lines 2-3 show live light and temperature readings updating every 5 seconds.

---

### Part 3: Add MQTT Subscriber -- Respond to Other Stations

Now subscribe to another station's sensor data. When their light level drops below a threshold, YOUR LED lights up.

**Partner up:** Your team will pair with another station (instructor will assign pairs).

```cpp
/*
 * Day 4 Lab: MQTT Subscriber -- Cross-Station Response
 * Team ___ -- Creation Station #___
 * Partner Station: Record in your notebook
 * Purpose: Subscribe to partner station's light data and light LED when dark
 * Expected result: LED illuminates when partner station's LDR is covered
 */
#include <WiFiNINA.h>
#include <PubSubClient.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

const char* ssid = "LAB_WIFI";
const char* password = "LAB_PASSWORD";
const char* broker = "192.168.X.X";

const int MY_STATION = 1;        // Your station number
const int PARTNER_STATION = 4;   // Partner station number

WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

const int LED_PIN = 9;
const int DARK_THRESHOLD = 200;  // Light value below this = "dark"

void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  int lightValue = message.toInt();

  lcd.setCursor(0, 2);
  lcd.print("Partner: " + String(lightValue) + "       ");

  if (lightValue < DARK_THRESHOLD) {
    digitalWrite(LED_PIN, HIGH);
    lcd.setCursor(0, 3);
    lcd.print(">>> PARTNER DARK!      ");
  } else {
    digitalWrite(LED_PIN, LOW);
    lcd.setCursor(0, 3);
    lcd.print("  Partner OK           ");
  }
}

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Connecting...       ");
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  mqttClient.setServer(broker, 1883);
  mqttClient.setCallback(callback);

  String clientID = "Station-";
  clientID += MY_STATION;

  while (!mqttClient.connected()) {
    if (mqttClient.connect(clientID.c_str())) {
      String subscribeTopic = "lab/";
      subscribeTopic += PARTNER_STATION;
      subscribeTopic += "/light";
      mqttClient.subscribe(subscribeTopic.c_str());

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print(" Subscribing to #");
      lcd.print(PARTNER_STATION);
      lcd.print("             ");
      lcd.setCursor(0, 1);
      lcd.print("Cover their LDR!    ");
      break;
    }
    delay(1000);
  }
}

void loop() {
  mqttClient.loop();
}
```

#### Test cross-station communication

1. Send the subscriber sketch to the board with your station number AND partner station number
2. Partner team transfers their PUBLISHER sketch (Part 2) to the board
3. Partner covers their LDR sensor
4. YOUR LED should illuminate and LCD should show "PARTNER DARK!"

> **EXPECTED RESULT:** When partner station's LDR is covered (light value drops), your station's LED illuminates wirelessly via MQTT. LCD line 3 shows ">>> PARTNER DARK!" and line 2 shows the received light value.

---

### Part 4: Build the Full Network

With instructor coordination, ALL 6 stations will join the network simultaneously.

#### Network topology

Each station publishes its own sensor data AND subscribes to all other stations using the wildcard topic `lab/+/light`.

#### Combined publisher + subscriber sketch

```cpp
/*
 * Day 4 Lab: Full MQTT Network -- All Stations
 * Team ___ -- Creation Station #___
 * Purpose: Publish own sensors, subscribe to all station light events
 * Expected result: Station reports own data AND responds to all other stations
 */
#include <WiFiNINA.h>
#include <PubSubClient.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

const char* ssid = "LAB_WIFI";
const char* password = "LAB_PASSWORD";
const char* broker = "192.168.X.X";

const int MY_STATION = 1;  // Change to your station

WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

const int LDR_PIN = A0;
const int TEMP_PIN = A1;
const int LED_PIN = 9;

unsigned long lastPublish = 0;
const int DARK_THRESHOLD = 200;

void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  // Ignore our own messages
  String myTopic = "lab/";
  myTopic += MY_STATION;
  if (topic.startsWith(myTopic.c_str())) {
    return;
  }

  int lightValue = message.toInt();
  if (lightValue < DARK_THRESHOLD) {
    digitalWrite(LED_PIN, HIGH);
    delay(200);
    digitalWrite(LED_PIN, LOW);

    lcd.setCursor(0, 3);
    lcd.print("Alert: " + String(topic) + "     ");
  }
}

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Connecting...       ");
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  mqttClient.setServer(broker, 1883);
  mqttClient.setCallback(callback);

  String clientID = "Station-";
  clientID += MY_STATION;

  while (!mqttClient.connected()) {
    if (mqttClient.connect(clientID.c_str())) {
      mqttClient.subscribe("lab/+/light");

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print(" Station #");
      lcd.print(MY_STATION);
      lcd.print(" Network     ");
      lcd.setCursor(0, 3);
      lcd.print("Sub: lab/+/light     ");
      break;
    }
    delay(1000);
  }
}

void loop() {
  mqttClient.loop();

  if (millis() - lastPublish > 5000) {
    lastPublish = millis();

    int lightValue = analogRead(LDR_PIN);
    String lightTopic = "lab/";
    lightTopic += MY_STATION;
    lightTopic += "/light";
    mqttClient.publish(lightTopic.c_str(), String(lightValue).c_str());

    int tempValue = analogRead(TEMP_PIN);
    float voltage = tempValue * (5.0 / 1023.0);
    float temperatureC = (voltage - 0.5) * 100.0;
    String tempTopic = "lab/";
    tempTopic += MY_STATION;
    tempTopic += "/temperature";
    mqttClient.publish(tempTopic.c_str(), String(temperatureC, 1).c_str());

    lcd.setCursor(0, 1);
    lcd.print("My Light: " + String(lightValue) + "     ");
    lcd.setCursor(0, 2);
    lcd.print("My Temp: " + String(temperatureC, 1) + " C      ");
  }
}
```

#### Network verification

| Test | Expected Result |
| :---- | :--------------- |
| One station's LDR covered | ALL other stations flash LED briefly and show alert on LCD |
| Multiple stations covered | Each station responds to every dark event it didn't generate |
| LCD dashboard | Shows own light/temp readings on lines 2-3, network alerts on line 4 |

---

## Verification Checklist

- [ ] Wi-Fi connection test passed (IP address displayed on LCD)
- [ ] MQTT publisher: own sensor data displayed on LCD
- [ ] MQTT subscriber: LED responds to partner station's light level
- [ ] Full network: station publishes own data AND responds to all others
- [ ] Sketches saved with station number in filename

---

## Challenge Extensions

### Challenge 1: Network Dashboard (15 min)

Create a dashboard on the LCD that tracks the last known state of all 6 stations:

```cpp
String stationStates[7];  // Index 1-6, store latest light values

// In callback(): parse station number from topic, update array
// Rotate LCD display to show 2 stations per update cycle
```

### Challenge 2: Alert Cascade (10 min)

When your station detects dark AND receives a dark alert from another station, publish an "ALERT" message on a special topic. Watch how conditions cascade through the network.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
| :------- | :------------ | :--- |
| LCD stuck on "Connecting..." | Wrong SSID/password or lab network unavailable | Verify credentials with instructor |
| MQTT connection never completes | Broker not running, wrong IP, or firewall blocking port 1883 | Ask instructor to verify Mosquitto |
| Published messages don't appear | Wrong topic or `mqttClient.loop()` not called | Verify topic string. Ensure `loop()` includes `mqttClient.loop()` |
| Callback never fires | Not subscribed to correct topic or wildcard syntax wrong | Verify subscribe topic. `+` = single level, `#` = subtree |
| LED responds to OWN data | Callback doesn't filter own messages | Add topic check in callback to skip own station |
| `WiFiNINA` / `PubSubClient` not found | Library not pre-installed | Notify instructor |

---

## Key Concept Summary

**MQTT enables many-to-many device communication through a central broker.** Instead of wiring every device to every other device, each device publishes messages to topics and subscribes to topics it cares about. The broker handles all the routing.

**The publish/subscribe pattern is everywhere:**
- Smart home systems (Nest, Home Assistant)
- Industrial IoT (factory sensor networks)
- Message queues in software (RabbitMQ, Apache Kafka)
- Real-time notifications (chat apps, news feeds)

---

## Next Up

Continue to [Motion Pattern Data Collection](/lab-manuals/day-04/data-collection/)
