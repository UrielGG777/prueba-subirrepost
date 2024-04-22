void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);

}
int estado = 0;
float v1;
float v2;
float v3;
float v4;
float v5;
void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0){
    Serial.println("Primer valor");
    estado = estado + 1;
  }
  else if (estado == 1){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      v1 = v;
      estado++;
    }
  }
  else if (estado == 2){
    Serial.println("Segundo valor");
    estado = estado + 1;
  }
  else if (estado == 3){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      v2 = v;
      estado++;
    }
  }
  else if (estado == 4){
    Serial.println("Tercer valor");
    estado = estado + 1;
  }
  else if (estado == 5){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      v3 = v;
      estado++;
    }
  }
  else if (estado == 6){
    Serial.println("Cuarto valor");
    estado = estado + 1;
  }
  else if (estado == 7){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      v4 = v;
      estado++;
    }
  }
  else if (estado == 8){
  Serial.println("Quinto valor");
    estado = estado + 1;
  }
  else if (estado == 9){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      v5 = v;
      estado++;
    }
  }
  else if (estado == 10){
    float promedio = (v1 + v2 + v3 + v4 + v5) / 5;
    Serial.println("Promedio: " + String(promedio));
    estado++;
  }
  else if (estado == 11){
    Serial.println("¿Deses calcular con otros valores? [0]Si  [1]No");
    estado++;
  }
  else if (estado == 12){
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
