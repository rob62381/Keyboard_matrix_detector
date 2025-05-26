// ESP32 Keyboard Matrix Mapper

// Adjust NUM_ROWS and NUM_COLS as needed (edit to match keyboard matrix)
#define NUM_ROWS 8
#define NUM_COLS 10

// GPIO pins for rows and columns (edit these to match your wiring)
int row_pins[NUM_ROWS] = {13, 12, 14, 27, 26, 25, 33, 32};
int col_pins[NUM_COLS] = {4, 16, 17, 5, 18, 19, 21, 22, 23, 15};

void setup() {
  Serial.begin(115200);

  // Set up row pins as outputs
  for (int i = 0; i < NUM_ROWS; i++) {
    pinMode(row_pins[i], OUTPUT);
    digitalWrite(row_pins[i], LOW);
  }

  // Set up column pins as inputs with pull-downs
  for (int i = 0; i < NUM_COLS; i++) {
    pinMode(col_pins[i], INPUT_PULLDOWN);
  }

  Serial.println("Matrix Mapper Ready. Press each key as prompted.");
}

void loop() {
  for (int r = 0; r < NUM_ROWS; r++) {
    // Set current row HIGH
    digitalWrite(row_pins[r], HIGH);

    delay(5); // small delay to stabilize

    for (int c = 0; c < NUM_COLS; c++) {
      if (digitalRead(col_pins[c])) {
        Serial.print("Key Press Detected at ROW ");
        Serial.print(r);
        Serial.print(" / COL ");
        Serial.println(c);

        Serial.println("Label this key (e.g. ESC, A, F1): ");
        while (!Serial.available());
        String label = Serial.readStringUntil('\n');
        label.trim();
        Serial.print("Mapped ROW ");
        Serial.print(r);
        Serial.print(" COL ");
        Serial.print(c);
        Serial.print(" to: ");
        Serial.println(label);
      }
    }

    // Set current row LOW again
    digitalWrite(row_pins[r], LOW);
  }

  delay(200); // Polling interval
}
