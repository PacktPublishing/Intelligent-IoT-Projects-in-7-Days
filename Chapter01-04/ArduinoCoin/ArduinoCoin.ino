// Hx711.DOUT - pin #A2
// Hx711.SCK - pin #A3

#include <Hx711.h>
Hx711 scale(A2, A3);

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print("Coin: ");
  Serial.print(scale.getGram(), 1);
  Serial.println(" g");
  delay(500);
}
