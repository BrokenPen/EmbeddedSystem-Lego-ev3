#define BAUDRATE 9600

void setup() {
  // start serial port at 9600 bps and wait for port to open:
  Serial.begin(BAUDRATE);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  // establishContact();
}

// initial global variable
int temp = 0; // temperate variable
int humi = 0; // humidity varaiable

void loop() {
   
  String inString = "";         // incoming string

  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming string:
    inString = Serial.readString();
    // convert incoming string into lower case
    inString.toLowerCase();
    // return incoming string in uppercase
    Serial.println(inString);
    if (inString == "temp") {
      // generate a random number as temperatue value
      temp = random(20, 30);
      Serial.println(temp);
    } else if (inString == "humi") {
      // generate a random number as humidty value
      humi = random(30, 70);b
      Serial.println(humi);
    } else {
      // Serial.println("unknow require");
    }
  }
}

// wait for the serial connected device are already to comunicate
void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println(".");   // send an initial string
    delay(300);
  }
}


