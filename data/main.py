import pandas as pd

print("Lazarus Medical Recovery System Running...")

data = {"Patient": ["A", "B"], "BPM": [80, None]}
df = pd.DataFrame(data)

df["BPM"] = df["BPM"].fillna(method="ffill")

print(df)
