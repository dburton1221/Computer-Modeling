# Array based implementation:
from pylab import randn, ones, figure, plot, show, sqrt, title, zeros

def curve2(z,i_start,i_end,var,s):
    # Find di, the change in indices:
    di=i_end-i_start #subtract start from end
    
    #find the height of teh unperturbed midpoint
    h_in=z[i_start]+(z[i_end]-z[i_start])/2 #add difference between start and end positions to the start pos height

    if di > 1: # Base case, keep bisecting until the indices are 1 apart
        # Find the index of the midpoint in bisection (// is integer division)
        i_n=i_start+di//2 #midpoint index is start index plius half od the difference
        # Set the value of z at the index where bisection occurs to
        # dz + perturbation:
        ds=h_in #unperturbed height is h_in
        delta = sqrt(var) * randn() #we then vary the height of the midpoint
        z[i_n]=ds+delta #we add that variance to the current height
        
        # Make recursive calls to the two segments on either side of the perturbed
        # point:
        curve2(z,i_start,i_n,var/s,s) #callign the left side
        curve2(z,i_n,i_end,var/s,s) #calling the rigth side
        
# Define the size of the array
N = 100

z = zeros(N)
z[0],z[-1]=1,1  # This is so results look like list results:
H = 1. # Hurst's exponent
curve2(z,0,N-1,0.01,2**(2*H))
figure(1)
plot(z,'k')
title("Hurst Exponent = 1.0")
show()

z = zeros(N)
z[0],z[-1]=1,1
H = 0.5 # Hurst's exponent
curve2(z,0,N-1,0.01,2**(2*H))
figure(1)
plot(z,'k')
title("Hurst Exponent = 0.5")
show()

z = zeros(N)
z[0],z[-1]=1,1
H = 0.05 # Hurst's exponent
curve2(z,0,N-1,0.01,2**(2*H))
figure(1)
plot(z,'k')
title("Hurst Exponent = 0.05")
show()
