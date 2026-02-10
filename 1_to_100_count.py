#Counting numbers
def count(n,i=1):
    if(n<i):
        return
    print(i)
    count(n,i+1)
    
    
count(10)
