import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/pulsars.csv")


# binary star filter
df = df.replace("*", pd.NA)

# converting the columns to numeric
df["P0"] = pd.to_numeric(df["P0"], errors="coerce")
df["P1"] = pd.to_numeric(df["P1"], errors="coerce")

df = df[
    (df["P0"] > 0.03) &
    (df["P1"] > 0)
]

df_binary = df[
    (df["BINARY"].notna())
]
df = df[(df["BINARY"].isna())]


plt.figure()
plt.scatter(df["P0"], df["P1"], s=5, label = "Single Pulsars")
plt.scatter(df_binary["P0"],df_binary["P1"], s=10, color="red", label="Binary Pulsars")

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Period P (s)")
plt.ylabel("Period Derivative Pdot (s/s)")
plt.title("Binary labelled P–Pdot Diagram")

plt.legend()
plt.savefig("./plots/PvP_with_binary.png");
plt.show()

print("Singular Pulsars", len(df))
print("Binary Pulsars", len(df_binary))






