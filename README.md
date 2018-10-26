# HashHacks3_FutureGadgetsLab
An Overtaking Assistance System developed as a part of the HashHacks3.0 hackathon. 

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/pbTPrBaxpX0/0.jpg)](https://www.youtube.com/watch?v=pbTPrBaxpX0)

[![Watch the video](https://raw.github.com/ishanijanveja/HashHacks3_FutureGadgetsLab/master/ressources/WebMole_Youtube_Video.png)](https://www.youtube.com/watch?v=pbTPrBaxpX0&feature=youtu.be)



### What is the problem that we aim to solve?

India, being an over-populated country, suffers from highly busy roads and a huge amount of traffic. This leads to various road accidents occurring very frequently. According to Annual Report of Transport Research Wing on “Road accidents in India-2015”, around 5,01,423 accidents are claimed in 2015 in India only, resulting in around 1,46,133 deaths. 

One of the major causes of these accidents is the risky overtaking on the roads as demonstrated in the video above. Around 30,134 accidents happened solely due to this reason. The overtaking becomes risky when the driver doesn’t know if he can overtake the vehicle in front or not and hence takes an intuitive decision. Due to this unawareness, he tends to collide with the pedestrian/vehicle in front and hence leads to a disastrous accident. 

We aim to develop a solution that can address this issue completely and can make the driver aware of what he can come across if he overtakes a vehicle at any point. We aim to make this system non-invasive to the vehicle mechanics and day to day driving styles, is non distracting and works as close to real-time performance while not degrading the accuracy.

### How do we propose to address it? 

We propose to design an overtaking assistance system to assist drivers as they plan on overtaking the vehicles in front of them. 

All previous solutions that have been proposed to deal with this issue work on the lines of establishing a P2P (point to point) communication link with the vehicle in front and providing a live stream from the cameras mounted on that vehicle (in front). As we are aware, this kind of a solution not only requires a huge bandwidth for live video streaming but the “see-through” mechanism is also not efficient enough in that it requires the driver to look at the video stream alongside driving, hence heavily distracting their own driving.

Therefore, we propose to design an effective system that avoids transmission of the heavy video stream and analyses the video from a local hardware itself, incorporating edge computing, to issue an alert to the vehicle behind in case the overtaking maneuver might result in an accident. The alert is issued using C2V (cloud-to-vehicle) communication. This is achieved through a Green-Red Light mechanism for giving the indication of passing through freely for overtaking or not.

Technical Description of the solution 

The proposed architecture of our solution requires vehicles to have a camera mounted on the dashboard which is interfaced with an on-board processor. We intend to use a Raspberry Pi Model 3B along with a Pi-cam for this purpose in the prototype. This is used so as to provide good networking capabilities, efficient computing at the edge and fast connectivity with the camera module.

All vehicles, at each time, will use the camera to perform two tasks locally - (i) detect number plate of the vehicle in front and (ii) detect the vehicles approaching from the opposite side of the lane within a given Region of Interest (ROI) and having a size more than a given threshold indicating the degree of its closeness. These two tasks are performed in alternate frames to prevent excessive delays due to compute intensive detection algorithms. This works in part to make a computing pipeline that we aim to have near real-time results.

Each vehicle is also connected to a real-time database (Firebase) and identified by its car number. All information collected by the vehicles locally is updated on this real-time database. The visual representation of the structure of our database is shown in the figure below :


We take into consideration the scenario where Car 1 wants to overtake Car 2. Now Car1 first detects the number plate of Car 2 and establishes communication with it on the firebase database and forms a grouping. Car 2 then checks the presence of vehicles approaching it from the opposite lane. This is checked in a given Region of Interest. When a car of size more than a given threshold approaches the Car 2 (which represents the degree of closeness), it sets the value of the variable on the firebase to 0, representing that Car 1 cannot overtake. This is set as an event listener on Car 1 which lights Red light on it. If there is no obstruction in the given ROI, the variable is set to 1, lighting green light in Car 1, indicating it to overtake freely. 

![alt text](https://github.com/ishanijanveja/HashHacks3_FutureGadgetsLab/blob/master/ex.png)

### Flowchart

![alt text](https://raw.githubusercontent.com/ishanijanveja/hashHacks3_FutureGadgetsLab/master/flow.png)

### Technology Stack 
#### Hardware :
1. Camera Module 
2. Raspberry Pi for local processing 

#### Software :
1. OpenCv
2. Tensorflow
3. Keras
