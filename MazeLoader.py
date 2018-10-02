class MazeLoader:
    def __init__(self):
        MazeLoader.loadMaze("../A1/mazes/medium_maze.txt")

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

        MazeLoader.printMaze(maze)

    def printMaze(maze):
        for line in maze:
            for space in line:
                print(space, end='')
            print()

m = MazeLoader()
