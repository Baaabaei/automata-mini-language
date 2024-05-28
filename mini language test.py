# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tIuQjhz1ohemzST0EvaSG_wOI7L2u8Cx
"""

# Test
code = 'a b c ab'
tokens = tokenize(code)
print(f"Tokens: {tokens}")

automata = [create_automaton(token) for token in TOKENS]
nfa, start_state, final_state = combine_automata(automata)
dfa, start_state = nfa_to_dfa(nfa, start_state, final_state)

print("DFA:")
for state, transitions in dfa.items():
    print(f"State {state}:")
    for char, next_state in transitions.items():
        print(f"  '{char}' -> {next_state}")



