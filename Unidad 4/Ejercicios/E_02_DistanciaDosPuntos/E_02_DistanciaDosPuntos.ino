void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);

}
int estado = 0;
float x1;
float y1;
float x2;
float y2;
void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0){
    Serial.println("Coordenada X del primer punto");
    estado = estado + 1;
  }
  else if (estado == 1){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      x1 = v;
      estado++;
    }
  }
  else if (estado == 2){
    Serial.println("Coordenada Y del primer punto");
    estado++;
  }
  else if (estado == 3){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      y1 = v;
      estado++;
    }
  }
  else if (estado == 4){
    Serial.println("Coordenada X del segundo punto");
    estado++;
  }
  else if (estado == 5){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      x2 = v;
      estado++;
    }
  }
  else if (estado == 6){
    Serial.println("Coordenada Y del segundo punto");
    estado++;
  }
  else if (estado == 7){
    if (Serial.available() > 0){
      float v = Serial.readString().toFloat();
      y2 = v;
      estado++;
    }
  }
  else if (estado == 8){
    float distancia = sqrt(sq(x2 - x1) + sq(y2 - y1));
    Serial.println("La distancia es: " + String(distancia));
    estado++;
  }
  else if (estado == 9){
    Serial.println("¿Deses calcular con otros valores? [0]Si  [1]No");
    estado++;
  }
  else if (estado == 10){
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
