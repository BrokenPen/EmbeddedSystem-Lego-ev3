#define BAUDRATE 9600

void setup() {
  // start serial port at 9600 bps and wait for port to open:
  Serial.begin(BAUDRATE);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  establishContact();
}

void loop() {
   
  String inString = "";         // incoming string

  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming string:
    inString = Serial.readString();
    inString.toUpperCase();
    // return incoming string in uppercase
    Serial.println(inString);
  }
}

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println(".");   // send an initial string
    delay(300);
  }
}


