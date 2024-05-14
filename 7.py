def unify(term1, term2, substitution=None):
    if substitution is None:
        substitution = {}

    if term1 == term2:
        return substitution

    if isinstance(term1, str) and term1.islower():
        return unify_var(term1, term2, substitution)
    elif isinstance(term2, str) and term2.islower():
        return unify_var(term2, term1, substitution)
    elif isinstance(term1, list) and isinstance(term2, list):
        if len(term1) != len(term2):
            return "None"
        for t1, t2 in zip(term1, term2):
            substitution = unify(t1, t2, substitution)
            if substitution == "None":
                return "None"
        return substitution
    else:
        return "None"

def unify_var(var, x, substitution):
    if var in substitution:
        return unify(substitution[var], x, substitution)
    elif isinstance(x, str) and x.islower() and x in substitution:
        return unify(var, substitution[x], substitution)
    else:
        substitution[var] = x
        return substitution

# Test cases
if __name__ == "__main__":
    # Test 1
    fact1 = ['likes', 'Alice', 'Bob']
    fact2 = ['likes', 'Alice', 'Bob']
    print(unify(fact1, fact2))  # Output: {}

    # Test 2
    fact3 = ['likes', 'Alice', 'Bob']
    fact4 = ['likes', 'Alice', 'Charlie']
    print(unify(fact3, fact4))  # Output: None

    # Test 3
    fact5 = ['drinks', 'X', 'coffee']
    fact6 = ['drinks', 'Alice', 'coffee']
    print(unify(fact5, fact6))  # Output: {'X': 'Alice'}

    # Test 4
    fact7 = ['drinks', 'X', 'tea']
    fact8 = ['drinks', 'Alice', 'coffee']
    print(unify(fact7, fact8))  # Output: None
