import time

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
        self.maze = maze
        self.pos = Search.findChar(self.maze, 'P')

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

    # Steps back to the nearest intersection, removing dots
    def backTrace(self):
        dirs = self.getDirs('.')
        # handle running into other paths
        if(len(dirs) == 2):
            temp = self.pos
            self.pos = dirs[0]
            numPaths = len(self.getDirs([' ', '*', '.']))
            self.pos = dirs[1]
            if(numPaths > len(self.getDirs([' ', '*', '.']))):
                self.pos = dirs[1]
                dirs = self.getDirs('.')
            else:
                self.pos = dirs[0]
                dirs = self.getDirs('.')

        while(len(dirs) == 1):
            openSpaces = self.getDirs(' ')
            if(len(openSpaces) < 2):
                self.maze[self.pos[0]][self.pos[1]] = ' '
                self.pos = dirs[0]
            else:
                break

            MazeLoader.printMaze(self.maze)

            dirs = self.getDirs('.')

    # Step to nearest crossing, leaving dots. Returns '*' when found
    def traceToXing(self):
        dirs = self.getDirs([' ', '*'])
        while(len(dirs) == 1):
            

            if(self.maze[self.pos[0]][self.pos[1]] == '*'):
                return '*'

            self.maze[self.pos[0]][self.pos[1]] = '.'
            self.pos = dirs[0]

            MazeLoader.printMaze(self.maze)

            dirs = self.getDirs([' ', '*'])

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
    unexploredPaths = []

    def search(self):
        pathResult = self.traceToXing()

        while(pathResult != '*'):

            # Handle dead ends
            if(pathResult == '%'):
                paths = self.getDirs([' ', '*'])
                for path in paths:
                    if(self.unexploredPaths.count(path) != 0):
                        self.unexploredPaths.remove(path)

                self.backTrace()
                paths = self.getDirs([' ', '*'])

                nextPath = self.unexploredPaths.pop()
                while(paths.count(nextPath) != 1):
                    self.maze[self.pos[0]][self.pos[1]] = ' '
                    self.pos = self.getDirs(['.']).pop()
                    self.backTrace()
                    paths = self.getDirs([' ', '*'])
                    for path in paths:
                        if(self.unexploredPaths.count(path) != 0):
                            self.unexploredPaths.remove(path)

                self.pos = nextPath
            # Handle intersections
            elif(pathResult == ' '):
                self.maze[self.pos[0]][self.pos[1]] = '.'
                openDirs = self.getDirs([' ', '*'])
                self.pos = openDirs.pop()

                # Put the rest of possible directions in a stack
                for path in openDirs:
                    self.unexploredPaths.append(path)


            pathResult = self.traceToXing()

        print("Goal found")

s = DFS(MazeLoader.loadMaze("../A1/mazes/large_maze.txt"))
s.search()
