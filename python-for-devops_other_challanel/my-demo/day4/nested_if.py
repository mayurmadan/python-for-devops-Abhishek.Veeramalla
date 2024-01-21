#In programming, "nested" refers to something being placed inside another thing. It's like putting one thing inside another like a set of nesting dolls.
#In code, it often refers to structures like nested loops or nested if statements. Imagine you have a loop (a repetitive action), and inside that loop, you have another loop. That's a nested loop. Similarly, if you have a condition (an if statement), and inside that condition, you have another condition, that's a nested if statement
age = 23
height = 6
if height > 5.9:
    if age <=22:
    #if both if and netsed if true
        print("you are eligible for post without fund")
    #if first if is true and nested if is false
    else:
        print("you are eligibale for post with fund")
#if first if is false, not look into netsed if, and print below
else:
    print("you are not eligibale")
print("finished")

x = 10
y = 5
if x > y:
    if x > 15:
        print("x is greater than 15")
    else:
        print("x is not grerter than 15")
else:
    print("x is not greater than y")
