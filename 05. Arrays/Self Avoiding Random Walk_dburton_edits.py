from pylab import ones,zeros,array,plot,show,title,xlabel,ylabel,randint,imshow,subplot
#from random import shuffle, no longer necessary
#%matplotlib inline #this is needed to display within iPython Jupyter notebook

def int_ary(s_tp): #takes in a tuple and gives back starting positions and a 2D array of zeros
    s_tup=(s_tp,s_tp)
    garden=zeros(s_tup) #preparing the 2D array that will be walked around in, accepts N as a tuple
    rows,cols=s_tup #unpacking the rows and columns values from the tuple
    #assigning the starting x and y positions by how the rows and columns numbers divide
    if rows%2!=0:
        st_x=(rows//2)+(rows%2)-1 #this roudns up so we always are at the middle
    else:
        st_x=(rows//2)+randint(0,2)-1 #we introduce randomness to decrease bias of side of even div we are on
    if cols%2!=0:
        st_y=(cols//2)+(cols%2)-1 #same thing as above but for columns
    else:
        st_y=(cols//2)+randint(0,2)-1
    st_pos=(st_x,st_y) #starting position as a tuple
    return(st_pos,garden)

#accepts a tuple of cirrent positions and the array and returns a tuple of where to move next
def move_it(posy,pty): #we like to MOVE IT! MOVE IT!
    cu_x,cu_y=posy
    m_possible=[]
    trp=0
    try: #testing for up
        if pty[cu_x][cu_y+1]==0: #we make sure that teh space has nto been visited before
            m_possible.append((cu_x,cu_y+1)) #we make this an option to go to
        else: #we are keeping track of being trapped by own path
            if pty[cu_x][cu_y+1]==1:
                trp+=1
    except:
        m_possible.append("None") #you have the option to walk off the grid now
    try: #testign for down
        if pty[cu_x][cu_y-1]==0 and (cu_y-1)!=(-1): #make sure we don't do reverse indexing and it hasn't been visited
            m_possible.append((cu_x,cu_y-1))
        else:
            if pty[cu_x][cu_y-1]==1:
                trp+=1
            elif (cu_y-1)==(-1): #you may walk off the grid now
                m_possible.append("None")
    except:
        pass
    try: #testign for right
        if pty[cu_x+1][cu_y]==0:
            m_possible.append((cu_x+1,cu_y))
        else:
            if pty[cu_x+1][cu_y]==1:
                trp+=1
    except:
        m_possible.append("None")
    try: #testign for left
        if pty[cu_x-1][cu_y]==0 and (cu_x-1)!=(-1):
            m_possible.append((cu_x-1,cu_y))
        else:
            if pty[cu_x-1][cu_y]==1:
                trp+=1
            elif (cu_x-1)==(-1): #you can now walk off the grid as an option
                m_possible.append("None")
    except:
        pass
    if len(m_possible)>0: #we make a a valif move if possible
        move=m_possible[randint(0,len(m_possible))]
    elif trp==4: #we return trapped if we have made our own path trapping us
        move="Trapped"
    return move


def self_avoid_random_walk(N,trials,PLOT=False):
    steps,trapped=0,0 #total steps made, when trapped
    for i in range(trials): #this for loop is for our number of simulations
        stpos,grid=int_ary(N) #we reintialize the starting positions and grid everytime
        tnot=0 #we reset the number of times trapped or off grid so taht the whiel loop restarts
        c_x,c_y=stpos #we reset to starting position everytime
        while tnot<1: #we continue to move around as logn as we don;t go off grid or get trapped
            grid[c_x][c_y]=1 #we say that we have been where we are standing
            do_it=move_it((c_x,c_y),grid) #we then produce the next move
            if do_it=="Trapped": #we record the trapped scenario and break the loop
                tnot+=1
                trapped+=1
            elif do_it=="None": #we just aren't allowed to walk off the grid, so we only break the loop
                tnot+=1
            else: #huzzah, we can make a move, so we do it!
                c_x,c_y=do_it #we unpack the tuple and reassign new positions
                steps+=1 #we record the move after we make it as a step
            #print(do_it)
            #imshow(grid,interpolation='nearest',cmap='gray')
            #show()
    return(steps/trials,trapped/trials)

l = []   # Hold the average length of random walks in a list.
p = []   # Hold the probability of getting trappend in a list.
rs = range(22,102,5)   # These are the sizes of grids that are explored.
for s in rs:   # for each size of grid.
    t = self_avoid_random_walk(s,500,False)   # Get the data through simulation. store in t.
    p.append(t[1])  # record the probability of being trapped
    l.append(t[0])  # record the average length of walk

# some plotting code that should be somewhat clear...
plot(array(rs)-2,p,'ko-')
title("Random Walker Results (500 Trials)")
xlabel("Matrix size (N)")
ylabel("Probability trapped")
show()

plot(array(rs)-2,l,'ro-')
title("Random Walker Results (500 Trials)")
xlabel("Matrix size (N)")
ylabel("Average step in walk")
show()