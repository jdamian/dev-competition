# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())

    a = []
    b = []
    while n != 0:
        n, d = divmod(n, 10)
        if d == 4:
            a.append(int(d-1))
            b.append(int(1))
        else:
            a.append(int(d))
            b.append(int(0))
        
    a.reverse()
    b.reverse()

    x = [str(i) for i in a] 
    y = [str(i) for i in b] 

    aa = int("".join(x))
    bb = int("".join(y))

    
    print("Case #{}: {} {}".format(i, aa, bb))
    # check out .format's specification for more formatting options