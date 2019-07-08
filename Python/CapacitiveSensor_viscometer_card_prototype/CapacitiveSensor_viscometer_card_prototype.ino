#include <CapacitiveSensor.h>

/*
 * CapitiveSense Library Demo Sketch
 * Paul Badger 2008
 * Uses a high value resistor e.g. 10M between send pin and receive pin
 * Resistor effects sensitivity, experiment with values, 50K - 50M. Larger resistor values yield larger sensor values.
 * Receive pin is the sensor pin - try different amounts of foil/metal on this pin
 */

CapacitiveSensor   cs1 = CapacitiveSensor(2,3);   
CapacitiveSensor   cs2 = CapacitiveSensor(2,4);  
CapacitiveSensor   cs3 = CapacitiveSensor(2,5);   
CapacitiveSensor   cs4 = CapacitiveSensor(2,6);     
CapacitiveSensor   cs5 = CapacitiveSensor(2,7);       
CapacitiveSensor   cs6 = CapacitiveSensor(2,8);
CapacitiveSensor   cs7 = CapacitiveSensor(2,9);   
CapacitiveSensor   cs8 = CapacitiveSensor(2,10);  
CapacitiveSensor   cs9 = CapacitiveSensor(2,11);   
CapacitiveSensor   cs10 = CapacitiveSensor(2,12);     
     
void setup()                    
{
   cs1.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 1 - just as an example
   cs2.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 2 - just as an example
   cs3.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 3 - just as an example
   cs4.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 4 - just as an example
   cs5.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 5 - just as an example
   cs6.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 6 - just as an example
   cs7.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 1 - just as an example
   cs8.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 2 - just as an example
   cs9.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 3 - just as an example
   cs10.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 4 - just as an example
   Serial.begin(9600);
}

void loop()                    
{
    long start = millis();
    long total1 =  cs1.capacitiveSensor(30);
    long total2 =  cs2.capacitiveSensor(30);
    long total3 =  cs3.capacitiveSensor(30);
    long total4 =  cs4.capacitiveSensor(30);
    long total5 =  cs5.capacitiveSensor(30);
    long total6 =  cs6.capacitiveSensor(30);
    long total7 =  cs7.capacitiveSensor(30);
    long total8 =  cs8.capacitiveSensor(30);
    long total9 =  cs9.capacitiveSensor(30);
    long total10 =  cs10.capacitiveSensor(30);

    Serial.print(millis() - start);        // check on performance in milliseconds
    Serial.print(',');                    // tab character for debug windown spacing

    Serial.print(total1);       
    Serial.print(',');
    Serial.print(total2);   
    Serial.print(',');
    Serial.print(total3);    
    Serial.print(',');
    Serial.print(total4);         
    Serial.print(',');
    Serial.print(total5);              
    Serial.print(',');
    Serial.print(total6);     
    Serial.print(',');
    Serial.print(total7);   
    Serial.print(',');
    Serial.print(total8);    
    Serial.print(',');
    Serial.print(total9);         
    Serial.print(',');
    Serial.println(total10);                           

    delay(10);                             // arbitrary delay to limit data to serial port 
}
