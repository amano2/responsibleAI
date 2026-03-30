import pandas as pd

# Simulated dataset
data = {
    "candidate": ["A", "B", "C", "D", "E", "F"],
    "skin_tone": ["light", "light", "dark", "dark", "light", "dark"],
    "actual": [1, 1, 1, 1, 0, 0],   # 1 = correct match
    "predicted": [1, 1, 0, 0, 0, 0]  # biased predictions
}
df = pd.DataFrame(data)
print("\n--- Original Dataset ---")
print(df)

# Accuracy per group
def group_accuracy(df, group):
    group_df = df[df["skin_tone"] == group]
    return (group_df["actual"] == group_df["predicted"]).mean()

print("\n--- Initial Bias Measurement ---")
light_acc = group_accuracy(df, "light")
dark_acc = group_accuracy(df, "dark")
print("Accuracy (Light):", light_acc)
print("Accuracy (Dark):", dark_acc)
print("Bias Gap:", light_acc - dark_acc)

# Fix: balance predictions manually (simulate better data - Pre-processing)
df.loc[df["skin_tone"] == "dark", "predicted"] = [1, 1, 0]

# Apply fairness correction (In-processing)
def apply_fairness(df):
    for i in df.index:
        if df.loc[i, "skin_tone"] == "dark" and df.loc[i, "predicted"] == 0:
            df.loc[i, "predicted"] = 1  # simulate correction
    return df
df = apply_fairness(df)

# Reject uncertain predictions (Post-processing)
def post_process(pred):
    if pred == 0:
        return "REVIEW"
    return "ACCEPT"
df["final_decision"] = df["predicted"].apply(post_process)

print("\n--- Final Decisions ---")
print(df[["candidate", "final_decision"]])

print("\n--- After Fix Metrics ---")
light_acc = group_accuracy(df, "light")
dark_acc = group_accuracy(df, "dark")
print("Accuracy (Light):", light_acc)
print("Accuracy (Dark):", dark_acc)
print("Bias Gap:", light_acc - dark_acc)