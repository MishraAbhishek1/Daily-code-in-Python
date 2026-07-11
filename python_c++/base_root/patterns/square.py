# print the square nnumebr having  a n= 4 value

# 1234
# 1234
# 1234

def square_patterns(n):
    
    for i in range(0, n+1):
        for j in range(0, n+1):
            print(j,end=" ")
        print()

square_patterns(4)
