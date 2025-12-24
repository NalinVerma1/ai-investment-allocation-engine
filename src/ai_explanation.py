import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_ai_explanation(assets, weights, risks, returns_5y, score):
    portfolio_lines = []

    for i in range(len(assets)):
        if weights[i] > 0:
            portfolio_lines.append(
                f"{assets[i]}: {round(weights[i]*100,1)}% "
                f"(RiskScore={risks[i]}, 5Y Return={round(returns_5y[i]*100,1)}%)"
            )

    prompt = f"""
You are a financial analysis assistant.

The portfolio below was constructed using 5-year returns to reduce short-term noise.

Portfolio:
{chr(10).join(portfolio_lines)}

Worst-case portfolio return: {round(score*100,2)}%

Explain:
1. Why these assets were selected
2. Why some assets received zero allocation
3. Why long-term returns were prioritized

Do NOT provide investment advice.
Keep the explanation concise and professional.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
