import csv,sys
print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))
if len(sys.argv)>1:
    catch=""
    for i in sys.argv:
        catch=catch+i
    print(catch)