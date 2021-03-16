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

L2 = swap(L, int(input(" n1 -> ")), int(input(" n2 -> ")))

print("After Swap: ", L1)
print("After Swap: ", L2)


def getdata(N, funcobj):
    return funcobj(N)

N = list(range(10))

print("MAXIMUM : ", getdata(N, max))
print("MINIMUM : ", getdata(N, min))
