def permutations(remaining, candidate=''):
 
    if len(remaining) == 0:
        print(candidate)
 
    for i in range(len(remaining)):
 
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i+1:]
 
        permutations(newRemaining, newCandidate)


        
# def printPermutations(string):
#     #Implement Your Code Here
#     pass

s = input()
permutations(s)
 
