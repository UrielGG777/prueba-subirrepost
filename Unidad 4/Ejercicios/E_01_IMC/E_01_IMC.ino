void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);

}
int estado = 0;
float masa;
float altura;
void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0){
    Serial.println("¿Cuanto pesas? (en Kg)");
    estado = estado + 1;
  }
  else if (estado == 1){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      masa = v;
      estado++;
    }
  }
  else if (estado == 2){
    Serial.println("¿Cuanto mides? (en metros)");
    estado++;
  }
  else if (estado == 3){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      altura = v;
      estado++;
    }
  }
  else if (estado == 4){
    float imc = masa / (altura * altura);
    Serial.println("Tu IMC es de: " + String(imc));
    estado++;
  }
  else if (estado == 5){
    Serial.println("¿Deses calcular con otros valores? [0]Si  [1]No");
    estado++;
  }
  else if (estado == 6){
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
