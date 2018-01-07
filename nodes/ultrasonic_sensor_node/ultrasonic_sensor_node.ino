#include "RFM69_DSH.h"

RFM69_DSH dsh_radio;

// Define pin numbers
const int trigPin = 3;
const int echoPin = 9;
// Constants for distance sensor
long duration;
int distance;
int safetyDistance;

const uint8_t node_id = 9;
const uint8_t network_id = 0;

//var for time
long previous_time = 0;

enum request_types {
  ALL,
  DIST,
  BAD_REQUEST,
  NONE
};

request_types current_request = NONE;

void setup()
{
	pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600);

	dsh_radio.initialize(RF69_915MHZ, node_id, network_id);
	dsh_radio.setHighPower(true);

}

void loop()
{

  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration*0.034/2;
  // Prints the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.println(distance);

	if (dsh_radio.receiveDone()) {

		Serial.println("Transmission Received");
    
    if (dsh_radio.requestReceived()) {
      if (dsh_radio.requestAllReceived())
        current_request = ALL;
      else if (dsh_radio.getReceivedStr() == "DIST")
        current_request = DIST;
      else
        current_request = BAD_REQUEST;
    }
    
		if (dsh_radio.ACKRequested()) {
			dsh_radio.sendACK();
			Serial.println("ACK sent");
		}
   
	}
 
  switch(current_request) {
    case NONE:
      break;

    case BAD_REQUEST:
      dsh_radio.sendError("BAD REQUEST");
      current_request = NONE;
      break;
    
    case ALL:
      Serial.println("Sending all sensor Data");
      if (!dsh_radio.sendSensorReading("DIST", distance)) {
        dsh_radio.sendError("DIST SEND");
        Serial.println("Distance Transmission Failed");
        current_request = NONE;
        break;
      }
      
      dsh_radio.sendEnd();
      current_request = NONE;
      break;
       
    case DIST:
      if (!dsh_radio.sendSensorReading("DIST", distance))
        Serial.println("Temp Transmission Failed");
      dsh_radio.sendEnd();
      current_request = NONE;
      break;
    
    default:
      current_request = NONE;
 
  }

  
  
}

