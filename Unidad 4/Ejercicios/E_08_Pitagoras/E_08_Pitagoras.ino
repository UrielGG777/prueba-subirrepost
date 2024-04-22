void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);

}
int estado = 0;
float catetoA;
float catetoB;
void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0){
    Serial.println("Valor del primer cateto");
    estado = estado + 1;
  }
  else if (estado == 1){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      catetoA = v;
      estado++;
    }
  }
  else if (estado == 2){
    Serial.println("Valor del segundo cateto");
    estado = estado + 1;
  }
  else if (estado == 3){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      catetoB = v;
      estado++;
    }
  }
  else if (estado == 4){
    float hipo = sqrt(sq(catetoA) + sq(catetoB));
    Serial.println("Hipotenusa = " + String(hipo));
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
