void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);

}
int estado = 0;
int n;
void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0){
    Serial.println("Ingresa un numero");
    estado = estado + 1;
  }
  else if (estado == 1){
    if (Serial.available() > 0){
      int v = Serial.readString().toInt();
      n = v;
      estado++;
    }
  }
  else if (estado == 2){
    String primo = "Si";
    for (int i = 2; i <= n/2; i++){
      if (n%i == 0){
        primo = "No";
        break;
      }
    }
    Serial.println("¿El numero es primo? " + String(primo));
    estado++;
  }
  else if (estado == 3){
    Serial.println("¿Deses calcular con otros valores? [0]Si  [1]No");
    estado++;
  }
  else if (estado == 4){
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
