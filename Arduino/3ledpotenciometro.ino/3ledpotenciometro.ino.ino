const int pinoVerde = 2;
const int pinoAmarelo = 3;
const int pinoVermelho = 4;
const int pinoPot = A0;
float valorPot = 0;


void setup() {
  pinMode(pinoVerde,OUTPUT);
  pinMode(pinoAmarelo,OUTPUT);
  pinMode(pinoVermelho,OUTPUT);
}

void loop() {
  valorPot = map(analogRead(pinoPot),0,1023,0,1023);
  if(valorPot >= 0 && valorPot <=256){
    digitalWrite(pinoVerde,HIGH);
    digitalWrite(pinoAmarelo,LOW);
    digitalWrite(pinoVermelho,LOW);
  }
  if(valorPot>256 && valorPot <=550){
    digitalWrite(pinoVerde,LOW);
    digitalWrite(pinoAmarelo,HIGH);
    digitalWrite(pinoVermelho,LOW);    
  }
  if(valorPot>512 && valorPot<=1023){
    digitalWrite(pinoVerde,LOW);
    digitalWrite(pinoAmarelo,LOW);
    digitalWrite(pinoVermelho,HIGH);     
  }
}
