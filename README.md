# The-Carpenter-s-Challenge
This challenge is to provide a Python program to minimize the wastage of wood by using it to make boxes.

As little kids and grown ups, we have often toyed around with pieces of wood, and almost everyone may have at least once tried making 
something out of those.

Imagine that there are n pieces of wood, each piece of wood has three dimensions: x(length), y( breadth) and z(height). A carpenter wishes 
to create 'm' boxes out of these n pieces such that wastage of wood is minimum.The dimensions of these 'm' boxes are p,q and r respectively 
and can be different for each box so as to minimize wastage.

Your challenge is to provide a Python program which when executed:

-  Allows recording different pieces of wood and the dimensions of each piece of wood
-  Allows recording of 'm' - the number of boxes required, while allowing 'm' input to be optional as well
-  Allows recording of some or all of dimensions of the 'm' boxes if there is a specific requirement for sizes. If only few dimensions are 
   specified, the program is free to calculate the dimensions of remaining boxes for wastage reduction
-  Provides optimized dimensions p,q and r and indicates wastage per box, and total minimized wastage
-  Since more waste wood may be available, the program may even predict addition of what new sizes x, y and z (of additional waste wood) 
   can produce even better boxes for further wastage reduction.  The program may help indicate whether one or two or more additional pieces
   of wood of specified dimensions can help reduce wastage further
