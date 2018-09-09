void setup() {
  Serial.begin(115200); // use the same baud-rate as the python side
}

void printStuff(const char *text)
{
  char length[100]; // Screw buffer overflows!
  sprintf(length, "%d\n", strlen(text)); // Screw error handling!
  Serial.print(length);
  Serial.print(text);
}

void loop() {
  if(Serial.available() > 0) {
    char data = Serial.read();

    if (data == 'r') {
      printStuff("raise ImportError(\"Try harder!\")");
    }
  }
  delay(100);
}
