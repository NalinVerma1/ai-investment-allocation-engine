import pandas as pd
from sheets_io import write_df

df = pd.DataFrame({
    "Asset": ["US Equity", "Tech ETF", "Bonds"],
    "Weight": [0.4, 0.4, 0.2]
})

write_df("Results", df)
print("Results written successfully")
