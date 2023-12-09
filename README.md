# Monte-Carlo-Simulation
A program shows that sometimes it is a random event at the first sight but when it comes to a very large amount the result will convert to a constant number.
Imagine a 100 x 50 of rectangle area, and there're two small area.
One shape is circle, its centre is at (20, 20) and the radius is 10.
One shape is aquare, its centre is at (80, 10) and each of its side length is also 10.
![image](https://github.com/Yorkxe/Monte-Carlo-Simulation/blob/main/%E6%8A%95%E5%BD%B1%E7%89%871.PNG)
And we started to throw marbles from a random location above the area.
So what's the ratio of marble in circle area and marble in square area?
It seems that it could be 0 ~ 1, right?
But how about we throwed 100 marbles, 1000 marbles, 10000 marbles?
The result is quite interesting, when the amount of marbles arises the ratio converts to a constant number.
Guess what, the constant number is π(3.1415)!
Why it converts to a constant number?
Let's have a little analysis.
All the marbles randomly fall on the rectangle area, so the only thing that influence the probability of marbles fall on the smaller area is the area.
The bigger area the more probabilisticly the marbles fall on that area.
So we can have a quick calculation.
![image](https://github.com/Yorkxe/Monte-Carlo-Simulation/blob/main/The%20ratio%20of%20circle%20and%20square.PNG)
So, isn't it interesting?
Share with your friends!
And there're two program illustrate this simulation.
The first one is console version, type in the amount of marbles and it will print the amount of marbles in circle and square area and the ratio.
![image](https://github.com/Yorkxe/Monte-Carlo-Simulation/blob/main/Console%20Version.PNG)
The second one create the fifure that shows the relation between amount of marbles and ratio.
![image](https://github.com/Yorkxe/Monte-Carlo-Simulation/blob/main/Figure%20version.PNG)
