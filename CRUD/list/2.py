arr = [1,2,3,4,5]
print(len(arr))

# print(arr)

# for i in range(len(arr)):
#     print(arr[i])

# for item in range(arr):
#     print(item, arr[item])

# here we use a enumerate funciton 
for iteration, value in enumerate(arr):
    print(iteration, value)