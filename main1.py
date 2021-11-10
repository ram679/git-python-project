
# Python3 program for the above approach
import math
 
def checkperfectsquare(x):
     
    # If ceil and floor are equal
    # the number is a perfect
    # square
    if (math.ceil(math.sqrt(n)) ==
       math.floor(math.sqrt(n))):
        print("perfect square")
    else:
        print("no,it is not a perfect square")
     
# Driver code
n = 49
  
checkperfectsquare(n)
 
# This code is contributed by jana_sayantan