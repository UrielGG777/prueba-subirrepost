//1298d --- modulo
//--- 2 puentes h


//ENA ....... velocidad de giro
//IN1 ....... SENTIDO
//IN2 ....... 
//OUT 1
//OUT 2

//ENB
//IN3
//IN4
//OUT 3
//OUT 4
int ENA = 3;
int IN1 = 5;
int IN2 = 6;

//conectamos al motor
//out 1 y out 2 se conectan directamente al puente h al motor
void setup() {
  // put your setup code here, to run once:
  pinMode (in1, OUTPUT);
  pinMode (in2, OUTPUT);

  Serial.begin(9600);
  Serial.setTimeout(10);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.aviable()>0){
    int v = Serial.readString().toInt();
    if(v == 0){
      Serial.println("Detenerse");
      digitalWrite(in1, 0);
      digitalWrite(in2, 0);
      digitalWrite(ENA, 0)
    }
    else if (v == 1){
      Serial.println("Grirar Izquierda");
       Serial.println("Detenerse");
      digitalWrite(in1, 0);
      digitalWrite(in2, 1);
      digitalWrite(ENA, 255)
    }
    else if (v == 2){
      Serial.println("Grirar derecha");
       Serial.println("Detenerse");
      digitalWrite(in1, 1);
      digitalWrite(in2, 0);
      digitalWrite(ENA, 255)
    }
    else{
      Serial.println("Movimiento no valido");
    }
  }
  delay(100);
}
