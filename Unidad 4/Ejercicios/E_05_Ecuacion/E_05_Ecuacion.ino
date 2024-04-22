void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);

}
int estado = 0;
float m;
float x;
float b;
void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0){
    Serial.println("Valor de m");
    estado = estado + 1;
  }
  else if (estado == 1){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      m = v;
      estado++;
    }
  }
  else if (estado == 2){
    Serial.println("Valor de x");
    estado = estado + 1;
  }
  else if (estado == 3){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      x = v;
      estado++;
    }
  }
  else if (estado == 4){
    Serial.println("Valor de b");
    estado = estado + 1;
  }
  else if (estado == 5){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      b = v;
      estado++;
    }
  }
  else if (estado == 6){
    float y = m * x + b;
    Serial.println("y = mx + b = " + String(y));
    estado++;
  }
  else if (estado == 7){
    Serial.println("¿Deses calcular con otros valores? [0]Si  [1]No");
    estado++;
  }
  else if (estado == 8){
    if (Serial.available() > 0){
      int v = Serial.readString().toInt();
      if (v == 0){
        estado = 0;
      } else {
        estado++;
      }
    }
  }
  delay(100);
}
