# Quantum_grover_algorithm-implementation
Grover's algorithm
# Grover's Search Demonstrator (2-Qubit)

## Grover's Algorithm: Definition and Summary
- **Grover's algorithm** is a quantum algorithm that searches an unsorted database for a marked item with quadratic speedup compared to classical search—instead of checking every item one by one, Grover's algorithm can find the winning item in roughly √N steps, where N is the number of items.
- This demonstration uses 2 qubits (representing 4 items: |00⟩, |01⟩, |10⟩, |11⟩) and amplifies the probability of the marked item using quantum amplitude amplification.

## Oracle Construction for Marking States (OpenQASM/X-Gate Pattern)
- To "mark" a specific item, the algorithm applies X gates and a CZ gate as follows:
    - For |00⟩: `X q[0]; X q[1]; cz q[0],q[1]; X q[0]; X q[1];`
    - For |01⟩: `X q[0]; cz q[0],q[1]; X q[0];`
    - For |10⟩: `X q[1]; cz q[0],q[1]; X q[1];`
    - For |11⟩: `cz q[0],q[1];`
- Just change the X gate pattern around the controlled-Z gate to suit your marked_index: flip (X) any qubit that's a 0 in the marked basis state before and after CZ.

## Application Flow
- **Backend**: Implements Grover's algorithm (as a Python function, with API endpoint) to run the quantum search and return measurement probabilities.
- **UI**: User chooses a "target item" (index 0–3). The interface calls the API and displays each item's probability in a bar chart, with the marked item shown as highest—demonstrating quantum search speedup.

## One-Line Summary
Grover's algorithm finds a marked item in an unsorted database much faster than classical methods, and this code demonstrates it for a 2-qubit (4-item) search with a simple API and UI.
