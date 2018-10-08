import time
import heapq
import math

class MazeLoader:
    def __init__(self):
        pass

    # Returns maze as an array
    def loadMaze(path):
        maze = []
        line_num = 0
        maze_file = open(path, "r")
        for line in maze_file:
            maze.append([])
            for char in line:
                if(char != ',' and char != '\n'):
                    maze[line_num].append(char)
            line_num += 1

        print("---------- Loaded Maze -----------")
        MazeLoader.printMaze(maze)

        return maze

    # Prints the maze better than the built in print function
    def printMaze(maze):
        # Slows print down to make it viewable
        time.sleep(0.5)
        for line in maze:
            for space in line:
                print(space, end='')
            print()

# Base class for search functions
class Search:
    def __init__(self, maze):
        self.path = []
        self.unexploredPaths = []
        self.maze = maze
        self.pos = Search.findChar(self.maze, 'P')
        visited = []

    # Returns the first occurence the character
    def findChar(maze, char):
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if(maze[i][j] == char):
                    return [i,j]

    # This function searches for the  goal
    def search(self):
        pass

    # Takes either an array or singe char and returns all occurrences
    # of characters close within a step as an array of maze positions
    def getDirs(self, chars):
        dirs = []
        up = [self.pos[0] - 1, self.pos[1]]
        down = [self.pos[0] + 1, self.pos[1]]
        left = [self.pos[0], self.pos[1] - 1]
        right = [self.pos[0], self.pos[1] + 1]
        for newPos in [up, down, left, right]:
            for char in chars:
                if(self.maze[newPos[0]][newPos[1]] == char):
                    dirs.append(newPos)

        return dirs

    # Steps back to the intersection near path, removing dots
    def backTrace(self, path):
        while(self.getDirs(['.', '*', ' ']).count(path) != 1):
            self.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = self.path.pop()


    # Step to nearest crossing, leaving dots. Returns '*' when found
    def traceToXing(self):
        dirs = self.getDirs([' ', '*'])
        while(len(dirs) == 1):
            if(self.unexploredPaths.count(self.pos) != 0):
                self.unexploredPaths.remove(self.pos)

            if(self.maze[self.pos[0]][self.pos[1]] == '*'):
                return '*'

            self.maze[self.pos[0]][self.pos[1]] = '.'
            self.path.append(self.pos)
            self.pos = dirs[0]
            

            MazeLoader.printMaze(self.maze)

            dirs = self.getDirs([' ', '*'])

        self.path.append(self.pos)
        # Check for goal on dead ends and intersections
        if(self.maze[self.pos[0]][self.pos[1]] == '*'):
            return '*'
        # returns % if there is a dead end
        elif(len(dirs) < 1):
            return '%'
        # returns ' ' if there is another intersection
        elif(len(dirs) > 1):
            return ' '




class DFS(Search):

    def search(self):
        pathResult = self.traceToXing()

        while(pathResult != '*'):

            # Handle dead ends
            if(pathResult == '%'):
                nextPath = self.unexploredPaths.pop()
                self.backTrace(nextPath)
                self.pos = nextPath
            # Handle intersections
            elif(pathResult == ' '):
                self.maze[self.pos[0]][self.pos[1]] = '.'
                self.path.append(self.pos)
                openDirs = self.getDirs([' ', '*'])
                self.pos = openDirs.pop()

                # Put the rest of possible directions in a stack
                for path in openDirs:
                    self.unexploredPaths.append(path)


            pathResult = self.traceToXing()

        print("Goal found")

class BFS(Search):
    visited = []
    
    def search(self):    
        pathResult = self.traceToXing()

        while(pathResult != '*'):
            
            if(pathResult == '%'):
                paths = self.getDirs([' ', '*'])
                
    

class AStar(Search):
    goalPos = []

    def calcDistToGoal(self, spot):
        dist = abs(spot[0] - self.goalPos[0]) + abs(spot[1] - self.goalPos[1])
        return dist

    def search(self):
        self.goalPos = Search.findChar(self.maze, '*')
        pathResult = self.traceToXing()

        while(pathResult != '*'):

            # Handle dead ends
            if(pathResult == '%'):
                nextPath = self.unexploredPaths.pop()
                self.backTrace(nextPath)
                self.pos = nextPath
            # Handle intersections
            elif(pathResult == ' '):
                self.maze[self.pos[0]][self.pos[1]] = '.'
                self.path.append(self.pos)
                openDirs = self.getDirs([' ', '*'])

                openDirs.sort(key = lambda x: self.calcDistToGoal(x))

                self.pos = openDirs.pop()

                openDirs.reverse()
                # Put the rest of possible directions in a stack
                for path in openDirs:
                    self.unexploredPaths.append(path)


            pathResult = self.traceToXing()

        print("Goal found")

s = AStar(MazeLoader.loadMaze("../A1/mazes/large_maze.txt"))
s.search()
