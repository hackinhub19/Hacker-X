#include <SoftwareSerial.h>

SoftwareSerial BT(0, 1); //TX, RX respetively
String readvoice;

void setup() {
 BT.begin(9600);
 Serial.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9,INPUT);

}
long duration, distance;
//-----------------------------------------------------------------------// 
void loop() {
     while (BT.available()){  //Check if there is an available byte to read
  delay(10); //Delay added to make thing stable
  char c = BT.read(); //Conduct a serial read
  readvoice += c; //build the string- "forward", "reverse", "left" and "right"
  } 
    
     {
      digitalWrite(8, LOW);
    delayMicroseconds(2);
    digitalWrite(8,HIGH);
    delayMicroseconds(10);
    digitalWrite(8,LOW);
    duration = pulseIn(9, HIGH);
    distance= duration/58.2;
     }
   if(distance<5)
   {
    digitalWrite (3, LOW);
   digitalWrite (4, LOW);
   digitalWrite (5, LOW);
   digitalWrite (6, LOW);
   delay (100);
    }
    else
    {
      if (readvoice.length() > 0) {
    Serial.println(readvoice);
    
  if(readvoice == "*forward#")
  {
    digitalWrite(3, HIGH);
    digitalWrite (4, HIGH);
    digitalWrite(5,LOW);
    digitalWrite(6,LOW);
    delay(100);
  }

  
  else if (readvoice == "*right#")
  {
    digitalWrite (3,HIGH);
    digitalWrite (4,LOW);
    digitalWrite (5,LOW);
    digitalWrite (6,LOW);
     digitalWrite(10,LOW);
   delay (3400);
      digitalWrite(3, HIGH);
    digitalWrite (4, HIGH);
    digitalWrite(5,LOW);
    digitalWrite(6,LOW);
     digitalWrite(10,LOW);
    delay(100);
  
 }

 else if ( readvoice == "*left#")
 {
   digitalWrite (3, LOW);
   digitalWrite (4, HIGH);
   digitalWrite (5, LOW);
   digitalWrite (6, LOW);
    digitalWrite(10,LOW);
   delay (3400);
      digitalWrite(3, HIGH);
    digitalWrite (4, HIGH);
    digitalWrite(5,LOW);
    digitalWrite(6,LOW);
     digitalWrite(10,LOW);
    delay(100);
 }
      
 
