#include <LobotServoController.h>

LobotServoController servo_controller;
LobotServo servos[17]; 
bool update=false;
void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(9600);
  while(!Serial);
  digitalWrite(13,HIGH);
  
  uint8_t servo_id;
  uint16_t servo_pos=1500;
  for (servo_id=0;servo_id<17;servo_id++)
  {
    servos[servo_id].ID=servo_id;
    servos[servo_id].Position=servo_pos;
  }

  
  servo_controller.moveServos(servos,17,100);
  

}

void loop() {
  String val="";
  int comma=-1,underline=-1;
  while (Serial.available())
  {
    val=Serial.readStringUntil('|');
    //Serial.println(val);
    comma=val.indexOf(',');
    String left_string=val;
    while (comma !=-1)
    {
      String command=left_string.substring(0,comma);
      underline = command.indexOf('_');
      if (underline!=-1)
      {
        uint8_t servo_id=command.substring(0,underline).toInt();
        uint16_t servo_pos=command.substring(underline+1).toInt();
        if (servo_id >=0 & servo_id<17 & servo_pos >=500 and servo_pos<=2500)
        {
          servos[servo_id].Position=servo_pos;
          //Serial.println(command);
          update=true;
        }
      }
      left_string=left_string.substring(comma+1,left_string.length());
      comma=left_string.indexOf(',');
    }
  }
  
  if (update)
  {
    servo_controller.moveServos(servos,17,100);
    update=false;
    digitalWrite(13, HIGH-digitalRead(13)); 
  }

}
