import pandas as pd

THRESHOLD = 0.74

df = pd.read_csv("retrieval_evaluation.csv")

df["Accepted"] = df["Score"] >= THRESHOLD

print("\nRETRIEVAL THRESHOLD TEST")
print("=" * 60)

print(f"Threshold: {THRESHOLD}")

print("\nAll Results")
print("-" * 60)

for _, row in df.iterrows():
    status = "ACCEPT" if row["Accepted"] else "REJECT"

    print(
        f"{row['Test_ID']} | "
        f"{row['Score']:.3f} | "
        f"{row['Retrieval_Assessment']:<8} | "
        f"{status}"
    )

print("\nSUMMARY")
print("=" * 60)

strong = df[df["Retrieval_Assessment"] == "Strong"]
partial = df[df["Retrieval_Assessment"] == "Partial"]
wrong = df[df["Retrieval_Assessment"] == "Wrong"]

print(f"Strong matches:  {len(strong)}")
print(f"Partial matches: {len(partial)}")
print(f"Wrong matches:   {len(wrong)}")

print("\nThreshold behavior")
print("-" * 60)

print(
    f"Strong accepted: "
    f"{(strong['Accepted']).sum()} / {len(strong)}"
)

print(
    f"Wrong rejected:   "
    f"{(~wrong['Accepted']).sum()} / {len(wrong)}"
)

print("\nBorderline / Partial Cases")
print("-" * 60)

for _, row in partial.iterrows():
    print(
        f"{row['Test_ID']} | "
        f"{row['Score']:.3f} | "
        f"{'ACCEPT' if row['Accepted'] else 'REJECT'}"
    )