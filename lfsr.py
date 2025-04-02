def lfsr8Bit(seed, polynomial):
    
    state = seed
    sequence = []
    registers = []

    maxPeriod = 255

    for i in range(maxPeriod):
        # Obtenemos el lbs para la secuencia
        bit_out = state & 1
        sequence.append(bit_out)
        
        # Obtener el bit en base al polinomio
        new_bit = 0
        for t in polynomial:
            new_bit ^= (state >> (t - 1)) & 1
        
        state = (state >> 1) | (new_bit << 7)
        registers.append(state)

        # Comprobamos el periodo máximo cuando el registro sea igual a
        # la semilla.
        if state == seed:
            print(f"Periodo máxicmo: {i+1}" )
            break

    return sequence, registers

seed=0b11000011
polynomial=[8,7,2,1]

lfsr, registers = lfsr8Bit(seed, polynomial)
print("Secuencia generada:", "".join(map(str, lfsr)))
print()
print("Vista de como se modifica la semilla: ")
for i in registers:
    print(format(i, '08b'))

