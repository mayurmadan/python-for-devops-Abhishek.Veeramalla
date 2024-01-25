#break statement.
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    #stop when reach 3, print only 1 & 2
    if number == 3:
        break
    print(number)

#continue statement.
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    #here it skip the number 3 print else from list
    if number == 3:
        continue
    print(number)    
