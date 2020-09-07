from itertools import permutations, product


def generate_possible_keys(number_of_columns):
    results = []
    columns = [number for number in range(1, number_of_columns + 1)]
    for perm in permutations(columns):
        for signs in product([-1, 1], repeat=len(columns)):
            results.append([i*sign for i, sign in zip(perm, signs)])
    return results
