import sys
def tidy(g):
    height = 0
    for i in range(len(g)):
        width = 0
        for j in range(len(g)):
            if grid[i][j]:
                width = j
            else:
                break

def move(g, p, bounds):
    i, j = p

    if bounds:
        i_min, i_max, j_min, j_max = bounds

    if all(g[i - 1]):
        if bounds:
            if i_min < i + 1 <= i_max:
                return (1, 0)
        else:
            return (1, 0)

    if all(g[i + 1]):
        if bounds:
            if i_min < i - 1 <= i_max:
                return (-1, 0)
        else:
            return (-1, 0)

    if all(g[x][j + 1] for x  in range(len(g))):
        if bounds:
            if j_min < j - 1 <= j_max:
                return (0, -1)
        else:
            return (0, -1)

    if all(g[x][j - 1] for x  in range(len(g))):
        if bounds:
            if j_min < j + 1 <= j_max:
                return (0, 1)
        else:
            return (0, 1)

    return (0, 0)

def deploy(p):
    i, j = p
    print(i, j)
    return map(int, input().split())

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        grid = [[False for i in range(1000)] for j in range(1000)]
        a = int(input())
        
        p = (500, 500)
        i_min, i_max, j_min, j_max = 0, 0, 0, 0
        d = 0

        for _ in range(1000):
            i, j = deploy(p)
            if i == 0 and j == 0:
                break

            i_min = min(i_min, i)
            j_min = min(j_min, j)
            i_max = max(i_max, i)
            j_max = max(j_max, j)

            area = (i_max - i_min) * (j_max - j_min)

            if area >= a:
                bounds = i_min, i_max, j_min, j_max 
            else:
                bounds = None

            grid[i][j] = True
            di, dj = move(grid, p, bounds)
            while di != 0 and dj != 0 :
                i += di
                j += dj
                di, dj = move(grid, (i, j), bounds)

            grid_str = ""
            for r in grid:
                if any(r):
                    for c in r:
                        grid_str += "*" if c else ""
                    grid_str += "\n"
            print(grid_str, file=sys.stderr)

            p = (i, j)
                
            
        



