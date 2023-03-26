#include <Servo.h>
#include <math.h>
Servo servoX;  // 9
Servo servoY; //6

//desired postion X ,Y
float x=0.9;//9
float y=7.36; //6

float r1=0.0;
float phi1=0.0;
float phi2=0.0;
float phi3=0.0;
float a2=4.8;
float a4=3.5;
//desired angles for inverse kinematics
float T1=0.0;// theata t1 in radian
float T2=0.0;// theata t2 in radian
float THETA1;
float THETA2;
float actual1;
float actual2;
float m=1.2858; // limit the move of servo motor 90 degree= 70degree in out case
float n=0.9;

void setup() {
  servoX.attach(10);  // attaches the servo on pin 9 to the servo object
  servoY.attach(6);
  Serial.begin(9600);
  

}

void loop() {
  if (x==0){
    x==0.1;
  }
  else if (y==0){
    y==0.1;
  }
    // invrse kinematics part
   r1=sqrt(x*x+y*y);
  //motor1
  float ww = (((a4 * a4) - (a2 * a2) - (r1 * r1))/(-2.0 * a2 * r1));
  phi1=acos(ww);
  phi2=atan(y/x);
  T1=phi2-phi1;
  //motor2
  float mm = (((r1 * r1) - (a2 * a2) - (a4 * a4))/(-2.0 * a2 * a4));
  phi3=acos(mm);
  T2=3.14159-phi3;
  
  THETA1=(((T1/3.1459)*180.0));
  THETA2=(((T2/3.1459)*180.0));
   

  
Serial.println("T1 actual");
Serial.println(actual1);
Serial.println("\n T2 actual");
Serial.println(actual2);
 //optimizing location
   actual1=(THETA1/m);
   actual2=(THETA2/n);
 

  
  servoX.write(actual1); //THEATA 1
  servoY.write(actual2);
  delay(1000);
    
    
}
