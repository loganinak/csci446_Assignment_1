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

    # Prints the maze better than the buil in print function
    def printMaze(maze):
        for line in maze:
            for space in line:
                print(space, end='')
            print()

# Base class for search functions
class Search:
    def __init__(self, maze):
        self.maze = maze
        self.startPos = Search.findChar(self.maze, 'P')

    # Returns the first occurence the chararcter
    def findChar(maze, char):
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if(maze[i][j] == char):
                    return [i,j]


s = Search(MazeLoader.loadMaze("../A1/mazes/medium_maze.txt"))
