#define BAUDRATE 9600

// initial global variable
int temp = 0; // temperate variable
int humi = 0; // humidity varaiable

void setup() {
  // start serial port at 9600 bps and wait for port to open:
  Serial.begin(BAUDRATE);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  // establishContact();
}

void loop() {
   
  String inString = "";         // incoming string
  // gnerate random humidity value
  humi = random(30, 70);
  // generate random temperatur value
  temp = random(20, 30);
  Serial.println(String(temp) + "," + String(humi));
  // delay 5 seconds
  delay(5000);
}

// wait for the serial connected device are already to comunicate
void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println(".");   // send an initial string
    delay(300);
  }
}


