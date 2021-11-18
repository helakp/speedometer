
unsigned long startMillis;
unsigned long currentMillis;
const unsigned period=1;
int magnetSense = 0;
int lastState = 1;

int sensPin=2;
int counter = 0;

float vecichleSpeed;
float radius=0.2;
float pi=3.14;
float circumference = 2*pi*radius;

void setup() {
  Serial.begin(115200);
  startMillis = millis();
  pinMode(sensPin, INPUT);

}

void loop() {
  currentMillis=millis();
  magnetSense = digitalRead(sensPin);
  if(magnetSense==0 && lastState==1){
    lastState=0;
    if(currentMillis-startMillis>=period && lastState==0){
      vecichleSpeed = circumference/(currentMillis-startMillis)*1000;
      startMillis = currentMillis;
      counter++;
      Serial.println(String(vecichleSpeed)+"m/s");}}
  else{
    if(currentMillis-startMillis>=period && lastState==0){
      startMillis = currentMillis;
      lastState = 1;}}
}
