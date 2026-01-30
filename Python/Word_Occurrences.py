file = open("DemoFile.txt", "r")

text = file.read()
file.close()

words = text.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
