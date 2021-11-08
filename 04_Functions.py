
##############################################################################
#######################  creating a basic Function  ##########################
##############################################################################


def sumProblem(x, y):
    sum = x + y
    print(sum)
    sentence = 'The sum between {} and {} is {}'.format(x, y, sum)
    print(sentence)

sumProblem(2, 3)

def f(x):
    return x * x

print(f(3))
print(f(3) + f(4))


##### solving math problems

def CircleArea(r, measure):
    pi = 3.14159265
    area = pi * r*r
    if measure == 'm':
        message = 'The Area of an circle with radius = {} m is {} square meters'.format(r, area)
    elif measure == 'cm':
        message = 'The Area of an circle with radius = {} cm is {} square centimeters'.format(r, area)
    print(message)

##### Arguments of the function: radius and measure.
CircleArea(3, 'cm')

#### building another function, more general aproach.

def CircleArea2(r, measure):
    pi = 3.14159265
    area = pi * r*r
    message = 'The Area of an circle with radius r = {} {} is {} square {}'.format(r, measure, area, measure)
    print(message)
    
##### Arguments of the function: radius and measure.
CircleArea2(3, 'cm')
CircleArea2(5, 'km')

