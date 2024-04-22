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

int current = 0;
int pattern[] = {0, 0, 0, 0, 0};
void loop() {
  if(Serial.available() > 0){
    String patternRaw = Serial.readString();
    int size = patternRaw.length();
    char carray[size+1];
    patternRaw.toCharArray(carray, sizeof(carray));
    for (int i = 0; i < 8; i++){
      pattern[i] = 0;
    }
    for (int i = 0; i < size; i++){
      pattern[i] = String(carray[i]).toInt();
    }
    for (int i = 0; i < 8; i++){
      digitalWrite(leds[i], LOW);
    }
    Serial.print("Patron: ");
    for(int i = 0; i < 5; i++){
      Serial.print(String(pattern[i]));
    }
    Serial.println();
    current = 0;
  }
  digitalWrite(leds[pattern[current]-1], LOW);
  if (current == 5){
    current = 0;
  } else {
    current++;
  }
  Serial.println(String(pattern[current]));
  digitalWrite(leds[pattern[current]-1], HIGH);
  delay(1000);
}