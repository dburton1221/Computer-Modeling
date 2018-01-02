#thsi thing mostly works but does not quite return the pretty thing we want
import csv,re,argparse
from pylab import ylabel, xlabel, show, figure, scatter, cm, linspace, legend

#creating the description for our parser
parser=argparse.ArgumentParser(description="Plot some csv files") #the filename cannot have spaces in it
#makign an argument for the filename
parser.add_argument("filename",help="Give the name of the csv file to plot")
#adding arg for x-axis column
parser.add_argument("x_axis",help="the x-axis of the plot",type=int)
#cols to be plotted agnst x-axis, allowing for multiple columsn to be plotted
parser.add_argument("cols",help="the cols to be plotted against the x-axis",type=int,nargs="+")

#we must process the arguments
args=parser.parse_args()

#makign a function to extract data from a csv file and returns a list of lists containing each column in the file
def extract_data(nam_fil): #the name of the file must be input as a string with the file extension
    TheFile=nam_fil
    OurData=[] #an empty list to hold things
    with open(TheFile) as csvfile:  # This is a nice construct that helps with exceptions.
        reader = csv.reader(csvfile) # Create csv reader
        for row in reader: #every row in the reader is a list containing strings
            OurData.append(row) #we append that list into the Our Data list so we can then convert rows to columns
    OurData=list(zip(*OurData)) #this transposes our rows into columns but creates a list of tuples
    #first attempt doing list comprehension, we are applying list function to every item in OurData, requires brackets
    OurData=[list(i) for i in OurData]
    return OurData

#create a function to convert the strings with numbers into floats
def str_to_flt(lst_of_lsts): #takes a list of lists that is full fo strings
    decimal_fun=re.compile(r'\d*\.?\d*') #we make a regex variable for any numbers, maybe period, any numbers
    for i in range(len(lst_of_lsts)): #we go through positions of lists within the list
        for j in range(len(lst_of_lsts[i])): #for each item in the raneg of the first list
            lst_of_lsts[i][j]=lst_of_lsts[i][j].replace(",","") #we need to eliminate commas if they exist
            fun=decimal_fun.match(lst_of_lsts[i][j]) #we then check for a mtch to the regex variable
            if fun.group()!="": #if we found a match to the regex variable
                lst_of_lsts[i][j]=float(fun.group()) #we turn into a floatign point number
    return lst_of_lsts #returns a list fo lists with all str nums as floating point numbers

#a function that finds the labels for data and teh header
def header_labels(ListOfLists,column): #takes a list fo lists and finds the header and labels
    header=""
    label_pos=[column,0] #position of label is column in the csv and position in the column
    #finding the label for the data
    for i in range(len(ListOfLists[column])):
        if (type(ListOfLists[column][i]) is float)==True:
            label=ListOfLists[column][i-1] #teh thign right above a float is probably its label
            label_pos=[column,i-1]
            break #we found what we needed, so we break it    
        else: #we now run a majority check to see if most of the things in this row are floats
            count=0 #tracking the number of floats we find
            traveled=0 #tracking how many columns we have visited
            for j in range(len(ListOfLists)): #we check to see if most of the things in other 
                #columns at this row are floats
                if (type(ListOfLists[j][i]) is float)==True:
                    count+=1
                    traveled+=1
                else:
                    traveled+=1
            if (count/traveled)>=0.5:
                label=ListOfLists[column][i-1] #if the things on either side of a str are floats, 
                #the thing above is probably that label
                label_pos=[column,i-1]
                break #if we found the label, we break it
    #systematically fginding the header
    while True:
        for i in range(len(ListOfLists[:label_pos[0]+1])): #we start by sreaching the column the label was in
            for j in range(len(ListOfLists[label_pos[0]-i])):
                tester=ListOfLists[label_pos[0]-i][label_pos[1]-j] #the item we are testing to be a header
                #the tester cannot match the label, cannot be empty str, must be a str, and nto same row as label
                if tester!=label and tester!="" and (type(tester) is str)==True and (label_pos[1]-j)!=(label_pos[1]):
                    header=tester
                    break
            if header!="" and header!=label:
                break
        if header!="" and header!=label:
            break
    if header=="": #we need a readout
        header="Ergawd!!"
    return (header,label)

#make a function to normalize the data in the csv, be able to say this thing is str and should be a number,
#fill in some number
def normal_data(lst_o_lst):
    for i in range(len(lst_o_lst)):
        for j in range(len(lst_o_lst[i])): #we're going to check every item in a list
            count=0
            travel=0
            current=lst_o_lst[i][j]
            for h in range(len(lst_o_lst)): #check against the average of tests
                test=lst_o_lst[h][j]
                if (type(lst_o_lst[h][j]) is float)==True:
                    count+=1
                    travel+=1
                else:
                    travel+=1
            average=count/travel #we average how many were floats
            #if teh thing in this row isn't a float and most other things are, then we should fill it in
            if average>=0.5 and (type(current) is float)==False:
                lst_o_lst[i][j]=float(0)
    return lst_o_lst

#make a function to simplify the list so it is all just floats
def simple_list(ug_list): #takes the list of columns
    ug_list=list(zip(*ug_list)) #puttign this back as list fo rows
    ug_list=[list(i) for i in ug_list] #convertign everythign back into lists
    while True:
        count=0
        for i in range(len(ug_list)): #deletign any rows that contain strings
            if all(isinstance(thing,float) for thing in ug_list[i])!=True:
                #all checks that every thing is true for such conditions
                #isinstance checks that this thing matches the type of object specified
                #.... for thign in myCat is list comprehenison and checks every thign in myCat
                count+=1 #thsi is to prevent us from exiting while loop
                del ug_list[i] #we delete any row that is not only floats
                break #then, we restart, the for loop so we don;t get an index error
        if count==0:
            break
    pretty_list=list(zip(*ug_list)) #puttign back as a list of columns
    pretty_list=[list(i) for i in pretty_list] #convertign everythign back into lists
    return pretty_list

#takes a list of lists and a list fo columns and returns a dictionary with header, labels, and values of each column
#we're handlign the x_axis in thsi as well just to unify things
def organizing_info(lol,x_ax,col):
    lol_dict={} #our empty dictionary to shove stuff into
    #extract teh headers and labels
    for val in col:
        lol_dict[val]={} #create a dictionary to hold these thinsg for the value of the column
        header,label=header_labels(lol,val) #unpack teh tuple from the header,labels function
        lol_dict[val]["Header"]=header #assign a key-valeu pair for the header
        lol_dict[val]["Label"]=label #assign a key-valeu paoir for the label
    #handinlign the x-axis
    lol_dict[x_ax]={}
    xheader,xlabel=header_labels(lol,x_ax)
    lol_dict[x_ax]["Header"]=xheader
    lol_dict[x_ax]["Label"]=xlabel
    #simplify the list
    lol=simple_list(lol)
    #shove evrythign into a dictionary
    for val in lol_dict.keys():
        lol_dict[val]["points"]=lol[val]
    return lol_dict

#next, we must pass teh arguments from argparse to the functiosn we have written
NewData=extract_data(args.filename) #extracting data from the file
NewData=str_to_flt(NewData) #we convert all str's with nums into floats
NewData=normal_data(NewData)  #we convert the str's that shoudl be floats into filler data fo zeroes

redy_plot=organizing_info(NewData,args.x_axis,args.cols)

x=redy_plot[args.x_axis]['points'] #we take all fo the points from the value given for x
figure(figsize=(12,12))
clrs = cm.rainbow(linspace(0, 1, len(args.cols)))

#find a way to randomly choose a row from the clrs list
clr_c=0 #our color counter, so each data set is a differenmt color
clct_labels=[] #our empty list to collect all of the headers for objects which is tehir "label"

lab_check=[] #thsi checks teh "labels" which are really the units are the same for the y-axis
for thing in args.cols:
    lab_check.append(redy_plot[thing]["Label"])

if all(lab_check[0]==thing for thing in lab_check)==True: #checks all labels are teh same, if so, we do below
    #our for loop to ge through everythibng to add to the plot
    for thing in args.cols:
        choce=clrs[clr_c]
        y=redy_plot[thing]['points'] #we take the value for points from the column value in the list of columns
        point=scatter(x,y,c=choce,alpha=0.5, label=redy_plot[thing]["Header"])
        #find a way to connect the dots for each group
        clct_labels.append(point)
        clr_c+=1
    #we can do teh following, because the units for teh data are the same
    ylabel(redy_plot[args.cols[0]]["Label"])
    
else:
    for thing in args.cols:
        choce=clrs[clr_c]
        y=redy_plot[thing]['points']
        #we comdine the units (label) with the type of data (header) so we don't mix units on the ylabel
        con_cat=redy_plot[thing]["Header"]+","+redy_plot[thing]["Label"]
        point=scatter(x,y,c=choce,alpha=0.5, label=con_cat,norm=True)
        #find a way to connect the dots for each group
        clct_labels.append(point)
        clr_c+=1
    #we can do teh following, because the units for teh data are the same
    ylabel("Check the legend, units not same")

xlabel(redy_plot[args.x_axis]["Header"]) #the x-ax value is zero, must be changed to args.x_ax when moved to Spyder

legend(handles=clct_labels)

show()