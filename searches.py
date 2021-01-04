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
