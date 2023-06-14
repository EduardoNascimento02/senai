#include <LiquidCrystal.h>
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
const int pinoTri = 8;
const int pinoEcho =9;
float TempoEcho = 0;
const float VelocidadeSom_mpors = 340; 
const float VelocidadeSom_mporus = 0.000340; 
float dist = 0;
const String msg = "Afaste-se";
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
const String msg2 = "Nao aproximar";

void setup() {
  pinMode(pinoTri, OUTPUT);
  digitalWrite(pinoTri, LOW);
  pinMode(pinoEcho, INPUT); 
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {
  DisparaPulsoUltrassonico();
  TempoEcho = pulseIn(pinoEcho, HIGH);
  dist = CalculaDistancia(TempoEcho*100);
  Serial.print("Distancia em centimetros: ");
  Serial.println(dist);
  if(dist<30){
    lcd.print(msg);
    delay(500);
    lcd.clear();
  } 
  else{
    lcd.print(msg2);
    delay(500);
    lcd.clear();
  }
}

void DisparaPulsoUltrassonico(){
  digitalWrite(pinoTri, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinoTri, LOW);
  }

float CalculaDistancia(float tempo_us){
  return((tempo_us*VelocidadeSom_mporus)/2);
}