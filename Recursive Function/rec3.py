# sum of first n natural Numbers

def sumOF_Numbers(n):
    if n == 0:
        return 0
    return n + sumOF_Numbers(n-1)
print(sumOF_Numbers(10))   