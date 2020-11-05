def edge(crd):
    return crd in [1, 8]


c1, c2 = int(input()), int(input())
if edge(c1) and edge(c2):
    print(3)
elif edge(c1) or edge(c2):
    print(5)
else:
    print(8)
