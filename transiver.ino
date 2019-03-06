#include <VirtualWire.h>

const int led_pin = 13; // Пин светодиода
const int transmit_pin = 12; // Пин подключения передатчика

char incomingchar;

void setup() {
       Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
      vw_set_tx_pin(transmit_pin);
      vw_setup(2000);       // Скорость передачи (Бит в секунду)
      pinMode(led_pin, OUTPUT);
}

void loop() {
       if (Serial.available()) {
               incomingchar = Serial.read();
                  if (incomingchar=='g'){
                   const char *msg = "g"; // Передаваемое сообщение
                   digitalWrite(led_pin, HIGH); // Зажигаем светодиод в начале передачи
                   vw_send((uint8_t *)msg, strlen(msg)); // Отправка сообщения
                   vw_wait_tx(); // Ожидаем окончания отправки сообщения
                   digitalWrite(led_pin, LOW); // Гасим светодиод в конце передачи
                   delay(1);} // Пауза 1 секунда

                  else if (incomingchar=='d'){
                   const char *msg ="d"; // Передаваемое сообщение
                   digitalWrite(led_pin, HIGH); // Зажигаем светодиод в начале передачи
                   vw_send((uint8_t *)msg, strlen(msg)); // Отправка сообщения
                   vw_wait_tx(); // Ожидаем окончания отправки сообщения
                   digitalWrite(led_pin, LOW); // Гасим светодиод в конце передачи
                   delay(1);} // Пауза 1 секунда

                  else if (incomingchar=='q'){
                   const char *msg = "q"; // Передаваемое сообщение
                   digitalWrite(led_pin, HIGH); // Зажигаем светодиод в начале передачи
                   vw_send((uint8_t *)msg, strlen(msg)); // Отправка сообщения
                   vw_wait_tx(); // Ожидаем окончания отправки сообщения
                   digitalWrite(led_pin, LOW); // Гасим светодиод в конце передачи
                   delay(1);} // Пауза 1 секунда

                  else if (incomingchar=='a'){
                   const char *msg = "a"; // Передаваемое сообщение
                   digitalWrite(led_pin, HIGH); // Зажигаем светодиод в начале передачи
                   vw_send((uint8_t *)msg, strlen(msg)); // Отправка сообщения
                   vw_wait_tx(); // Ожидаем окончания отправки сообщения
                   digitalWrite(led_pin, LOW); // Гасим светодиод в конце передачи
                   delay(1);} // Пауза 1 секунда

                  else if (incomingchar=='s'){
                   const char *msg = "s"; // Передаваемое сообщение
                   digitalWrite(led_pin, HIGH); // Зажигаем светодиод в начале передачи
                   vw_send((uint8_t *)msg, strlen(msg)); // Отправка сообщения
                   vw_wait_tx(); // Ожидаем окончания отправки сообщения
                   digitalWrite(led_pin, LOW); // Гасим светодиод в конце передачи
                   delay(1);} // Пауза 1 секунда
                 else{
                 Serial.println(incomingchar);
       }
}
}