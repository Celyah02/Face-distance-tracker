#include <Stepper.h>
const int stepsPerRevolution = 2048; // 28BYJ-48 motor
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);
void setup() {
  myStepper.setSpeed(10); // adjust speed (RPM)
  Serial.begin(9600);
  Serial.println("Stepper Motor Ready...");
}
void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();
    if (input.startsWith("rotate")) {
      int angle = input.substring(6).toInt();
      long steps = (long)angle * stepsPerRevolution / 360;
      myStepper.step(steps);
      Serial.print("Rotated ");
      Serial.print(angle);
      Serial.println(" degrees");
    }
  }
}