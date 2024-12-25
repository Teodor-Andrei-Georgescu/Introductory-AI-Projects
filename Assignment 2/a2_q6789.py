import prolog 

def solve(source, goal_text):
    tokens = prolog.Scanner(source).tokenize()
    rules = prolog.Parser(tokens).parse_rules()
    runtime = prolog.Runtime(rules)
    
    goal = prolog.Parser(prolog.Scanner(goal_text).tokenize()).parse_terms()
    var_args = [a for a in goal.args if isinstance(a,prolog.types.Variable)]
    has_solution = False
    solutions = []
    solutions_vars = [] 
    
    for item in runtime.execute(goal):
        has_solution = True
        solutions.append(item)
        vars = {} 
        for var in var_args:
            vars[var] = str(goal.match(item).get(var))
        solutions_vars.append(vars)
    return (solutions, solutions_vars)


def print_solutions(goal_text, solutions, solutions_vars):
    print("Goal: ", goal_text)
    if len(solutions) == 0:
        print("No solution found") 
    for (s, sv) in zip(solutions, solutions_vars):
        print(s)
        for (k,v) in sv.items():
            print('\t', k, ':',  v) 



source = '''
and_gate(0, 0, 0).
and_gate(0, 1, 0).
and_gate(1, 0, 0).
and_gate(1, 1, 1).

or_gate(0, 0, 0).
or_gate(0, 1, 1).
or_gate(1, 0, 1).
or_gate(1, 1, 1).

not_gate(0, 1).
% not_gate(1, 0).

human(socrates). 
mammal(X) :- human(X). 

circuit(A, B, C, Output) :- 
    and_gate(A, B, AndResult),
    not_gate(C, NotResult),
    or_gate(AndResult, NotResult, Output).
'''
            
# starter goals 
            
goal_text = 'and_gate(0,0,0).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

goal_text = 'and_gate(0,0,1).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

goal_text = 'and_gate(0,0,X).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

goal_text = 'and_gate(0,X,0).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

goal_text = 'mammal(X).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

# Question 6 (single variable) - change goal_text appropriately 

goal_text_q6 = 'or_gate(0, 1, X).'
(solutions_q6, solutions_vars_q6) = solve(source, goal_text_q6) 
print_solutions(goal_text_q6, solutions_q6, solutions_vars_q6)

# Question 7 (two variables) 

goal_text_q7a = 'and_gate(0, Y, X).'
(solutions_q7a, solutions_vars_q7a) = solve(source, goal_text_q7a) 
print_solutions(goal_text_q7a, solutions_q7a, solutions_vars_q7a)

goal_text_q7b = 'and_gate(X, Y, 1).'
(solutions_q7b, solutions_vars_q7b) = solve(source, goal_text_q7b) 
print_solutions(goal_text_q7b, solutions_q7b, solutions_vars_q7b)

# Question 8 
goal_text_q8a = 'circuit(1, 1, 0, Output).'
(solutions_q8a, solutions_vars_q8a) = solve(source, goal_text_q8a) 
print_solutions(goal_text_q8a, solutions_q8a, solutions_vars_q8a)

goal_text_q8b = 'circuit(A, B, C, Output).'
(solutions_q8b, solutions_vars_q8b) = solve(source, goal_text_q8b) 
print_solutions(goal_text_q8b, solutions_q8b, solutions_vars_q8b)

# Question 9 write the source_factory facts and rules 
source_factory = ''' 
produces(advanced_factory, cars).
produces(advanced_factory, airplanes).
produces(advanced_factory, trains).
produces(factory, advanced_factory).
produces(factory, wheels).
produces(factory, engines).
produces(factory, tools).
produces(village, factory).
produces(city, factory).


need(Z, Y) :- produces(Y, Z).

need(X, Y) :- 
    produces(Z, X), 
    need(Z, Y).
'''

goal_text_q9a = 'need(cars, X).'
(solutions_q9a, solutions_vars_q9a) = solve(source_factory, goal_text_q9a) 
print_solutions(goal_text_q9a, solutions_q9a, solutions_vars_q9a)

def tech_needed(product):
    goal_text = f'need({product}, X).'
    (solutions, solutions_vars) = solve(source_factory, goal_text)
    results = []
    for (s, sv) in zip(solutions, solutions_vars):
        for (k,v) in sv.items():
            results.append(v)
    return results

needed_q9b = tech_needed('factory')
needed_q9c = tech_needed('cars')
print(needed_q9b) 
print(needed_q9c)

# desired output 
# ['village', 'city']
# ['advanced_factory', 'factory', 'village', 'city']    
