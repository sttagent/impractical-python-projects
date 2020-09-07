from itertools import permutations, product


def generate_possible_keys(number_of_columns):
    results = []
    for perm in permutations(number_of_columns):
        for signs in product([-1, 1], repeat=len(number_of_columns)):
            results.append([i*sign for i, sign in zip(perm, signs)])
    return results
