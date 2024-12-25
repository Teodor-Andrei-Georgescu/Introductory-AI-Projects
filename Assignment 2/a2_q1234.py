TRUTH_VALUES = ['O', 'Z', 'U']
AND_TABLE = {
    ('O', 'O'): 'O', 
    ('O', 'Z'): 'Z', 
    ('O', 'U'): 'O', 
    ('Z', 'O'): 'Z', 
    ('Z', 'Z'): 'Z', 
    ('Z', 'U'): 'Z', 
    ('U', 'O'): 'O', 
    ('U', 'Z'): 'Z', 
    ('U', 'U'): 'U'
    }
OR_TABLE = {
    ('O', 'O'): 'O', 
    ('O', 'Z'): 'O', 
    ('O', 'U'): 'U', 
    ('Z', 'O'): 'O', 
    ('Z', 'Z'): 'Z', 
    ('Z', 'U'): 'U', 
    ('U', 'O'): 'U', 
    ('U', 'Z'): 'U', 
    ('U', 'U'): 'U'
    }
NEGATION_TABLE = {
    'O': 'Z', 
    'Z': 'O', 
    'U': 'U'
    }

# CSC421 ASSIGNMENT 2 - QUESTION 1

def evaluate(s):
    # Split the input and handle basic prefix logic for two operands
    tokens = s.strip().split()
    
    operator, operand1, operand2 = tokens

    if operator == '&':
        return AND_TABLE[(operand1, operand2)]
    elif operator == '|':
        return OR_TABLE[(operand1, operand2)]

# examples
e1_1 = "& Z O"
e1_2 = "| O O"
e1_3 = "| Z Z"
e1_4 = "& U U"
e1_5 = "& U Z"

res_e1_1 = evaluate(e1_1)
res_e1_2 = evaluate(e1_2)
res_e1_3 = evaluate(e1_3)


print(f'{e1_1} = {res_e1_1}')
print(f'{e1_2} = {res_e1_2}')
print(f'{e1_3} = {res_e1_3}')


# CSC421 ASSIGNMENT 2 - QUESTION 2

d = {'foo': "Z", 'b': "O"}
print(d)
e2_1 = '& Z O'
e2_2 = '& foo O'
e2_3 = '& foo b'

def evaluate_with_bindings(s,d):
    tokens = s.strip().split()

    operator, operand1, operand2 = tokens

    # Resolve variables from bindings if present
    operand1 = d.get(operand1, operand1)
    operand2 = d.get(operand2, operand2)
 
    return evaluate(f"{operator} {operand1} {operand2}")


res_e2_1 = evaluate_with_bindings(e2_1,d)
res_e2_2 = evaluate_with_bindings(e2_2,d)
res_e2_3 = evaluate_with_bindings(e2_3,d)

print(f'{e2_1} = {res_e2_1}')
print(f'{e2_2} = {res_e2_2}')
print(f'{e2_3} = {res_e2_3}')


# CSC421 ASSIGNMENT 2 - QUESTIONS 3,4
#I think sample outputs r wrong
def recursive_eval(l,bindings):
    head, tail = l[0], l[1:]
    #print("head at start = " + head,tail)
    if head in ['&', '|', "~"]: 
        if head == "~":
            val1, tail = recursive_eval(tail, bindings)
            result = NEGATION_TABLE[val1]
            #print(f"~ {val1} = {result}")
            return result,tail
            #return NEGATION_TABLE[val1], tail
        val1, tail = recursive_eval(tail,bindings)
        val2, tail = recursive_eval(tail,bindings)
        
        #print(f"Evaluating: {head} {val1} {val2}")
        if head == '&': 
            result =AND_TABLE[(val1, val2)]
            #return AND_TABLE[(val1, val2)], tail
        elif head == '|':  
            result = OR_TABLE[(val1, val2)]
            #return OR_TABLE[(val1, val2)], tail
        #print(f"{head} {val1} {val2} = {result}")
        return result,tail
    # operator is a number
    else:  
        resolved = bindings.get(head, head)
        #print(f"Resolved '{head}' to '{resolved}'")
        return bindings.get(head, head), tail

def prefix_eval(input_str,bindings): 
    input_list = input_str.split(' ')
    res, tail = recursive_eval(input_list,bindings)
    return res

d = {'a': 'O', 'b': 'Z', 'c': 'U'}
e3_1 = "& a | Z O"
e3_2 = "& O | O b"
e3_3 = "| O & ~ b b"
e3_4 = "& ~ a & O O"
e3_5 = "| O & ~ b c"
e3_6 = "& ~ a & c O"
e3_7 = "& & c c & c c"

print(d)
for e in [e3_1,e3_2,e3_3,e3_4,e3_5,e3_6, e3_7]:
    print("%s \t = %s" % (e, prefix_eval(e,d)))

#print(AND_TABLE[("O","O")])
# EXPECTED OUTPUT
# & Z O = Z
# | O O = Z
#| Z Z = Z
# {'foo': 'Z', 'b': 'O'}
# & Z O = Z
# & foo O = Z
# & foo b = Z
# {'a': 'O', 'b': 'Z', 'c': 'U'}
# & a | Z O        = O
# & O | O b        = O
# | O & ~ b b      = O
# & ~ a & O O      = Z
# | O & ~ b c      = O
# & ~ a & c O      = Z
# & & c c & c c    = U
    




