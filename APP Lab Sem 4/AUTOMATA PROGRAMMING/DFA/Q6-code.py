""" 6. Write a automata code for Let Σ = {0, 1}.Given DFAs for {}, {ε}, Σ*, and Σ+. """

#6.1
from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q0'},
        'q1': {'0': 'q1', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)
for i in range(1,8):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
        
  #6.2
from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q1'},
        'q1': {'0': 'q1', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q0'}
)
for i in range(1,6):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
    
 #6.3
from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q0'}
    },
    initial_state='q0',
    final_states={'q0'}
)
for i in range(1,8):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
      
 #6.4
from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q1'},
        'q1': {'0': 'q1', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)
for i in range(1,8):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
