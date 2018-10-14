// https://www.instructables.com/id/Arduino-Button-with-no-resistor/
// Connect the button between the GND and PIN 12
// Sending the 'r' command while pressing the button will give you another stream of data back
// than when the button is not pressed

int buttonPin = 10;
int LED = 13;

int GREEN_LED = 8;
int RED_LED = 9;

void setup() {
  Serial.begin(115200); // use the same baud-rate as the python side
  pinMode(buttonPin, INPUT_PULLUP); // Hooray! Free resistors!
  pinMode(LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
}

void printStuff(const char *text)
{
  char length[350]; // Screw buffer overflows!
  const char drama[350] =
      "import time\n"
      "print('Dramatic pause...')\n"
      "time.sleep(4)\n"
      "print('*Pausing intensifies...*')\n"
      "time.sleep(3)\n";
  sprintf(length, "%d\n", strlen(drama) + strlen(text)); // Screw error handling!
  Serial.print(length);
  Serial.print(drama);
  Serial.print(text);
}

void loop() {
  int buttonValue = digitalRead(buttonPin);
  if (buttonValue == LOW){
    // If button pushed, turn LED on
    digitalWrite(LED, HIGH);
    digitalWrite(GREEN_LED, HIGH);
    digitalWrite(RED_LED, LOW);
  } else {
    // Otherwise, turn the LED off
    digitalWrite(LED, LOW);
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(RED_LED, HIGH);
  }

  if(Serial.available() > 0) {
    char data = Serial.read();

    if (data == 'r') {
      if (buttonValue == LOW) {
        printStuff(
            "print('Okay, you won! Executing secret stuff!')\n"
            "for i in range(25):\n"
            "    print('\\x08' + '|/-\\\\|/-\\\\'[i % 8], end='\\r')\n"
            "    time.sleep(0.1)\n"
            "print('\\n<cake>  <======  here\\'s your reward! \\o/')\n"
        );
      } else {
        printStuff("raise ImportError('Get off my lawn and try harder!')");
      }
    }
  }
  delay(50);
}
