#include <IRremote.h>
int RECV_pin = 4;
IRrecv irrecv(RECV_pin);
decode_results results;
void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();
}
void loop() {
  if (irrecv.decode())
  { 
    irrecv.resume();
    Serial.println(irrecv.results.value,HEX);
    }
  delay(100);
  }
