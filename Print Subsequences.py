def printSub(s , o):
    if len(s) == 0:
        print(o)
        return
    
    #dont include 0th char 
    printSub(s[1:],o)
    
    #include 0th char 
    newOutput = o + s[0]
    printSub (s[1:] , newOutput)
s = input()
printSub(s,"" )
