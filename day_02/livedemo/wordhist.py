path1 = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\whist.txt", "w")
path2 = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\data.txt", "r")


# Read the source
content = path2.read()
path2.close()

# Split the content
words = content.split()

# Build the dictionary
D = {}
for word in words:
    if word in D.keys():
        D[word] = D[word] + 1
    else:
        D[word] = 1

# Write the report to file
path1.write("WORD HISTOGRAM REPORT\n\n")
path1.write("--------------------------------------- \n\n")
for key in D.keys():
    path1.write(str(key).ljust(10) + ' -> ' + str(D[key]).ljust(5) + '\n')
path1.close()
