#include "esphome.h"
using namespace esphome;

// This is all just for testing out ultrasonic sensor hardware

// const int TRIG_PIN = 5; // D1
// const int ECHO_PIN = 4; // D2

const int TRIG_PIN = 12; // D6
const int ECHO_PIN = 13; // D7

class CustomUltrasonic : public PollingComponent, public Sensor {
 public:
  CustomUltrasonic() : PollingComponent(1000) {}

  float get_setup_priority() const override { return setup_priority::DATA; }

  void setup() override {
    pinMode(TRIG_PIN, OUTPUT);
    digitalWrite(TRIG_PIN, LOW);
    pinMode(ECHO_PIN, INPUT);
    randomSeed(analogRead(0));
  }

  void update() override {
    float trigger_width;
    // trigger_width = random(0, 20000) / 10.0;
    trigger_width = 15;

    // ESP_LOGD("ultrasonic", "START");
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(5);
    // ESP_LOGD("ultrasonic", "Before trig, echo %u", digitalRead(ECHO_PIN));
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(trigger_width);
    digitalWrite(TRIG_PIN, LOW);
    // ESP_LOGD("ultrasonic", "After trig, echo is %u", digitalRead(ECHO_PIN));
    

    unsigned long pulse_width;
    pinMode(ECHO_PIN, INPUT);
    pulse_width = pulseIn(ECHO_PIN, HIGH, 1000000);
    ESP_LOGD("ultrasonic", "%fµs --> %uµs = %fcm", trigger_width, pulse_width, pulse_width / 2.0 / 29.1);

    // always 135676 µs

    // pinMode(ECHO_PIN, INPUT);
    // pulseInManual2();

    // listen();
    // publish_state(time / 2.0 / 29.1);
  }

  void listen() {
    unsigned long t;
    unsigned long v = 0;
    t = micros();
    while ( micros() - t < 1000000 ) {
      if (digitalRead(ECHO_PIN) != v) {
        ESP_LOGD("ultrasonic", "%u for %u µs", v, micros() - t);
        if (v == 0) { v = 1; } else { v = 0; }
      }
    };
    ESP_LOGD("ultrasonic", "END");
  }

  unsigned long pulseInManual() {
    unsigned long w1;
    unsigned long w2;

    unsigned long t1;
    unsigned long t2;

    unsigned long waited;
    unsigned long pulse_width;

    // Wait for pulse on echo pin
    w1 = micros();
    while ( digitalRead(ECHO_PIN) == 0 );
    w2 = micros();
    
    // Measure how long the echo pin was held high (pulse width)
    // Note: the micros() counter will overflow after ~70 min
    t1 = micros();
    while ( digitalRead(ECHO_PIN) == 1);
    t2 = micros();

    waited = w2 - w1;
    pulse_width = t2 - t1;

    ESP_LOGD("ultrasonic", "%u / %u µs", waited, pulse_width);

    return pulse_width;
  }

  void pulseInManual2() {
    unsigned long s;
    unsigned long e;
    s = micros();
    while ( digitalRead(ECHO_PIN) == 0 ) {
      s = micros();
    };
    e = micros();
    while ( digitalRead(ECHO_PIN) == 1) {
      e = micros();
    };
    ESP_LOGD("ultrasonic", "%u - %u = %u µs", s, e, e - s);
  }  
};
