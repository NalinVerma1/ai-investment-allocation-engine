def portfolio_return(weights, returns):
    total_return = 0

    i = 0
    while i < len(weights):
        contribution = weights[i] * returns[i]
        total_return = total_return + contribution
        i = i + 1

    return total_return


def worst_case_return(weights, bull_returns, neutral_returns, bear_returns):
    bull_result = portfolio_return(weights, bull_returns)
    neutral_result = portfolio_return(weights, neutral_returns)
    bear_result = portfolio_return(weights, bear_returns)

    worst = bull_result

    if neutral_result < worst:
        worst = neutral_result

    if bear_result < worst:
        worst = bear_result

    return worst
