#importing everythign we need
from pylab import plot,hist,subplot,linspace,randn, pi, exp, sqrt, ylabel, xlabel, title, show, tight_layout

#defining our function
def n(x,sigma,mu): 
    return 1./ ( sigma * sqrt(2*pi) ) * exp( - (x - mu)**2 / (2 * sigma**2))

#defining a function to generate the data we want to plot
def sam_ret(size):
    x = linspace(-5,5,size) # an array of numbers, from -6 to 6, 100 points, including ends
    y = n(x,1,0)           # call the function to get all y points
    a = randn(size) # create an array of 1000 random numbers, zero mean, one standard deviation
    return (x,y,a) #returning a tuple that can be unpacked later

#creating a 1e3 subplot
subplot(2, 2, 1) #a subplot has (y,x,position on grid) arguments , position 1 is top left
x1,y1,a1=sam_ret(10**3) #unpacking of values from the tuple returned by the function
plot(x1, y1, 'green'); #this is our normal distribution plot with x,y values and a color of green
#this is our histogram with data, bin values, fill in colors for bins, bin outline colors, and normalizing to probablty
hist(a1,25,color='grey', ec='black', normed=True);
title('Sample Size 1e3') #the title of our subplot
xlabel('x value') #labels x-axis
ylabel('probablity') #labels y-axis

#creating a 1e4 subplot
subplot(2, 2, 2)
x2,y2,a2=sam_ret(10**4)
plot(x2, y2, 'green');
hist(a2,25,color='grey', ec='black',normed=True);
title('Sample Size 1e4')
xlabel('x value')
ylabel('probablity')

#creatign a 1e6 subplot
subplot(2, 2, 3)
x3,y3,a3=sam_ret(10**6)
plot(x3, y3, 'green');
hist(a3,25,color='grey', ec='black', normed=True);
title('Sample Size 1e6')
xlabel('x value')
ylabel('probablity')

#creating a 1e8 subplot
subplot(2, 2, 4)
x4,y4,a4=sam_ret(10**8)
plot(x4, y4, 'green');
hist(a4,25,color='grey', ec='black', normed=True);
title('Sample Size 1e8')
xlabel('x value')
ylabel('probablity')

#thsi makes it so the plots don;t overlap with each other
tight_layout()

#telling for the plots to be displayed
show()