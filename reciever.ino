#include <VirtualWire.h>

#define PWMA 13
#define PWMB 7
#define AIN1 11
#define AIN2 12
#define BIN1 9
#define BIN2 8
#define STBY 10


int err,b;
int i=1;

void motor(void);
void forward(void);
void back(void);
void left(void);
void right(void);



byte message[VW_MAX_MESSAGE_LEN]; // Буфер для хранения принимаемых данных
byte messageLength = VW_MAX_MESSAGE_LEN; // Размер сообщения

const int led_pin = 13; // Пин светодиода
const int receiver_pin = 15; // Пин подключения приемника
void setup()
{
    vw_set_rx_pin(receiver_pin); // Пин подключения приемника
    vw_setup(2000); // Скорость передачи данных (бит в секунду)
    vw_rx_start(); // Активация применика
    pinMode(PWMA, OUTPUT);
    pinMode(PWMB, OUTPUT);
    pinMode(AIN1, OUTPUT);
    pinMode(AIN2, OUTPUT);
    pinMode(BIN1, OUTPUT);
    pinMode(BIN2, OUTPUT);
    pinMode(STBY, OUTPUT);
    digitalWrite(STBY, HIGH);

    Serial.begin(9600); // Скорость передачиданных

}
void loop()
{
if (vw_get_message(message, &messageLength)) // Если есть данные..
{
digitalWrite(led_pin, HIGH); // Зажигаем светодиод в начале приема пакета
Serial.write(message[0]);
if (message[0]=='g'){
  err=0;
  }
else if(message[0]=='a'){
  err=3;}
else if(message[0]=='s'){
err=4;}
else if(message[0]=='d'){
err=1;}
else if(message[0]=='q'){
err=2;}
Serial.println(err);
digitalWrite(led_pin, LOW); // Гасим светодиод в конце
}
motor();
}

void forward(){
    digitalWrite(8,LOW);
    digitalWrite(9,HIGH);
    digitalWrite(11,LOW);
    digitalWrite(12,HIGH);
    Serial.println("forrrr");
    return 0;
  }
void left(){
    digitalWrite(8,LOW);
    digitalWrite(9,HIGH);
    digitalWrite(12,LOW);
    digitalWrite(11,HIGH);
    return 0;
  }

void right(){
      digitalWrite(9,LOW);
    digitalWrite(8,HIGH);
    digitalWrite(11,LOW);
    digitalWrite(12,HIGH);
    return 0;

  }
void back(){
    digitalWrite(9,HIGH);
    digitalWrite(8,LOW);
    digitalWrite(12,LOW);
    digitalWrite(11,HIGH);
    return 0;

  }


void motor()
{
  if(err==0){
    analogWrite(13,75);
    analogWrite(7,75);
    forward();
    Serial.println("for");
    return 0;
    }
   else if(err==1){
    analogWrite(13,55);
    analogWrite(7,15);
    forward();
    return 0;
    }
   else if(err==3){
    analogWrite(13,15);
    analogWrite(7,55);
    forward();
    return 0;
    }
   else if(err==2){
    analogWrite(13,100);
    analogWrite(7,10);
    forward();
    return 0;
    }
    else if(err==4){
    analogWrite(13,10);
    analogWrite(7,100);
    back();
    return 0;
    }
    else if(err==5){
    analogWrite(13,20);
    analogWrite(7,20);
    forward();
    return 0;
    }
return 0;
}
