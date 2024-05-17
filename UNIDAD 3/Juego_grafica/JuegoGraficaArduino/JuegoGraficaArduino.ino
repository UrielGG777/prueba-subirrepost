int ledsEnemySensor[] = {4, 5, 6};
int ledsEnemyTimer[] = {7, 8, 9};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  for(int i = 0; i<3; i++){
    pinMode(ledsEnemySensor[i], OUTPUT);
  }
  for(int i = 0; i<3; i++){
    pinMode(ledsEnemyTimer[i], OUTPUT);
  }
}

String mode = "";
int value = 0;
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    char temp[3];
    Serial.readString().toCharArray(temp, 3);
    mode = temp[0];
    value = int(temp[1]) - 48;
    if(mode == "T"){
      for(int i = 0; i<value; i++){
        digitalWrite(ledsEnemyTimer[i], 1);
      }
      for(int i = value; i<3; i++){
        digitalWrite(ledsEnemyTimer[i], 0);
      }
    }
    if(mode == "S"){
      for(int i = 0; i<3; i++){
        digitalWrite(ledsEnemySensor[i], 0);
      }
      digitalWrite(ledsEnemySensor[value], 1);
    }
  }
}
