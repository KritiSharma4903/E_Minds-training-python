# f = open("DemoFile.txt")
# print(f.read())


# with open("DemoFile.txt") as f:
#     print(f.read())


# f = open("DemoFile.txt")
# print(f.readline())
# f.close()


# with open("DemoFile.txt") as f:
#     # print(f.read(5))
#     print(f.readline())



# with open("DemoFile.txt")as f:
#     for z in f:
#         print(x)



# --------------------Add content of file

# with open ("DemoFile.txt", "a")as f:
#     f.write("Now the file has more content!")
# with open("DemoFile.txt")as f:
#     print(f.read())



# -------------------------------Delete content of file

# with open("DemoFile.txt","w")as f:
#     f.write("Woops! I have deleted the content!")
# with open("DemoFile.txt")as f:
#     print(f.read())




# -----------------------------------------Delete file

import os
if os.path.exists("testing_file.txt"):
    os.remove("testing_file.txt")
else:
    print("The file does not exist")