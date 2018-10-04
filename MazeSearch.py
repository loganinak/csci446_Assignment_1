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

    # Takes either an array or singe char and returns all occurrences of characters close within  a step
    def getDirs(self, chars):
        dirs = []
        print(self.pos)
        up = [self.pos[0] - 1, self.pos[1]]
        down = [self.pos[0] + 1, self.pos[1]]
        left = [self.pos[0], self.pos[1] - 1]
        right = [self.pos[0], self.pos[1] + 1]
        for newPos in [up, down, left, right]:
            for char in chars:
                if(self.maze[newPos[0]][newPos[1]] == char):
                    dirs.append(newPos)

        return dirs

    # Steps back to the nearest intersection, then jumps to point
    def backTrace(self):
        dirs = self.getDirs('.')
        while(len(dirs) == 1):
            if(len(dirs) == 1):
                self.maze[self.pos[0]][self.pos[1]] = ' '
                self.pos = dirs

            dirs = self.getDirs('.')


class DFS(Search):
    unexploredPaths = []

    def search(self):
        notDone = True

        while(notDone):
            openDirs = self.getDirs([' ', '*'])

            if(len(openDirs) == 1):
                self.maze[self.pos[0]][self.pos[1]] = '.'
                self.pos = openDirs.pop()
            elif (len(openDirs) > 1):
                self.maze[self.pos[0]][self.pos[1]] = '.'
                self.pos = openDirs.pop()

                # Put the rest of possible directions in a stack
                for _ in openDirs:
                    self.unexploredPaths.append(openDirs.pop())

            if(len(self.getDirs([' ', '*'])) == 0):
                self.backTrace()
                self.pos = unexploredPaths.pop()

            MazeLoader.printMaze(self.maze)

s = DFS(MazeLoader.loadMaze("../A1/mazes/medium_maze.txt"))
s.search()
