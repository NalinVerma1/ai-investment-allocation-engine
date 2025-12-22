def check_weight_limits(weights, min_w, max_w):
    for i in range(len(weights)):
        if weights[i] < min_w[i]:
            return False
        if weights[i] > max_w[i]:
            return False
    return True


def portfolio_risk(weights, risks):
    total = 0
    for i in range(len(weights)):
        total += weights[i] * risks[i]
    return total


def check_risk_limit(weights, risks, max_risk):
    r = portfolio_risk(weights, risks)
    if r <= max_risk:
        return True
    else:
        return False

