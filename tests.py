from qiskit import QuantumCircuit, execute, Aer

# Create a 8-qubit circuit
circuit = QuantumCircuit(8, 8)

# Apply Hadamard gate to all qubits
for i in range(8):
    circuit.h(i)

# Measure all qubits in the computational basis
circuit.measure(range(8), range(8))

# Execute the circuit on a simulator
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend, shots=1).result()
counts = result.get_counts()

# Convert the measurement result to a decimal number
number = int(list(counts.keys())[0], 2)

print(number)
