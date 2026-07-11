# * * * * *
# * * * * *
# * * * * *
# * * * * *

def square_star_patterns(n):
    
    for i in range(0, n+1):
        
        for j in range(0, n+1):
            
            print("*", end=" ")
            
        print()

square_star_patterns(5)