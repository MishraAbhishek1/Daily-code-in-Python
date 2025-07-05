# Kwargs Example >>
def print_info(**kwargs):
    # kwargs means Keyword Arguments
    print(kwargs)
print_info(name="Abhishek", age = 22, roll_no = 23242)    


# another example of kwargs>
def Home(**kwargs):
    print(kwargs)

x = Home(plot_no = 8979869, plot_height= 9798)
x