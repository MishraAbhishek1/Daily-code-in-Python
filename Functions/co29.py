# Access and Modify Python Global Variable

# global variables

network_code = "ABC123"

def modify_network_code():

    # print("Original Network Code: ", network_code)
    global network_code
    # here i access a global Varaibles and i modify it
    network_code = "XYZ789"
    print("Modified Network Code: ", network_code)

modify_network_code()

print("Final Network Code: ", network_code)