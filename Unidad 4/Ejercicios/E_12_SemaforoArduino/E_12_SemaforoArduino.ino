int leds[] = {4, 5, 6};
int ledState[] = {false, false, false};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(15);
  for(int led = 0; led < 8; led++){
    pinMode(leds[led], OUTPUT);
  }
}

int current = 0;
void loop() {
  digitalWrite(leds[current], LOW);
  if(current == 2){
    current = 0;
  } else {
    current++;
  }
  digitalWrite(leds[current], HIGH);
  delay(1000);
}