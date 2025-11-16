// Openqasm grover's algorithm backend library implementation 

OPENQASM 2.0;
include "qelib1.inc";

// 2 qubits for the search space, 2 classical bits for measurement
qreg q[2];
creg c[2];

// Step 1: Put both qubits into superposition (|00⟩ -> (|00⟩+|01⟩+|10⟩+|11⟩)/2)
h q[0];
h q[1];

// Step 2: Oracle for marked index 2 (state |10⟩):
// To mark |10⟩, we apply X to q[1] (bit 1) before/after CZ 
x q[1];
cz q[0], q[1];
x q[1];

// Step 3: Diffusion operator (inversion about mean)
h q[0];
h q[1];

x q[0];
x q[1];

h q[1];
cx q[0], q[1];
h q[1];

x q[0];
x q[1];

h q[0];
h q[1];

// Step 4: Measure
measure q[0] -> c[0];
measure q[1] -> c[1];
