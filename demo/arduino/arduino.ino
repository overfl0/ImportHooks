// https://www.instructables.com/id/Arduino-Button-with-no-resistor/
// Connect the button between the GND and PIN 12
// Sending the 'r' command while pressing the button will give you another stream of data back
// than when the button is not pressed

int buttonPin = 12;
int LED = 13;

void setup() {
  Serial.begin(115200); // use the same baud-rate as the python side
  pinMode(buttonPin, INPUT_PULLUP); // Hooray! Free resistors!
  pinMode(LED, OUTPUT);
}

void printStuff(const char *text)
{
  char length[100]; // Screw buffer overflows!
  sprintf(length, "%d\n", strlen(text)); // Screw error handling!
  Serial.print(length);
  Serial.print(text);
}

void loop() {
  int buttonValue = digitalRead(buttonPin);
  if (buttonValue == LOW){
    // If button pushed, turn LED on
    digitalWrite(LED,HIGH);
  } else {
    // Otherwise, turn the LED off
    digitalWrite(LED, LOW);
  }

  if(Serial.available() > 0) {
    char data = Serial.read();

    if (data == 'r') {
      if (buttonValue == LOW) {
        printStuff("print(\"Okay, you won! Executing secret stuff!\")");
      } else {
        printStuff("raise ImportError(\"Try harder!\")");
      }
    }
  }
  delay(100);
}
