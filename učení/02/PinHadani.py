import itertools

# Vytvoříme seznam čísel 1, 2, 3, 4
numbers = [1, 2, 3, 4]

# Vygenerujeme všechny možné kombinace 4 čísel
combinations = list(itertools.product(numbers, repeat=4))

# Projdeme všechny kombinace a vypíšeme je
for combination in combinations:
    print(combination)