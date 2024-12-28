# File: a2_q5.py

from logic import tt_entails  # Importing truth table entailment from AIMA logic.py

# Sample truth values for 0 and 1 representation
TRUE = 1
FALSE = 0

# Definitions for logic operations
AND_TABLE = {
    ('1', '1'): '1',
    ('1', '0'): '0',
    ('0', '1'): '0',
    ('0', '0'): '0'
}
OR_TABLE = {
    ('1', '1'): '1',
    ('1', '0'): '1',
    ('0', '1'): '1',
    ('0', '0'): '0'
}
NEGATION_TABLE = {
    '1': '0',
    '0': '1'
}

def prefix_to_infix(expression):
    """Convert a prefix logical expression to an infix expression."""
    tokens = expression.strip().split()

    def helper(token_list):
        if not token_list:
            raise ValueError("Empty expression is invalid.")
        
        # Get the current operator or operand
        token = token_list.pop(0)
        
        # Handle logical operators
        if token in ['&', '|', '~']:
            if token == '~':
                # Negation should be applied to a single operand
                operand = helper(token_list)
                return f"(~ {operand})"
            else:
                # Handle binary operations (& and |)
                left = helper(token_list)
                right = helper(token_list)
                return f"({left} {token} {right})"
        else:
            # Return operand
            return token

    return helper(tokens)

def evaluate_expression(expression, bindings):
    """Evaluate an expression using bindings."""
    # Convert the prefix to infix notation first
    infix_expression = prefix_to_infix(expression)
    # Replace variables with their values from bindings
    for var, value in bindings.items():
        infix_expression = infix_expression.replace(var, str(value))
    return infix_expression

def model_check(kb_prefix, alpha_prefix, bindings):
    """Check if KB entails α using tt_entails from AIMA's logic."""
    # Convert KB and α from prefix to infix notation
    kb_infix = prefix_to_infix(kb_prefix)
    alpha_infix = prefix_to_infix(alpha_prefix)

    # Evaluate both KB and α in infix format
    kb_evaluated = evaluate_expression(kb_infix, bindings)
    alpha_evaluated = evaluate_expression(alpha_infix, bindings)
    
    # Using tt_entails from AIMA's logic to check entailment
    return tt_entails(kb_evaluated, alpha_evaluated)

# Example Test Cases
if __name__ == "__main__":
    # Sample KB and α
    kb = "& | p q ~ r"  # Sample knowledge base in prefix
    alpha = "| p r"      # Sample consequence in prefix
    bindings = {'p': 1, 'q': 0, 'r': 0}

    print(f"Prefix KB: {kb}")
    print(f"Prefix α: {alpha}")
    
    # Perform conversion to infix
    kb_infix = prefix_to_infix(kb)
    alpha_infix = prefix_to_infix(alpha)
    
    print(f"Infix KB: {kb_infix}")
    print(f"Infix α: {alpha_infix}")
    
    # Model checking using the bindings
    entailment = model_check(kb, alpha, bindings)
    
    print(f"Does KB entail α? {entailment}")
    
    # Additional test cases for verification
    test_cases = [
        ("& p q", "| p ~ q"),  # Sample test 1
        ("| ~ p & q r", "& p ~ r"),  # Sample test 2
        ("~ | p q", "& ~ p ~ q")  # Sample test 3
    ]

    for kb_test, alpha_test in test_cases:
        result = model_check(kb_test, alpha_test, bindings)
        print(f"KB: {kb_test} entails α: {alpha_test} -> {result}")
