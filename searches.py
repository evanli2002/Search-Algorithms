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

if __name__ == "__main__":
    main()
