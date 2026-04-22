list=[1, 2, 3, 4, 5]
print(*list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
list[2]=11
print(*list)
list[0:2]=[4,5]
print(*list)
list.append(9)
print(*list)
list.pop()
print(*list)
list.remove(5)
print(*list)