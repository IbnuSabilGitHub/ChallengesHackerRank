

if __name__ == '__main__':
    item = []
    listInputs = []
    N = int(input())
    for line in range(0,N):
        inputs = input()
        listInputs.append(inputs)
    
    for items in listInputs:
        lists = items.split()
        if lists[0] == "print":
            print(item)
        elif lists[0] == "insert":
            index = int(lists[1])
            value = int(lists[2])
            item.insert(index, value)
        elif lists[0] == "remove":
            value = int(lists[1])
            item.remove(value)
        elif lists[0] == "append":
            value = int(lists[1])
            item.append(value)
        elif lists[0] == "sort":
            item.sort()
        elif lists[0] == "pop":
            item.pop()
        elif lists[0] == "reverse":
            item.reverse()
        
