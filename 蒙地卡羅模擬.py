import random, time
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
print('And it will show the result every 1000 marbles.')
amount = int(input('press the amount of marbles: '))

square_amount = 0
rectangle_amount = 0

for i in range(amount + 1):
    x = random.uniform(0, 100)
    y = random.uniform(0, 50)
    if ( ((x - 20)** 2) + (((y - 20)** 2)) )** 0.5 <= 10:
        square_amount += 1
    if 75 <= x and x <= 85 and 5 <= y and y <= 15:
        rectangle_amount += 1
    if i % 1000 == 0:
        print('i = ', i)
        if rectangle_amount > 0:
            print('square_amount = %d, rectangle_amount = %d ,ratio = %f'% (square_amount, rectangle_amount, square_amount/rectangle_amount ))
            time.sleep(1)
        else:
            print('square_amount = %d, rectangle_amount = %d' % (square_amount, rectangle_amount))
            time.sleep(1)