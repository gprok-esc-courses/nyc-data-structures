

def hanoi_towers(n, source, dest, helper):
    if n == 1:
        print("Move",n,"from",source,"to",dest)
    else:
        hanoi_towers(n-1, source, helper, dest)
        print("Move",n,"from",source,"to",dest)
        hanoi_towers(n-1, helper, dest, source)


hanoi_towers(64, "A", "C", "B")
