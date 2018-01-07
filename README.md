# Site Unseen
## Inspiration
For those who are blind, maneuvering throughout one's own home can be a difficult, and sometimes dangerous, process. We aspired to help improve the lives of the visually impaired by making their homes more accessible.

## What it does
The IoT localization system polls coordinate data from an attached user gyroscope and a grid of external sensors in order to learn from the user's movements over time, map the room, and navigate the user with the need of eyesight.

## How we built it
Once we formulated an idea, we created a concept map in order to structure our project timeline. We distributed the workload amidst our group into four main categories: hardware, networking, data analysis, and the web application.

For hardware, we designed a low-latency sensor network using Arduino Uno's equipped with RFM69 radio frequency transceivers. Each transceiver acted as a wireless sensor node that transmitted ultrasonic distance data to a central gateway. We had a minimum of 4 ultrasonic sensors in the room and 1 ultrasonic sensor on the person to retrieve localization data. On the person navigating the room, we also equipped an Arduino 101 with a built in gyroscopic sensor. The combination of data from every sensor component allowed us to infer positions through data fusion techniques.

The DragonBoard was used as the central brain of the network; handling everything from data collection to data processing and fusion. It also works as a gateway bridge between the sensor module hub and the front-end visualization. Once processed, the raw data from the sensors is converted to X and Y coordinates which were used by the computer to draw a map of the current room over time. This data was stored in MySQL for ease of querying.

## Challenges we ran into
We initially started off with the Myo Armband which is capable of reading EMG signals from the muscle movement of the arm. We aimed at using the Myo Armband to get accelerometer and gyroscope data, unfortunately, due to software incompatibility reasons and after hours of spending trying to fix the problems, we decided it was best to use our remaining time to make a working system that make a working component. We decided to use the Arduino 101 which has a built-in accelerometer.

A few challenges were also figuring out how to localize the person when in blind spots where no external sensor was reading him/her, to understand the signal drifting and potentially fluctuating measurements, and finally optimization of the placement of sensors. We finalized one setup of the sensors for optimal readings, reduced the number of blind zones and wrote a program to run the data analysis. Pipelining and organizing data through wireless communications and serial ports. We decided on using the MQTT protocol for transferring data wirelessly. We used the PySerial library for read in serial data.

## Accomplishments that we're proud of
We are all proud of the fact that we were able to learn and use technologies of which we previously had little to no knowledge. Making it through the night was also a big accomplishment for us.

## What we learned
Every hour, we wrestled with a new concept. Albeit being an arduous process, we learned many skills and technologies along the way. A summary of the hard and soft skills we learned are: -The Myo Armband software and SDK -Arduino programming -Wireless networking -Qualcomm dragonboard - a very powerful microsensor -D3.js library for making floor plans
-Optimization of sensors and data analysis -Teamwork and collaboration -Communication between people of different technical backgrounds

## What's next for Site Unseen
With additional effort and time, Site Unseen would see various improvements in its design. Short term goals include making the system completely wireless and battery operated and developing a mobile application for caretakers. Implementation of graph theory along with machine learning techniques would improve data analysis and help create a more sophisticated localization algorithm. We also intend on making the system cost efficient and affordable.