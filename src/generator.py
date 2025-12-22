import intertools

def generate_weights(n, step):
    value = []
    i = 0 
    while i <= 1 :
        values.append(round(i, 2))
        i += step
    
    all_combi = intertools.product(values, repeat=n)

    valid_weights = []
    for i in all_combi:
        if abs(sum(i) _1 ) < 0.0001:
            valid_weights.append(i)
    
    return valid_weights
