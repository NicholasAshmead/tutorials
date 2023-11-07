# Write a Python program that shows whether or not that a relation R on set A is reflexive, symmetricor transitive

A = {1, 2, 3, 4, 5}
R = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)}

# Reflexive
def reflexive(A, R):
    for a in A:
        if (a, a) not in R:
            return False
    return True

# Symmetric
def symmetric(A, R):
    for a in A:
        for b in A:
            if (a, b) in R and (b, a) not in R:
                return False
    return True

# Transitive
def transitive(A, R):
    for a in A:
        for b in A:
            for c in A:
                if (a, b) in R and (b, c) in R and (a, c) not in R:
                    return False
    return True

print("Reflexive: ", reflexive(A, R))
print("Symmetric: ", symmetric(A, R))
print("Transitive:", transitive(A, R))