//Making 3 Car Objects to show on the simulation
Car myCar1;
Car myCar2;
Car myCar3; 
//Variables to store the X-coordinates of the cars
float car1,car2,car3;
//Defines the variable to store the image for background
PImage img;

//This is the first function which- loads the background image and sets it and defines the myCar objects of all colors
void setup() {
  size(1386,592);//Size of the frame of simulation
  img = loadImage("road.jpg"); //Loads the image in the img variable
  // Parameters go inside the parentheses when the object is constructed.
  myCar1 = new Car(color(255,0,0),400,250,1); 
  myCar2 = new Car(color(0,0,255),600,250,1); 
  myCar3 = new Car(color(25,25,0),1000,350,-1);
}
//Draws the clusters of vehicles and the cars at particular locations
void draw() {
  image(img,0, 0);
  fill(255,0,0,63);
  triangle(car2, 250, car2+25, 450, car2+300,300);
  fill(0,255,0,63);
  car1=myCar1.drive();
  myCar1.display();
  car2=myCar2.drive();
  myCar2.display();
  car3=myCar3.drive2();
  myCar3.display();
  textSize(20);
  fill(255, 255, 255);
  text("Car1", car1-20, 250); 
  fill(255, 255, 255);
  text("Car2", car2-20, 250);
  fill(255, 255, 255);
  text("Car3", car3-20, 350); 
  if(car3<car2+250&&car3>car2+25){
    fill(255,0,0);
    ellipse(50,50,50,50);
  }
  else{
    fill(0,255,0);
    ellipse(200,50,50,50);
  }
}

// Even though there are multiple objects, we still only need one class. 
// No matter how many cookies we make, only one cookie cutter is needed.
class Car { 
  color c;
  float xpos;
  float ypos;
  float xspeed;

  // The Constructor is defined with arguments.
  Car(color tempC, float tempXpos, float tempYpos, float tempXspeed) { 
    c = tempC;
    xpos = tempXpos;
    ypos = tempYpos;
    xspeed = tempXspeed;
  }
//Displays the car
  void display() {
    stroke(0);
    fill(c);
    rectMode(CENTER);
    rect(xpos,ypos,80,40);
  }
//Changes the positions of the cars
  float drive() {
    xpos = xpos + xspeed;
    if (xpos > width) {
      xpos = 0;
    }
    return xpos;
  }

//Changes the positions of the cars in opposite(right to left direction
  float drive2() {
    xpos = xpos + xspeed;
    if (xpos < 0) {
      xpos = 1386;
    }
    return xpos;
  }
}
