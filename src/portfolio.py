import itertools

def portfolio_risk(weights, risks):
    total_risk = 0

    for i in range(len(weights)):
        total_risk = total_risk + weights[i] * risks[i]

    return total_risk


def worst_case_return(weights, bull, base, bear):
    worst = 1e9  

    for scenario in [bull, base, bear]:
        portfolio_return = 0

        for i in range(len(weights)):
            portfolio_return = portfolio_return + weights[i] * scenario[i]

        if portfolio_return < worst:
            worst = portfolio_return

    return worst


def find_best_portfolio(assets, risks, returns, min_w, max_w, max_risk):
    n = len(assets)
    step = 0.25

    best_score = -1e9
    best_weights = None

    values = []
    i = 0
    while i <= 1:
        values.append(round(i, 2))
        i = i + step

    all_combinations = itertools.product(values, repeat=n)

    for weights in all_combinations:
        total_weight = 0
        for i in range(n):
            total_weight = total_weight + weights[i]

        if abs(total_weight - 1) > 0.001:
            continue

        valid = True
        for i in range(n):
            if weights[i] < min_w[i] or weights[i] > max_w[i]:
                valid = False
                break

        if not valid:
            continue

        risk = portfolio_risk(weights, risks)
        if risk > max_risk:
            continue

        score = worst_case_return(weights, returns[0], returns[1], returns[2])

        if score > best_score:
            best_score = score
            best_weights = weights

    return best_weights, best_score
