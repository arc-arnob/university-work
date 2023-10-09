def mscxdeg(cell_tap_bits, n_output_bits, init_state):
    result = []
    for i in range(n_output_bits):
        feedback = 0
        result.append(init_state[-1])
        for index, value in enumerate(cell_tap_bits):
            if value:
                feedback ^= init_state[index]
        init_state = [feedback] + init_state
    print(init_state[-n_output_bits:])
    return result


