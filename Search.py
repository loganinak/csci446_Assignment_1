from collections import deque
import heapq
import mazes


class Search:
    def __init__(self, maze):
        self.px = 0
        self.py = 0
        self.fx = 0
        self.fy = 0
        self.maze = maze
        #figure out pacmans start and end places
        for i, row in enumerate(self.maze):
            for j, element in enumerate(row):
                if element.value is 'P':
                    self.px = i
                    self.py = j
                elif element.value is '*':
                    self.fx = i
                    self.fy = j

    def BFS(self, currentNode, finish, moves):
       #create queue, visitedNodes needs to be reset
       queue = deque([currentNode])
       visitedNodes = []

       while len(queue) > 0:
          node = queue.pop()
          if node in visitedNodes:
             continue

          visitedNodes.append(node)
          if node.value == finish:
              self.printResults("Breadth First Search: ", node, moves)
              return True
          moves += 1
          for neighbor in node.neighbors:
             if neighbor not in visitedNodes and neighbor.value is not '%':
                neighbor.previous = node
                queue.appendleft(neighbor)
       return False

    def DFS(self, currentNode, finish, moves):
       #create queue, visitedNodes needs to be reset
       queue = deque([currentNode])
       visitedNodes = []

       while len(queue) > 0:
          node = queue.pop()
          if node in visitedNodes:
             continue

          visitedNodes.append(node)
          if node.value == finish:
              self.printResults("Depth First Search: ", node, moves)
              return True
          moves += 1
          for neighbor in node.neighbors:
             if neighbor not in visitedNodes and neighbor.value is not '%':
                neighbor.previous = node
                queue.append(neighbor)

       return False

    def GREEDY(self,currentNode, finish, moves):
        #create heap queue for priority
        queue = []
        visitedNodes = []
        heapq.heapify(queue)
        #variable to always give unique identifiers to (priority, node) tuple
        task = 0
        heapq.heappush(queue, (0, task, currentNode))
        task += 1

        while len(queue) > 0:
            node = heapq.heappop(queue)[2]

            if node.value == finish:
                self.printResults("Greedy Search: ", node, moves)
                return True

            visitedNodes.append(node)
            moves += 1
            for neighbor in node.neighbors:
                if neighbor not in visitedNodes and neighbor.value is not '%':
                    neighbor.previous = node
                    heapq.heappush(queue, (self.manhattanDistance(neighbor, self.fx, self.fy), task, neighbor))
                    task += 1
        return False

    def ASTAR(self,currentNode, finish, moves):
        #create heap queue for priority
        queue = []
        visitedNodes = []
        heapq.heapify(queue)
        #variable to always give unique identifiers to (priority, node) tuple
        task = 0
        heapq.heappush(queue, (0, task, currentNode))
        task += 1

        while len(queue) > 0:
            node = heapq.heappop(queue)[2]

            if node.value == finish:
                self.printResults("A* Search: ", node, moves)
                return True

            visitedNodes.append(node)
            moves += 1
            for neighbor in node.neighbors:
                if neighbor not in visitedNodes and neighbor.value is not '%':
                    neighbor.previous = node
                    heapq.heappush(queue, (self.manhattanDistance(node, self.px, self.py) + self.manhattanDistance(neighbor, self.fx, self.fy), task, neighbor))
                    task += 1
        return False
    

    def manhattanDistance(self, currentNode, x, y):
        return abs(currentNode.x - x) + abs(currentNode.y - y)

    def printResults(self, search, currentNode, cost):

        #print path
        node = currentNode
        steps = 0
        while node.previous is not None:
            if node.value is not 'P' and node.value is not '*':
                steps += 1
                node.value = '.'
            node = node.previous

        print("{} \nCost: {}, Steps {}".format(search, cost, steps))
        print("Solved Maze:")
        mazes.printMaze(self.maze)

        #clean maze
        node = currentNode
        while node.previous is not None:
            if node.value is not 'P' and node.value is not '*':
                node.value = ' '

            node = node.previous
if __name__=='__main__':
    #create mazes
    open_maze = mazes.readMaze("mazes/open_maze.txt")
    medium_maze = mazes.readMaze("mazes/medium_maze.txt")
    large_maze = mazes.readMaze("mazes/large_maze.txt")

    moves = 0

    open_search = Search(open_maze)
    # open_search.DFS(open_search.maze[open_search.px][open_search.py],'*', moves)
    # open_search.BFS(open_search.maze[open_search.px][open_search.py],'*', moves)
    # open_search.GREEDY(open_search.maze[open_search.px][open_search.py], '*', moves)

    mediumSearch = Search(medium_maze)
    mediumSearch.DFS(mediumSearch.maze[mediumSearch.px][mediumSearch.py],'*', moves)
    mediumSearch.BFS(mediumSearch.maze[mediumSearch.px][mediumSearch.py],'*', moves)
    mediumSearch.GREEDY(mediumSearch.maze[mediumSearch.px][mediumSearch.py], '*', moves)
    mediumSearch.ASTAR(mediumSearch.maze[mediumSearch.px][mediumSearch.py], '*', moves)

    #large_search = Search(large_maze)
    #large_search.BFS(large_search.maze[large_search.px][large_search.py], '*', moves)
    #large_search.GREEDY(large_search.maze[large_search.px][large_search.py], '*', moves)
