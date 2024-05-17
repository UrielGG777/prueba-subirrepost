 #include "Servo.h"  
 int pinServo = 9;
 int PIR = 4;
 Servo servo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  servo.attach(pinServo);
  pinMode(PIR, INPUT_PULLUP);

}
int Val;
void loop() {
  // put your main code here, to run repeatedly:
  Val = digitalRead(PIR);
  if(Val > 100){
    servo.write(Val);
    Serial.println("Movimiento");
    delay(4000);
  }
 delay(1000);
}
