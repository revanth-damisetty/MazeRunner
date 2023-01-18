#sender side
from sense_hat import SenseHat
import time
import RPi.GPIO as GPIO
from time import sleep
from bluedot.btcomm import BluetoothServer

sense=SenseHat()

green=(0,255,0)
blue=(0,0,100)
orange=(255, 213, 128)

# Maze size
N = 8

# A utility function to print solution matrix sol
def printMaze( sol ):
    w=(150,150,150)
    b=(64,40,14)
    maze=[]
    for i in sol:
        for j in i:
            print(str(j) + " ", end ="")
        
            if j==1:
                maze.append(w)
            else:
                maze.append(b)
        print("\n")
    sense.set_pixels(maze)
   
   

# A utility function to check if x, y is valid
# index for N * N Maze

def isSafe( maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False

""" This function solves the Maze problem using Backtracking.
      It mainly uses solveMazeUtil() to solve the problem. It
      returns false if no path is possible, otherwise return
      true and prints the path in the form of 1s. Please note
      that there may be more than one solutions, this function
      prints one of the feasible solutions. """
def solveMaze( maze ):
    # Creating a 4 * 4 2-D list
    sol = [ [ 0 for j in range(N) ] for i in range(N) ]
   
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist");
        return False
    return sol
# A recursive utility function to solve Maze problem
def solveMazeUtil(maze, x, y, sol):
    # if (x, y is goal) return True
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True
    # Check if maze[x][y] is valid
    if isSafe(maze, x, y) == True:
        # mark x, y as part of solution path
        sol[x][y] = 1
        # Move forward in x direction

        if solveMazeUtil(maze, x + 1, y, sol) == True:
            sense.set_pixel(y,x,blue)
            return True

        # If moving in x direction doesn't give solution
        # then Move down in y direction
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            sense.set_pixel(y,x,blue)
            return True
       
        # If none of the above movements work then
        # BACKTRACK: unmark x, y as part of solution path
        sol[x][y] = 0
        return False
   

def next(sol,x,y,dire):
    a=False
    if x>0 and a==False:
        if sol[x-1][y]==1:
            if dire!="down":
                x-=1
                dire="up"
                a=True
    if x<7 and a==False:
        if sol[x+1][y]==1 :
            if dire!="up":
                x+=1
                dire="down"
                a=True
    if y<7 and a==False:
        if sol[x][y+1]==1 :
            if dire!="left":
                a=True
                y+=1
                dire="right"
    if y>0 and a==False:
        if sol[x][y-1]:
            if dire!="right" :
                y-=1
                a=True
                dire="left"
                
    print(x,y,dire)
    for i in range(8):
        for j in range(8):
            if maze[i][j] ==1:
                sense.set_pixel(j,i,orange)
            if sol[i][j] ==1:
                sense.set_pixel(j,i,blue)
    sense.set_pixel(y,x,green)
    time.sleep(1)
    return x,y,dire

# Driver program to test above function
if True:
    # Initialising the maze
    maze =     [[1, 0, 0, 0,0,0,0,0],
                [1, 1, 0, 1,0,0,0,0],
                [0, 1, 0, 0,0,0,0,0],
                [1, 1, 1, 1,1,1,1,1],
                [0, 1, 0, 1,0,0,0,1],
                [0, 1, 0, 1,1,1,1,1],
                [0, 1, 1, 1,0,1,0,1],
                [1, 1, 1, 0,1,0,1,1]]
    printMaze(maze)
    time.sleep(5)
    print("\n")
    sol=solveMaze(maze)
   
    x,y=0,0
    dire="right"
    for i in range(8):
        for j in range(8):
            if maze[i][j] ==1:
                sense.set_pixel(j,i,orange)
    sense.set_pixel(y,x,green)
    time.sleep(2)
    
    c = BluetoothServer(None)
    
    
    while True:
        t=dire
        x,y,dire=next(sol,x,y,dire)
        if t==dire:
            c.send("forward")
        elif t=="up":
            if dire=="left":
                c.send("left")
            else:
                c.send("right")
        elif t=="right":
            if dire=="up":
                c.send("left")
            else:
                c.send("right")
        elif t=="left":
            if dire=="down":
                c.send("left")
            else:
                c.send("right")
        else:
            if dire=="right":
                c.send("left")
            else:
                c.send("right")
        sleep(2)
            
        if x==7 and y==7:
            
            break
    time.sleep(5)
    sense.clear()#sender side
from sense_hat import SenseHat
import time
import RPi.GPIO as GPIO
from time import sleep
from bluedot.btcomm import BluetoothServer

sense=SenseHat()

green=(0,255,0)
blue=(0,0,100)
orange=(255, 213, 128)

# Maze size
N = 8

# A utility function to print solution matrix sol
def printMaze( sol ):
    w=(150,150,150)
    b=(64,40,14)
    maze=[]
    for i in sol:
        for j in i:
            print(str(j) + " ", end ="")
        
            if j==1:
                maze.append(w)
            else:
                maze.append(b)
        print("\n")
    sense.set_pixels(maze)
   
   

# A utility function to check if x, y is valid
# index for N * N Maze

def isSafe( maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False

""" This function solves the Maze problem using Backtracking.
      It mainly uses solveMazeUtil() to solve the problem. It
      returns false if no path is possible, otherwise return
      true and prints the path in the form of 1s. Please note
      that there may be more than one solutions, this function
      prints one of the feasible solutions. """
def solveMaze( maze ):
    # Creating a 4 * 4 2-D list
    sol = [ [ 0 for j in range(N) ] for i in range(N) ]
   
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist");
        return False
    return sol
# A recursive utility function to solve Maze problem
def solveMazeUtil(maze, x, y, sol):
    # if (x, y is goal) return True
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True
    # Check if maze[x][y] is valid
    if isSafe(maze, x, y) == True:
        # mark x, y as part of solution path
        sol[x][y] = 1
        # Move forward in x direction

        if solveMazeUtil(maze, x + 1, y, sol) == True:
            sense.set_pixel(y,x,blue)
            return True

        # If moving in x direction doesn't give solution
        # then Move down in y direction
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            sense.set_pixel(y,x,blue)
            return True
       
        # If none of the above movements work then
        # BACKTRACK: unmark x, y as part of solution path
        sol[x][y] = 0
        return False
   

def next(sol,x,y,dire):
    a=False
    if x>0 and a==False:
        if sol[x-1][y]==1:
            if dire!="down":
                x-=1
                dire="up"
                a=True
    if x<7 and a==False:
        if sol[x+1][y]==1 :
            if dire!="up":
                x+=1
                dire="down"
                a=True
    if y<7 and a==False:
        if sol[x][y+1]==1 :
            if dire!="left":
                a=True
                y+=1
                dire="right"
    if y>0 and a==False:
        if sol[x][y-1]:
            if dire!="right" :
                y-=1
                a=True
                dire="left"
                
    print(x,y,dire)
    for i in range(8):
        for j in range(8):
            if maze[i][j] ==1:
                sense.set_pixel(j,i,orange)
            if sol[i][j] ==1:
                sense.set_pixel(j,i,blue)
    sense.set_pixel(y,x,green)
    time.sleep(1)
    return x,y,dire

# Driver program to test above function
if True:
    # Initialising the maze
    maze =     [[1, 0, 0, 0,0,0,0,0],
                [1, 1, 0, 1,0,0,0,0],
                [0, 1, 0, 0,0,0,0,0],
                [1, 1, 1, 1,1,1,1,1],
                [0, 1, 0, 1,0,0,0,1],
                [0, 1, 0, 1,1,1,1,1],
                [0, 1, 1, 1,0,1,0,1],
                [1, 1, 1, 0,1,0,1,1]]
    printMaze(maze)
    time.sleep(5)
    print("\n")
    sol=solveMaze(maze)
   
    x,y=0,0
    dire="right"
    for i in range(8):
        for j in range(8):
            if maze[i][j] ==1:
                sense.set_pixel(j,i,orange)
    sense.set_pixel(y,x,green)
    time.sleep(2)
    
    c = BluetoothServer(None)
    
    
    while True:
        t=dire
        x,y,dire=next(sol,x,y,dire)
        if t==dire:
            c.send("forward")
        elif t=="up":
            if dire=="left":
                c.send("left")
            else:
                c.send("right")
        elif t=="right":
            if dire=="up":
                c.send("left")
            else:
                c.send("right")
        elif t=="left":
            if dire=="down":
                c.send("left")
            else:
                c.send("right")
        else:
            if dire=="right":
                c.send("left")
            else:
                c.send("right")
        sleep(2)
            
        if x==7 and y==7:
            
            break
    time.sleep(5)
    sense.clear()