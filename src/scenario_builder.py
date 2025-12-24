def build_scenarios(base_returns):
    
    bull = []
    neutral = []
    bear = []

    for r in base_returns:
        bull.append(r * 1.2)
        neutral.append(r)
        bear.append(r * 0.7)

    return bull, neutral, bear