def permutations(str):
    if len(str) == 0:
        return 
    
    output = []
    for i in range(len(str)):
        
        start = str[i]
        
        remaining = str[:i] + str[i+1:]        
        permutations(remaining)
        output.append(start + remaining)
        
        next1 = remaining[::-1]
        permutations(next1)
        output.append(start + next1 )
        
    return output
import itertools
str = input()
x = list(itertools.permutations(str))
for i in x:
    for j in i:
        print(j, end ="")
    print()






