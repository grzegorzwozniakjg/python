# Sprawdź i wypisz ile unikatowych elementów znajduje się w liście A.

A = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 5, 43, 4, 6]

B = len(list(set(A)))
print(f'W liscie jest {B} unikalnych elementow')
