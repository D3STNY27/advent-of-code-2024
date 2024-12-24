import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    divider = lines.index('')
    initial_wires = lines[:divider]
    configurations = lines[divider+1:]

    wires_map = {}
    unprocessed_gates = set()
    ready_gates = set()
    z_outputs = []

    for wires in initial_wires:
        wire_name, wire_value = [wire.strip() for wire  in wires.split(':')]
        
        if wire_name not in wires_map:
            wires_map[wire_name] = bool(int(wire_value))
    

    for gates in configurations:
        input_config, output_wire = gates.split(' -> ')
        wire_a, gate_type, wire_b = input_config.split(' ')

        if (wire_a in wires_map) and (wire_b in wires_map):
            ready_gates.add((wire_a, wire_b, gate_type, output_wire))
        else:
            unprocessed_gates.add((wire_a, wire_b, gate_type, output_wire))

    
    while True:
        while ready_gates:
            wire_a, wire_b, gate_type, output_wire = ready_gates.pop()
    
            if gate_type == 'AND':
                output_wire_value = wires_map[wire_a] and wires_map[wire_b]
            elif gate_type == 'OR':
                output_wire_value = wires_map[wire_a] or wires_map[wire_b]
            else:
                output_wire_value = wires_map[wire_a] != wires_map[wire_b]
        
            wires_map[output_wire] = output_wire_value
            if output_wire.startswith('z'):
                z_outputs.append((output_wire, output_wire_value))
        
        if not unprocessed_gates:
            break

        for (wire_a, wire_b, gate_type, output_wire) in list(unprocessed_gates):
            if (wire_a in wires_map) and (wire_b in wires_map):
                ready_gates.add((wire_a, wire_b, gate_type, output_wire))
                unprocessed_gates.remove((wire_a, wire_b, gate_type, output_wire))
    
    binary_num = ''
    for _, wire_value in sorted(z_outputs):
        binary_num = str(int(wire_value)) + binary_num
    
    print(int(binary_num, 2))


lines = read_input_file(file_path="input.txt")
solution(lines)