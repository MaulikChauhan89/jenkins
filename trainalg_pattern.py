
def pattern(n): 
    myList = [] 
    for i in range(1,n+1): 
        myList.append("*"*i) 
    print("\n".join(myList)) 
  
# Driver Code 
n = 5
pattern(n) 
print("--------------------------------------------")
print("@@@@--------------------Again-------------------@@@@")
print("--------------------------------------------")
pattern(n) 
