from .generator import generate_weights
from .constraints import check_weight_limits, check_risk_limit
from .scoring import worst_case_return


def get_feasible_portfolios(n_assets, step, min_w, max_w, risk_scores, max_risk):
    feasible = []
    all_weights = generate_weights(n_assets, step)

    for weights in all_weights:
        if check_weight_limits(weights, min_w, max_w) == True:
            if check_risk_limit(weights, risk_scores, max_risk) == True:
                feasible.append(weights)

    return feasible


def find_best_portfolio(feasible_portfolios, bull_returns, neutral_returns, bear_returns):

    best_weights = None
    best_score = -999999

    for weights in feasible_portfolios:
        score = worst_case_return(
            weights,
            bull_returns,
            neutral_returns,
            bear_returns
        )

        if score > best_score:
            best_score = score
            best_weights = weights

    return best_weights, best_score
