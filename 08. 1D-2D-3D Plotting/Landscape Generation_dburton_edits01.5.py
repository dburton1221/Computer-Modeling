#This program generates a random 3D terrain
from mpl_toolkits.mplot3d.axes3d import Axes3D
from pylab import *

def surface(z,i_s,i_e,j_s,j_e,var,s):
    """
    INPUTS:
    z - an NxN numpy array that will contain the finished landscape
    i_s - the index where the row of the region being perturbed at the center
           begins
    i_e - the index of the row where the region being perturbed at the center ends
    j_s - as with i_s, but now the begining column
    j_e - as with i_e, but now the ending column
    var - the variance
    s   - the range of perturbations, related to the Hurst exponent
    
    OUTPUT:
     because arrays are passed by reference, z will contain the landscape.
    """
    # Differences in indices in both directions
    di = i_e - i_s
    dj = j_e - j_s
    
    # The base from which to perturb, 1/4 the corners:
    z_b = .25*(z[i_s,j_s] + z[i_s,j_e] +\
                  z[i_e,  j_s] + z[i_e  ,j_e])    
    # Indices of the mid-point of the square being peturbed:
    i_n = i_s + di//2
    j_n = j_s + dj//2
    # Apply the perturbation to the center:
    z[i_n,j_n] = z_b + sqrt(var) * randn()
    
    if di > 1 or dj>1:  # Base case - continue until indices adjacent
        # Provide averages on edges for coming recursive calls
        z[i_s,j_n] = (z[i_s,j_s] + z[i_s,j_e]) / 2
        z[i_n,j_e] = (z[i_s,j_e] + z[i_e,j_e]) / 2
        z[i_e,j_n] = (z[i_e,j_s] + z[i_e,j_e]) / 2
        z[i_n,j_s] = (z[i_s,j_s] + z[i_e,j_s]) / 2

        surface(z ,i_s, i_n ,j_s ,j_n , var/s, s)
        surface(z ,i_n, i_e ,j_s ,j_n , var/s, s)
        surface(z ,i_s, i_n ,j_n ,j_e , var/s, s)
        surface(z ,i_n, i_e ,j_n ,j_e , var/s, s)
    

N = 100
z = zeros((N,N))
H = .75  # Hurst's exponent
surface(z,0,N-1,0,N-1,.1,2**(2*H))

fig = figure(figsize=(14,8))

x,y = meshgrid(range(0,N),range(0,N))

#somehow make the below interactive

# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 1, 1, projection='3d')
p = ax.plot_surface(x,y,z, rstride=2, cstride=2, \
                    cmap=matplotlib.cm.terrain, linewidth=0, \
                    antialiased=True)

cb = fig.colorbar(p, shrink=0.5)

#in Spyder, go to Console>iPyhton Console>Graphics>Backend Graphics (change to Automatic)
#this give syou a popup that you cna interact with

#draw()
#draw is unecssary, matplotlib 3d plots are interactive by default; I just needed to get a popup window
#to make the figure interactive