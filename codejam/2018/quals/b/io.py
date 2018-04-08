import itertools
def trouble_sort(l):
    l = l[::]
    done = False
    while not done:
        done = True
        for i in range(len(l)-2):
            if l[i] > l[i+2]:
                done = False
                l[i], l[i+2] = l[i+2], l[i]
    return l

def fast_trouble_sort(l):
    even = sorted(l[::2])
    odd = sorted(l[1::2])
    return list(itertools.chain(*zip(even, odd)))

def first_invalid(l):
    last = l[0]
    for i in range(1, len(l)):
        if l[i] < last:
            return i - 1
        else:
            last = l[i]
    return "OK"

def search_large(l):
    l = fast_trouble_sort(l)
    return first_invalid(l)

def search_small(l):
    l = trouble_sort(l)
    return first_invalid(l)

def print_cases(func):
    for i in range(1, int(input())+1):
        n = int(input())
        l = list(map(int, input().split()))
        output = func(l)
        print("Case #{}: {}".format(i, output))

def debug_cases(func):
    for i in range(1, int(input())+1):
        n = int(input())
        l = list(map(int, input().split()))
        output = func(l)
        print("Case #{} -> {}\n{}".format(i, output, l))

if __name__ == "__main__":
    print_cases(search_large)

