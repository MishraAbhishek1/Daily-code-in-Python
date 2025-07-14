# ✅ Example 2: Loop inside **kwargs

def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_profile(name="abhsihek")        
