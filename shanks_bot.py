# Shanksbot

def find(element, li):
    count = 1
    for i in li:
        if i == element:
            return count
        else:
            count += 1

def quotient(a, b):
    return int(a/b)

def div(n, d):
    integer = quotient(n, d)
    rem = n - d*quotient(n, d)
    
    if rem == 0:
        done = True
    else:
        done = False
        
    li_rem = []
    
    while done == False:
        val = quotient(rem*10, d)
        rem = (rem*10) - d*quotient(rem*10, d)
        
        if rem in li_rem:
            done = True
            repeat = len(li_rem) - find(rem, li_rem) + 1
        else:
            li_rem.append(rem)
    
    return repeat

print(div(1, 60013))
