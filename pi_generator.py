from mpmath import mp

mp.dps = 1_000_000  # Set precision to 1 million digits
pi_str = str(mp.pi)[2:]  # Remove "3." at the beginning

# Save to file for future analysis
with open("pi_1million.txt", "w") as f:
    f.write(pi_str)
