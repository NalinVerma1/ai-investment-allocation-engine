from engine import get_feasible_portfolios, find_best_portfolio

n = 3
step = 0.5

min_w = [0, 0, 0]
max_w = [1, 1, 1]

risk_scores = [8, 5, 2]
max_risk = 6

bull_returns = [0.20, 0.12, 0.05]
neutral_returns = [0.10, 0.07, 0.04]
bear_returns = [-0.25, -0.10, -0.02]

feasible = get_feasible_portfolios(n, step, min_w, max_w, risk_scores, max_risk)

print("FEASIBLE PORTFOLIOS")
for f in feasible:
    print(f)

result = find_best_portfolio( feasible, bull_returns, neutral_returns, bear_returns)

best_weights = result[0]
best_score = result[1]

print("")
print("BEST PORTFOLIO")
print(best_weights)

print("")
print("WORST CASE RETURN")
print(best_score)
