for i in range(5):
    print(i)
else:
    print("Loop completed without a break.")

##else excute when no break there 
#when there is a break    
for m in range(5):
    if m == 2:
    #here stop at 2, no else excute
        break    
    print("break executed:\n",m)
else:
    print("Loop completed without a break.")

#when there is no break
for x in range(10):
    if x == 11:
        break
    print(x)
else:
    print("completed without break")       
