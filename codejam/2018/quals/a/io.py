def swaps_small(d, p):
    i = p.find("C")
    if i >= 0:
        ni = 2 * (len(p) - 1) - d
        if 0 <= ni < len(p):
            return abs(ni - i)
        else:
            #print(ni)
            return "IMPOSSIBLE"
    else:
        return 0 if d <= len(p) else "IMPOSSIBLE"

def damage(p):
    total = 0
    d = 1
    for c in p:
        if c == "S":
            total += d
        elif c == "C":
            d *= 2
    return total

def swap(p):
    i = p.rfind("CS")
    if i >= 0:
        l = list(p)
        l[i], l[i+1] = l[i+1], l[i]
        return "".join(l)
        
    return "IMPOSSIBLE"

    
def naive(d, p):
    total = damage(p)
    swaps = 0
    while total > d:
        p = swap(p)
        if p == "IMPOSSIBLE":
            return p
        swaps += 1
        total = damage(p)
    return swaps

def print_cases(func):
    for i in range(1, int(input())+1):
        c, p = input().split()
        output = func(int(c), p)
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(naive)

