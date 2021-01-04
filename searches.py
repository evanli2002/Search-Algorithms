def main():
    #generates maze (# = wall, S = start, E = end)
    maze = []
    maze.append(["#", "#", "#", "#", "#", "S", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "E", "#", "#", "#"])

    greedy_best(maze)

"""
SEARCH FUNCTIONS
"""
#depth first search
def depth_first(maze, visited = [], queue = [(0, 5)], moves = 0):
    #check if the queue is empty
    if len(queue) == 0:
        print("No solution")
        return False

    else:
        #remove the last point in the queue and add it to the list of visited points. Also, add 1 to moves
        current = queue.pop()
        visited.append(current)
        moves += 1
        
        #check if the point is the target
        if maze[current[0]][current[1]] == "E":
            #If it is, draw a path from the start to the end by looping through visited in reverse
            path_done = False
            path_cost = 0
            previous = visited[-1]
            for i in range(len(visited) - 2, 0, -1):
                if visited[i] in get_neighbours(maze, previous):
                    maze[visited[i][0]][visited[i][1]] = "."
                    path_cost += 1
                    previous = visited[i]

                    for neighbour in get_neighbours(maze, visited[i]):
                        if maze[neighbour[0]][neighbour[1]] == "S":
                            path_done = True
                            print(f"Solution found in {moves - 1} moves. Path Cost: {path_cost + 1}")
                            print_maze(maze)
                            break
            
                else:
                    maze[visited[i][0]][visited[i][1]] = "x"

                if path_done:
                    break

        #otherwise, add neighbouring points to the queue and recursively call the function
        else:
            for neighbour in get_neighbours(maze, current):
                
                if neighbour not in visited:
                    queue.append(neighbour)
            
            depth_first(maze, visited, queue, moves)

#breadth first search
def breadth_first(maze, visited = [], queue = [(0, 5)], moves = 0):
    #check if the queue is empty
    if len(queue) == 0:
        print("No solution")
        return False
    
    else:
        #remove the first point in the queue and add it to the list of visited points. Also, adds 1 to moves
        current = queue.pop(0)
        visited.append(current)
        moves += 1

        #check if the point is the target
        if maze[current[0]][current[1]] == "E":
            #If it is, draw a path from the start to the end by looping through visited in reverse
            path_done = False
            path_cost = 0
            previous = visited[-1]
            for i in range(len(visited) - 2, 0, -1):
                if visited[i] in get_neighbours(maze, previous):
                    maze[visited[i][0]][visited[i][1]] = "."
                    path_cost += 1
                    previous = visited[i]

                    for neighbour in get_neighbours(maze, visited[i]):
                        if maze[neighbour[0]][neighbour[1]] == "S":
                            path_done = True
                            print(f"Solution found in {moves - 1} moves. Path Cost: {path_cost + 1}")
                            print_maze(maze)
                            break
                
                else:
                    maze[visited[i][0]][visited[i][1]] = "x"

                if path_done:
                    break

        #otherwise, add neighbouring points to the queue and recursively call the function
        else:
            for neighbour in get_neighbours(maze, current):
                
                if neighbour not in visited:
                    queue.append(neighbour)
            
            breadth_first(maze, visited, queue, moves)
            
#greedy best search
def greedy_best(maze, visited = [], queue = [(0, 5)], moves = 0):
    #check if the queue is empty
    if len(queue) == 0:
        print("No solution")
        return False
    
    else:
        #remove the last point in the queue and add it to the list of visited points. Also, adds 1 to moves
        current = queue.pop()
        visited.append(current)
        moves += 1

        #check if the point is the target
        if maze[current[0]][current[1]] == "E":
            #If it is, draw a path from the start to the end by looping through visited in reverse
            path_done = False
            path_cost = 0
            previous = visited[-1]
            for i in range(len(visited) - 2, 0, -1):
                if visited[i] in get_neighbours(maze, previous):
                    maze[visited[i][0]][visited[i][1]] = "."
                    path_cost += 1
                    previous = visited[i]

                    for neighbour in get_neighbours(maze, visited[i]):
                        if maze[neighbour[0]][neighbour[1]] == "S":
                            path_done = True
                            print(f"Solution found in {moves - 1} moves. Path Cost: {path_cost + 1}")
                            print_maze(maze)
                            break
                
                else:
                    maze[visited[i][0]][visited[i][1]] = "x"
                
                if path_done:
                    break

        #otherwise, add neighbouring points to the queue based on Manhattan Distance and recursively call the function
        else:
            neighbours = []
            for neighbour in get_neighbours(maze, current):
                
                if neighbour not in visited:
                    neighbours.append(neighbour)
            
            #if there is only one neighbour, we must move there
            if len(neighbours) == 1:
                queue.append(neighbours[0])
            
            #if there are two neighbours, append in the order [larger MD, smaller MD]
            elif len(neighbours) == 2:
                if manhattan_distance(neighbours[0]) > manhattan_distance(neighbours[1]):
                    queue.append(neighbours[0])
                    queue.append(neighbours[1])
                else:
                    queue.append(neighbours[1])
                    queue.append(neighbours[0])
            
            #if there are three neighbours, append in the order [largest MD, middle MD, smallest MD]
            elif len(neighbours) == 3:
                d1 = manhattan_distance(neighbours[0])
                d2 = manhattan_distance(neighbours[1])
                d3 = manhattan_distance(neighbours[2])

                if d1 >= d2 >= d3:
                    queue.append(neighbours[0])
                    queue.append(neighbours[1])
                    queue.append(neighbours[2])
                elif d1 >= d3 >= d2:
                    queue.append(neighbours[0])
                    queue.append(neighbours[2])
                    queue.append(neighbours[1])
                elif d2 >= d1 >= d3:
                    queue.append(neighbours[1])
                    queue.append(neighbours[0])
                    queue.append(neighbours[2])
                elif d2 >= d3 >= d1:
                    queue.append(neighbours[1])
                    queue.append(neighbours[2])
                    queue.append(neighbours[0])
                elif d3 >= d1 >= d2:
                    queue.append(neighbours[2])
                    queue.append(neighbours[0])
                    queue.append(neighbours[1])
                elif d3 >= d2 >= d1:
                    queue.append(neighbours[2])
                    queue.append(neighbours[1])
                    queue.append(neighbours[0])
            
            greedy_best(maze, visited, queue, moves)

    
if __name__ == "__main__":
    main()
