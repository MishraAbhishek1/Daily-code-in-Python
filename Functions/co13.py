# ✅ **kwargs → Multiple Keyword Arguments
def profile(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key}: {value}")
profile(name = "Abhishek", age=30, city="Delhi")        