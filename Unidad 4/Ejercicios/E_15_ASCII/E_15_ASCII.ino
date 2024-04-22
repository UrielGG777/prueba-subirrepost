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

// Acuerdate de cambiar de "New Line" a "No Line Ending" en el monitor serial
char character = "A";
void loop() {
  if(Serial.available() > 0){
    character = Serial.read();
    Serial.println(character);
    for (int bit = 7; bit >= 0; bit--){
      Serial.print(bitRead(character, bit));
      digitalWrite(leds[bit], bitRead(character, bit));
    }
    Serial.println();
  }
  delay(1000);
}