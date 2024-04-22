int leds[] = {4, 5, 6, 7, 8, 9, 10, 11};
int ledState[] = {false, false, false, false, false, false, false, false};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(15);
  for(int led = 0; led < 8; led++){
    pinMode(leds[led], OUTPUT);
  }
}

byte number = 0;
void loop() {
  for (int bit = 7; bit >= 0; bit--){
    Serial.print(bitRead(number, bit));
    digitalWrite(leds[bit], bitRead(number, bit));
  }
  number++;
  delay(250);
}