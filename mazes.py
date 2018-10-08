#Class to read in maze files and print mazes


def readMaze(filename):
    #reads in file
    maze = []
    file = open(filename, "r")
    columns = file.readlines()
    for i, column in enumerate(columns):
        column = column.strip()
        rowNodes = []
        for j, row in enumerate(column):
            for element in row:
                #makes all elements into nodes
                newNode = Node(element, i, j)
                rowNodes.append(newNode)
        maze.append(rowNodes)
    #gives the neighbors of given nodes
    for i, row in enumerate(maze):
        for j, element in enumerate(row):
            if j+1 <= len(row)-1:
                element.neighbors.append(maze[i][j+1])
            if j-1 >= 0:
                element.neighbors.append(maze[i][j-1])
            if i-1 >= 0:
                element.neighbors.append(maze[i-1][j])
            if i+1 <= len(maze)-1:
                element.neighbors.append(maze[i+1][j])      
    return maze

def printMaze(maze):
    for row in maze:
        for element in row:
            print(element.value, end='')
        print('')
        

class Node:
    def __init__(self, val, x, y):
        self.visited = False
        self.value = val
        self.x = x
        self.y = y
        self.neighbors = []
        self.previous = None
        #if this node is a wall
        if val is '%':
            self.visited = True

    def is_visited(self):
        self.visited = True
