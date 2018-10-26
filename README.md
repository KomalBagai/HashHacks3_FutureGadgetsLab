# HashHacks3_FutureGadgetsLab
An Overtaking Assistance System developed as a part of the HashHacks3.0 hackathon. 

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/pbTPrBaxpX0/0.jpg)](https://www.youtube.com/watch?v=pbTPrBaxpX0)

[![Watch the video](https://raw.github.com/ishanijanveja/HashHacks3_FutureGadgetsLab/master/ressources/WebMole_Youtube_Video.png)](https://www.youtube.com/watch?v=pbTPrBaxpX0&feature=youtu.be)


![alt text](https://raw.githubusercontent.com/ishanijanveja/hashHacks3_FutureGadgetsLab/master/abstract/flow.png)

### What is the problem that we aim to solve?

India, being an overpopulated country, suffers from highly busy roads and a huge amount of traffic. This leads to various road accidents occurring very frequently. According to Annual Report of Transport Research Wing on Road accidents in India, around 5,01,423 accidents are claimed in 2015 in India resulting in around 1,46,133 deaths. 

One of the major causes of these accidents is the risky overtaking on the roads. Around 30,134 accidents happened solely due to this reason. The overtaking becomes risky when the driver doesn’t know if he can overtake the vehicle in front or not. Due to this unawareness, he collides with the pedestrian/vehicle in front and hence leads to a disastrous accident. 

We aim to develop a solution that can address this issue completely and can make the driver aware of what he can come across if he overtakes a vehicle at any point. This will definitely make the roads safer for driving.

### How do we propose to address it? 

We propose to design an overtaking assistance system to assist drivers as they plan on overtaking the vehicles in front of them. 

All previous solutions that have been proposed to deal with this issue work on the lines of establishing a communication link with the vehicle in front and providing a live stream from the cameras mounted on that vehicle (in front). As we are aware, this kind of a solution not only requires a huge bandwidth for live video streaming but the “see-through” mechanism is also not efficient enough in that it requires the driver to look at the video stream alongside driving. 

Therefore, we propose to design an effective system that avoids transmission of the heavy video stream and analyses the video from a local hardware itself to issue an alert to the vehicle behind in case the overtaking maneuver might result in an accident. The alert is issued using C2V (cloud-to-vehicle) communication.
