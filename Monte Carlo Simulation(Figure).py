import random, math
import matplotlib.pyplot as plt
import numpy as np
print('It''s a Monte Carlo Simulation.')
print('It shows the result of a simulation.')
print('The content of the simluation is that there''s a \
rectangle area and two smaller area.')
print('One area is circle and the other is square.')
print('The radius of the circle is equal with the length \
of the square.')
print('And countless marbles will fall on the rectangle \
area randomly.')
print('This program will calculate the amount of \
marbles fall on the square area and the circle area.')
print('And most imprtantly the ratio of probability of \
circle area and the square area.')
print('You need to type in a number for the amount of marbles.')
print('And it will show the figure for the ratio per marble.')
amount = int(input('press the amount of marbles: '))

square = circle = 0
square_amount = [0] * amount
circle_amount = [0] * amount
result = [0] * amount

for i in range(amount):
    x = random.uniform(0, 100)
    y = random.uniform(0, 50)
    if ( ((x - 20)** 2) + (((y - 20)** 2)) )** 0.5 <= 10:
        circle += 1
        circle_amount[i] = circle
    elif 75 <= x and x <= 85 and 5 <= y and y <= 15:
        square += 1
        square_amount[i] = square
    if square != 0:
        result[i] = circle / square


x = np.linspace(0, amount, amount) 
fig, ay = plt.subplots(figsize=(16, 9))

plt.plot(x, result, '.')
plt.axhline(y = 3.1415, xmin = 0, xmax = amount, color = "red", linestyle="--")
plt.yticks([0, 1, 2, 3, 3.1415, 4, 5, 6, 7, 8, 9, 10])
plt.xticks([i for i in range(0, amount + 1, 1000)])
ay.get_yticklabels()[4].set_color("red")
plt.xlabel('Amount of Marbles', size = 16)
plt.ylabel('Ratio of Circle area and  Square area', size = 16)
plt.title('Monte Carlo Simulation', size = 20)
plt.axes([0, 0, 0, 0])
plt.show()     
 
            
            