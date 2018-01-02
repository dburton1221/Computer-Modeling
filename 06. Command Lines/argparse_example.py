#writing the parser for our script
import sys,argparse

#creating the description for our parser
parser=argparse.ArgumentParser(description="Plot some csv files")
#makign an argument for the filename
parser.add_argument("filename",help="Give the name of the csv file to plot") #filename cannto have spaces in it
#adding arg for x-axis column
parser.add_argument("x_axis",help="the x-axis of the plot",type=int)
#cols to be plotted agnst x-axis, allowing for multiple columsn to be plotted
parser.add_argument("cols",help="the cols to be plotted against the x-axis",type=int,nargs="+")

#we must process the arguments
args=parser.parse_args()

print("The file to be plotted is",args.filename)
print("The x-axis is",str(args.x_axis))
print("The cols to be plotted against the x-axis are",str(args.cols))