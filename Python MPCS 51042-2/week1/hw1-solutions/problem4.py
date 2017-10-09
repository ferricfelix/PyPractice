from itertools import permutations

for s, l, a, y, e, r in permutations('0123456789', 6):
    # Determine string representation of SLAYER and LAYERS
    slayer = f'{s}{l}{a}{y}{e}{r}'
    layers = f'{l}{a}{y}{e}{r}{s}'

    # Actual result of SLAYER + SLAYER + SLAYER
    result = 3*int(slayer)

    # Check if actual and expected result match
    if str(result) == layers:
        print(f'{slayer} + {slayer} + {slayer} = {layers}')
