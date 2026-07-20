---
title: "Arduino Uno Q — Onboard 8×13 RGB LED Matrix"
description: "A built-in grid of 104 RGB LEDs on the Arduino Uno Q — no wiring needed."
date: 2026-07-20
categories: ["output", "display", "led", "onboard"]
---

## What Is It?

The Arduino Uno Q has a built-in grid of 104 RGB LEDs arranged in 8 rows and 13 columns. Each LED can display any color, and you control them all from code — no wiring required.

- **Grid size:** 8 rows × 13 columns = 104 LEDs
- **Colors:** Each LED can be any color (RGB = 16+ million colors)
- **Location:** Built into the board — no breadboard or wires needed

## When to Use It

- Displaying text or simple graphics
- Visual feedback (patterns, animations, status indicators)
- Color-coded output (red = error, green = OK)
- Scrolling messages
- Quick debugging (flash a color to confirm code reached a point)

## How It Works (Simple)

The LED matrix is controlled through the Arduino IDE using a built-in library. You address each LED by its row and column position, and set the color using red, green, and blue values (0–255 each).

- **Row 0–7:** The 8 rows (top to bottom)
- **Column 0–12:** The 13 columns (left to right)
- **Color:** `setPixel(row, col, red, green, blue)` where each value is 0–255

## Example Code

```cpp
#include <Arduino_LED_Matrix.h>
Arduino_LED_Matrix ledMatrix;

void setup() {
  ledMatrix.begin();

  // Set a single LED to red
  ledMatrix.setPixel(0, 0, 255, 0, 0);

  // Set another to green
  ledMatrix.setPixel(7, 12, 0, 255, 0);
}

void loop() {
  // Flash all LEDs white, then off
  for (int row = 0; row < 8; row++) {
    for (int col = 0; col < 13; col++) {
      ledMatrix.setPixel(row, col, 255, 255, 255);
    }
  }
  delay(500);

  for (int row = 0; row < 8; row++) {
    for (int col = 0; col < 13; col++) {
      ledMatrix.setPixel(row, col, 0, 0, 0);
    }
  }
  delay(500);
}
```

### Color Examples

| Color | Red | Green | Blue | Code |
|---|---|---|---|---|
| Red | 255 | 0 | 0 | `setPixel(r, c, 255, 0, 0)` |
| Green | 0 | 255 | 0 | `setPixel(r, c, 0, 255, 0)` |
| Blue | 0 | 0 | 255 | `setPixel(r, c, 0, 0, 255)` |
| Yellow | 255 | 255 | 0 | `setPixel(r, c, 255, 255, 0)` |
| White | 255 | 255 | 255 | `setPixel(r, c, 255, 255, 255)` |
| Off | 0 | 0 | 0 | `setPixel(r, c, 0, 0, 0)` |

## Common Pitfalls

- **Forget `ledMatrix.begin()`:** The matrix won't work without calling `begin()` in `setup()`.
- **Rows and columns reversed:** Rows are 0–7 (8 rows), columns are 0–12 (13 columns). Going out of range silently does nothing.
- **LEDs don't update instantly:** The matrix refreshes automatically, but complex animations may need small `delay()` calls to be visible.
- **No wiring needed:** Don't try to connect external wires to the matrix. It's controlled entirely through code.