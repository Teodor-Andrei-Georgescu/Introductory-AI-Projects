# Assignment 2: Propositional and First-Order Logic

This directory contains all files for **Assignment 2** of the CSC421 Fall 2024 course. The assignment focuses on **propositional logic**, **first-order logic**, and **logic evaluators**. Below is an overview of the questions and file structure. For detailed explanations of the questions, please refer to the screenshots provided.

## Overview of Questions

### OZU Logic Truth Table
In Question 1-4, the prefix logical evaluator works with a three-valued logic system. Below is the truth table used for this logic:

![OZU Logic Truth Table](./OZU%20Logic%20Truth%20Table.PNG)

### Question 1 (Basic): Evaluating Prefix Logic Expressions
- Implement a simple evaluator for prefix logical expressions with three-valued logic (`O`, `Z`, and `U`) and operators such as `|` and `&`.

### Question 2 (Basic): Adding Variable Bindings
- Extend the evaluator to support variable bindings using a dictionary.
    - The dictionary mapps variables to a corresponding O,Z or U value.

### Question 3 (Expected): Recursive Evaluator for Prefix Expressions
- Implement a recursive evaluator for logical prefix expressions, supporting multiple operands and nested operations.

### Question 4 (Expected): Support for Negation (`~`)
- Extend the evaluator to handle negation in logical expressions and validate its functionality.

### Question 5 (Advanced): Create Script For Knowledge Base Entailment and Infix Conversion
- Implement a feature to specify a knowledge base (KB) in prefix notation and a consequent in prefix notation.
- Convert the prefix expressions to infix notation and determine whether the KB entails the consequent using the `tt_entails` function from the AIMA logic.py code.
- Example entailment check:
  ```
  A&(B|C)&D&E&(¬F&¬G) |= A&D&E&¬F&¬G
  ```
- Ensure the solution includes test cases to confirm correctness.
- Extend the evaluator to handle negation in logical expressions and validate its functionality.

### Question 6 (Basic): Logical Circuits with Prolog
- Represent logical circuits (`OR`, `AND`, `NOT`) using Prolog facts and rules. Test circuit functionality through queries.

### Question 7 (Basic): Querying Logical Circuits
- Define and test logical circuits with multiple gates and queries.

### Question 8 (Expected): Complex Boolean Logic Expression in Prolog
- Create and test a Prolog rule for a complex Boolean logic expression (`(A AND B) OR (NOT C)`), including its truth table.

### Question 9 (Expected): Encoding a "Tech Tree" in Prolog
- Build a knowledge base to represent the dependency tree of game objects (e.g., villages, factories) and their production relationships. Use Prolog rules to query production needs.

## File Structure
- **`a2_q1234.py`**: Contains solutions for Questions 1 through 4.
- **`a2_q5.py`**: Contains Script that takes pre-fix notation inputs and check Knowledge Base entailment.
- **`a2_q6789.py`**: Prolog-related tasks (Questions 6 through 9).
- **`logic.py`**: A utility file that includes shared logic functions for Python-based logic evaluation tasks.
- **`Question Description screenshots`**: Contains screenshots of each question description.

