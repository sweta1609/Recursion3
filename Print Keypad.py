def getstring(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"
    return " "
def printkeypad(n , outputsofar):
    if n == 0:
        print(outputsofar)
        return
    smallNumber = n //10 #23
    lastdigit = n % 10 #4 we will call recursion according to options for 4
    
    optionforlastdigit = getstring(lastdigit)
    for c in optionforlastdigit:
        newoutput =c + outputsofar 
        printkeypad(smallNumber , newoutput)
n = int(input())
printkeypad(n ,"")
    
    
    
