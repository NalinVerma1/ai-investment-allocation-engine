import itertools

def generate_weights(n, step):
    value = []
    i = 0 
    while i <= 1 :
        value.append(round(i, 2))
        i += step
    
    all_combi = itertools.product(values, repeat=n)

    valid_weights = []
    for i in all_combi:
        if abs(sum(i) -1 ) < 0.0001:
            valid_weights.append(i)
    
    return valid_weights
