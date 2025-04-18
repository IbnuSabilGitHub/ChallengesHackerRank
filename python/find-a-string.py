strings = "ABCDCDC"
substring = "CDC"
count = 0
for i in range(len(strings) - len(substring) + 1):
    if strings[i:i+len(substring)] == substring:
        count += 1
        
    