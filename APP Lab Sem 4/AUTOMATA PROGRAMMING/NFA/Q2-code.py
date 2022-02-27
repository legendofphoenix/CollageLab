""" Write a automata code for L(M)= a + aa*b + a*b. 3. Write a automata code for Let Σ = {0,1}."""
from automata.fa.nfa import NFA
# NFA which accepts strings that ends with 'ab'
nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1','q2'}},
        'q1': {'a': {'q2','q4'}, 'b': {'q4'}},
        'q2': {'a': {'q2'}, 'b': {'q3'}},
        'q3': {},
        'q4': {}
    },
    initial_state='q0',
    final_states={'q1','q3'}
)
for i in range(1,6):
    num = input("Enter the string :")
    if(nfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
