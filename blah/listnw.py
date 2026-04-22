list=["apple", "banana", "cherry", "date", "strawberry"]
print(*list)
list[0]="mango"
print(*list)
list.append("kiwi")
print(*list)
list.pop(4)
print(*list)