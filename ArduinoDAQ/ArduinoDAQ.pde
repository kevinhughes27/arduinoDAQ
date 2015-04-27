//// ArduinoDAQ
// Kevin Hughes 2012

//// Constants
int d = 1;

void setup() {

  // All pins to input
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);

  // Init Serial
  Serial.begin(115200);

}// end setup

void loop() {

  if(Serial.available()) {

    int signal = Serial.read();

    if(signal == 119) {

      Serial.println( analogRead(A0) );    delayMicroseconds(d);
      Serial.println( analogRead(A1) );    delayMicroseconds(d);
      Serial.println( analogRead(A2) );    delayMicroseconds(d);
      Serial.println( analogRead(A3) );    delayMicroseconds(d);
      Serial.println( analogRead(A4) );    delayMicroseconds(d);
      Serial.println( analogRead(A5) );    delayMicroseconds(d);


      // Testing
      /*
      Serial.println( "A0" );    delayMicroseconds(d);
      Serial.println( "A1" );    delayMicroseconds(d);
      Serial.println( "A2" );    delayMicroseconds(d);
      Serial.println( "A3" );    delayMicroseconds(d);
      Serial.println( "A4" );    delayMicroseconds(d);
      Serial.println( "A5" );    delayMicroseconds(d);
      */

    }//end if
  }// end if
}// end loop
