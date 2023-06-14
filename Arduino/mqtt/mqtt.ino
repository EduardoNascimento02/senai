#include <SPI.h> // módulo de rede
#include <UIPEthernet.h> // módulo de rede
#include <PubSubClient.h> // mqtt

const int trigPin = 7;
const int echoPin = 6;

// Configurações do Ethernet
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x11 };  // Endereço MAC do Arduino
IPAddress ip(172, 16, 32, 111);                      // Endereço IP do Arduino
IPAddress server(172, 16, 32, 206);                   // Endereço IP do servidor MQTT

// Configurações do MQTT
const char* topic = "mesa1distancia1";  // Tópico MQTT para envio dos dados MUDAR PARA O SEU TOPICO EX mesa1distancia1, mesa1distancia2
				    // Ex: mesa2distancia1, mesa2distancia2
const char* clientID = "arduino";   // ID do cliente MQTT

EthernetClient ethClient;
PubSubClient client(ethClient);

void setup() {
  Ethernet.begin(mac, ip);
  delay(1500);  // Aguarda a conexão Ethernet

  Serial.begin(9600);
  pinMode(trigPin, OUTPUT); // sensor de movimento
  pinMode(echoPin, INPUT); // sensor de movimento
  
  client.setServer(server, 1883);
    
  Serial.begin(9600);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }

  client.loop();

  long duration, cm;

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  cm = microsecondsToCentimeters(duration);

  if (isnan(cm)) {
    Serial.println("Erro ao ler a distancia do sensor!");
    return;
  }
  
  char cmStr[4];
  dtostrf(cm, 6, 1, cmStr);  // Converte o valor float para uma string
  
  Serial.println(cmStr);
  client.publish(topic, cmStr);  // Publica a temperatura no tópico MQTT
  
  delay(5000);  // Aguarda 5 segundos antes de enviar a próxima leitura
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Conectando ao servidor MQTT...");
    
    if (client.connect(clientID)) {
      Serial.println("conectado!");
    } else {
      Serial.print(" falhou, código do erro: ");
      Serial.print(client.state());
      Serial.println(" Tentando novamente em 5 segundos...");
      
      delay(10000);  // Aguarda 5 segundos antes de tentar a conexão novamente
    }
  }
}

long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}