#include <LiquidCrystal.h> //Incluindo a biblioteca para o lcd
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2; //Definindo os pinos para a placa
const String msg = " Porta 1 aberta"; //Lembre-se que o numero de caracteres em uma linha será de no maximo 16, por conta do tamanho do lcd

LiquidCrystal lcd(rs, en, d4, d5, d6, d7); //Criando um objeto com nome lcd

void setup() {
  // configurando a tela do lcd para 16 x 2
  lcd.begin(16, 2);
}

void loop() {
  lcd.print(msg); //Imprime o que está na variavel msg na tela
  delay(750);
  lcd.clear(); //Apaga qualquer coisa que está na tela
  delay(750);  
}