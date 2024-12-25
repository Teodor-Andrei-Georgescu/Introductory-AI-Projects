def isComplete(assignment):
    return None not in (assignment.values())

def select_unassigned_variable(variables, assignment):
    for var in variables:
        if assignment[var] is None:
            return var

def is_consistent(assignment, constraints):
    for constraint_violated in constraints:
        if constraint_violated(assignment):
          return False
    return True

def init_assignment(csp):
    assignment = {}
    for var in csp["VARIABLES"]:
        assignment[var] = None
    return assignment

def add_constraint(csp, constraint): 
    csp['CONSTRAINTS'].append(constraint)
    
def recursive_backtracking(assignment, csp):
    if isComplete(assignment):
        return assignment
    var = select_unassigned_variable(csp["VARIABLES"], assignment)
    for value in csp["DOMAINS"]:
        assignment[var] = value
        if is_consistent(assignment, csp["CONSTRAINTS"]):
            result = recursive_backtracking(assignment, csp)
            if result != "FAILURE":
                return result
        assignment[var] = None
    return "FAILURE"


def binary_constraint(var_pair, violations):
    (v1,v2) = var_pair
    return lambda asmt: (asmt[v1], asmt[v2]) in violations
  
# add your code for CSP-based type inference as described in the notebook 
# below. The answer to the problem provided should be named result and 
# be a dictionary with a complete assignment of the variables to types 
# as returned by the CSP backtracking method. 
def unary_constraint(variable, not_possible_values):
    return lambda asmt: asmt[variable] in not_possible_values

def ternary_constraints(var, possible_values):
    not_possible_value = []
    if len(possible_values)  == 1:
        if possible_values[0] == "int":
            not_possible_value.append("float")
        else:
            not_possible_value.append("int")
    elif len(possible_values) == 2:
        if possible_values[0] == "int" and possible_values[1] == "float":
            not_possible_value.append("int")
        elif possible_values[0] == "int" and possible_values[1] == "int":
            not_possible_value.append("float")
        else:
            not_possible_value.append("int")
    return lambda asmt: asmt[var] in not_possible_value


csp = {
    "VARIABLES": ["I", "F", "X", "Y", "Z", "W"],
    "DOMAINS": ["int", "float"],
    "CONSTRAINTS": []
}
violations ={("int","int"),("float","float")}

#add type contraints for f to be float and I to be int
add_constraint(csp,unary_constraint("I",["float"]))
add_constraint(csp,unary_constraint("F",["int"]))\

#To infer restraint based on types on equations
add_constraint(csp,ternary_constraints("X",["int"]))
add_constraint(csp,ternary_constraints("Y",["int","float"]))
add_constraint(csp,ternary_constraints("Z",["int","float"]))
add_constraint(csp,ternary_constraints("W",["int","int"]))

result = recursive_backtracking(init_assignment(csp),csp)
    