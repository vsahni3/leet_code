def generate_parentheses(n):
    combos = set()
    def recurse(cur='', counter1=0, counter2=0):
        if counter1 == counter2 == n:
            combos.add(cur)
        if counter1 < n:
            recurse(cur + '(', counter1+1, counter2)
        if counter2 < counter1:
            recurse(cur + ')', counter1, counter2+1)
    recurse()
    return combos

print(generate_parentheses(3)) 


        

        
