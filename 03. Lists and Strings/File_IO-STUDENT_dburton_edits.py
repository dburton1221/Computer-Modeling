import re #regular expressions just b/c I want to get rid of the newline characters
l_f=re.compile('.*$') #we find eveyrthing up until the newline character

#our lists of data from the columns, yet to be filled
names=[]
living=[]
height=[]
mass=[]
brain=[]

humans=open("human_evolution.txt") #open sthe fiel as a variable we can access
for line in humans: #visualizing how we're goign to take the lines and make them into columns
    if line[0] not in ["S","-"," "]: #avoiding all the excess stuff
        #the names
        names_i=line[0:20] #the relatiev section where names would be
        names.append(names_i.replace(" ","")) #getting rid of teh whitespaces and appending it to our lists
        #living
        living_i=line[20:35]
        living.append(living_i.replace(" ",""))
        #height
        height_i=line[35:50]
        height.append(height_i.replace(" ",""))
        #mass
        mass_i=line[50:60]
        mass.append(mass_i.replace(" ",""))
        #Braaaaiinzz!!!
        l_s=l_f.match(line) #we search the string for matches to the regular expression
        l_h=l_s.group() #we make a variable of the whole matches which would be thta entire line
        brain_i=l_h[60:]
        brain.append(brain_i.replace(" ",""))
humans.close()

#lets' clean up the contents of our lists
def cleaner(lst):
    if "\n" in lst: #gettign rid of nay newline characters that got through
        lst.remove("\n")
    if lst[-1]=='': #deletign the empty strings at teh end of the lsist
        del lst[-1]
        
#cleanign all of the lists up
cleaner(names)
cleaner(living)
cleaner(height)
cleaner(mass)
cleaner(brain)

#Our dictioanries being made
human_evo={}
for person in range(len(names)): #person is a number
    personal_data={} #personal data is an empty dictionary to fill
    n_person=names[person] #the name of a person is 
    personal_data["Lived When (mil. yrs)"]=living[person] #we add key-val pairs into the dictioanry
    personal_data["Adult Height (m)"]=height[person] #from our lists
    personal_data["Body Mass (kg)"]=mass[person]
    personal_data["Brain Volume (cm**3)"]=brain[person]
    human_evo[n_person]=personal_data

for key,val in human_evo.items(): #we get items from the dictionary
    print(key) #we print the key
    for kee,vaa in val.items(): #teh value accessed is a dictionary
        print(kee,vaa) #so we print a key and val from that dictionary
    print() #we make a new line b/c why nto make it look nice