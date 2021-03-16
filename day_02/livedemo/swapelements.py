def swap(col, x, y):
    if(type(col) is list):
        temp = col[x]
        #print("temp  : ", temp)
        col[x] = col[y]
        #print("col[x]: ", col[x])
        col[y] = temp
        #print("col[y]: ", col[y])
        #print ("swap : ",col)
        return col
    else:
        return -1



L = ["red", "green", "blue", "yellow", "orange", "brown"]
print("Original : ", L)

# L.swap(1, 3)     # oop BASED
L1 = swap(L, 1, 3)    # non-oop BASED

print("After Swap: ", L1)

