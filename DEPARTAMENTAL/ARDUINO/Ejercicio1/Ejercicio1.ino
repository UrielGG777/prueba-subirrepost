int LDR = A0;
int LED = 7;

void setup(){
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(LED, OUTPUT);
}

int valor;
void loop(){
  valor = analogRead(LDR);
  if(valor > 600){
    digitalWrite(LED, 1);
    Serial.println("Apagados");
  }else {
    digitalWrite(LED, 0);
    Serial.println("Encendidos");
  }
  delay(200);
}