int potPin=0;
int ledPin=2;

void setup() {
  pinMode(ledPin,OUTPUT);

}

void loop() {
  int pot = analogRead(potPin);
  if (pot>511)
   digitalWrite(ledPin, HIGH);
   delay(pot);
   digitalWrite(ledPin, LOW);
   delay(pot);
  

}
