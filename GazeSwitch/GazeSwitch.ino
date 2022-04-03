
#include <M5StickC.h>

void setup() {
  // put your setup code here, to run once:
  M5.begin();
  M5.Lcd.setTextFont(1);
  M5.Lcd.setCursor(0, 0, 2); 
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  M5.update();
  if(Serial.read() != -1){
    M5.Lcd.println(Serial.read());
  }
  if ( M5.BtnA.wasPressed() ) {
    M5.Lcd.fillScreen(BLACK);
    //Serial.println("BtnA.wasPressed() == TRUE");
    M5.Lcd.println("wasPressed");
    Serial.write("P");
  }

  
}
