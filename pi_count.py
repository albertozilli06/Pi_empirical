from collections import Counter
import matplotlib.pyplot as plt

# Load the digits from the file
with open("pi_1million.txt", "r") as f:           #Replace with your own filename if necessary
    pi_str = f.read()

# Frequency Analysis of Digits (0-9)
digit_counts = Counter(pi_str)

# Print the frequency of each digit (0-9)
total_digits = len(pi_str)
for digit in range(10):
    freq = digit_counts[str(digit)] / total_digits * 100
    print(f"Digit {digit}: {digit_counts[str(digit)]} times ({freq:.4f}%)")

# Visualize the Frequency of Digits
digits, counts = zip(*sorted(digit_counts.items()))  # Sort for 0-9 order

# Alternate colors (for visualization purposes)
colors = ["skyblue", "lightcoral"] * 5  # Alternating between skyblue and lightcoral

plt.bar(digits, counts, color=colors)
plt.xlabel("Digits (0-9)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Digit Frequency in the First Million Digits of π", fontsize=16, fontweight='bold')
plt.tight_layout
plt.show()
