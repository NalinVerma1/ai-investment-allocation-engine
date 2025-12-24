from .sheets import read_assets, read_constraints, write_results , write_ai_explanation
from .scenario_builder import build_scenarios
from .portfolio import find_best_portfolio
from .ai_explanation import generate_ai_explanation
from .ai_explanation import generate_ai_explanation


def main():
    assets, risks, returns_5y = read_assets()
    capital, min_w, max_w, max_risk = read_constraints()

    bull, base, bear = build_scenarios(returns_5y)

    best_weights, score = find_best_portfolio(assets, risks, (bull, base, bear), min_w, max_w, max_risk)
    explanation = generate_ai_explanation(assets, best_weights, risks, returns_5y, score)
    write_ai_explanation(explanation)
    write_results(assets, best_weights, capital, score)

    if best_weights is None:
        print("No feasible portfolio found with current constraints.")
        return

    print("Capital:", capital)

    print("\nBest portfolio:")
    for i in range(len(assets)):
        print(assets[i], ":", round(best_weights[i] * 100, 1), "%")

    print("\nDollar allocation:")
    for i in range(len(assets)):
        dollars = best_weights[i] * capital
        print(assets[i], ":", round(dollars, 2))

    print("Worst-case return:", round(score * 100, 2), "%")
    print("\nAI Explanation:")
    print(explanation)

if __name__ == "__main__":
    main()
