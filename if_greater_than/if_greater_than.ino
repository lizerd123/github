int potPin=0;
int ledPin=2;

void setup() {
  pinMode(ledPin,OUTPUT);

}

void loop() {
  int potman = analogRead(potPin);
  if (potman>511)
   digitalWrite(ledPin, HIGH);
   delay(potman);
   digitalWrite(ledPin, LOW);
   delay(potman);
  

}
