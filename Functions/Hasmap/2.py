mp = {}

mp["name"] = "chini"
mp["age"] = 17
mp["branch"] = "CSE"

# print(mp)

# if "name" in mp:
#     print("Key is present in the Hashmap")
# else:
#     print("Key is not present in the Hashmap")
    
# # applying a loop to print all the keys only first

# for key in mp:
#     print(key)

# # pplting for loop to print all the values only first
# for value in mp.values():
#     print(value)
    
# # now wed applying a lopp and gget all key and values together
# for key, value in mp.items():
#     print(key, value)
    

# here we appllying a funtion and   i make a fucniton in this fuction i will passs a mp and i will print all the keys and values

def has_map(mp):
    for key, value in mp.items():
        return key, value
print(has_map())