const int pinoBuz = 11;
const int pinoLed = 8;
const int pinoTri = 2;
const int pinoEcho =3;
float TempoEcho = 0;
const float VelocidadeSom_mpors = 340; 
const float VelocidadeSom_mporus = 0.000340; 
int tempo = 400;
float dist = 0;

void setup() {
  pinMode(pinoTri, OUTPUT);
  digitalWrite(pinoTri, LOW);
  pinMode(pinoEcho, INPUT); 
  pinMode(pinoBuz,OUTPUT);
  Serial.begin(9600);
  delay(100);
}

void loop() {

  DisparaPulsoUltrassonico();
  TempoEcho = pulseIn(pinoEcho, HIGH);
  dist = CalculaDistancia(TempoEcho*100);
  Serial.print("Distancia em centimetros: ");
  Serial.println(dist);
  if(dist<10){
    tone(pinoBuz,528,tempo);
    digitalWrite(pinoLed,HIGH);
  }
digitalWrite(pinoLed,LOW);

}

void DisparaPulsoUltrassonico(){
  digitalWrite(pinoTri, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinoTri, LOW);
  }

float CalculaDistancia(float tempo_us){
  return((tempo_us*VelocidadeSom_mporus)/2);
}