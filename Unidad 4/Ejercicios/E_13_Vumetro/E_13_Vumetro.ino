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

int power = 0;
void loop() {
  if (Serial.available() > 0){
    int x = Serial.readString().toInt();
    if (x > 8){
      power = 8;
    } else if (x < 0){
      power = 0;
    } else {
      power = x;
    }
    for (int i = 0; i < power; i++){
      digitalWrite(leds[i], HIGH);
    }
    for (int i = power; i < 8; i++){
      digitalWrite(leds[i], LOW);
    }
  }
}