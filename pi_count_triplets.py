import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import random
from collections import Counter

# Function to generate random triplets
def generate_random_triplets(num_triplets):
    triplets = []
    for _ in range(num_triplets):
        triplet = ''.join(random.choices('0123456789', k=3))  # Random triplet
        triplets.append(triplet)
    return triplets

# Function to plot the bar graph
import matplotlib.pyplot as plt

# Function to plot the bar graph
def plot_graph(triplets, counts, percentages):
    # Prepare data for plotting
    labels = triplets
    fig, ax = plt.subplots()

    # Alternates between two colors
    colors = ['skyblue', 'lightcoral'] * (len(labels) // 2)  

    # Bar chart for counts
    ax.bar(labels, counts, color=colors, label='Occurrences')

    # Add percentages above the bars
    for i, count in enumerate(counts):
        ax.text(i, count + 10, f"{percentages[i]:.4f}%", ha='center', va='bottom', fontsize=18)

    # Labels and title with larger fonts
    ax.set_xlabel("Triplets", fontsize=24)
    ax.set_ylabel("Frequency", fontsize=24)
    ax.set_title("Triplet Frequency in the First Million Digits of π", fontsize=32, fontweight='bold')
    ax.tick_params(axis='both', labelsize=18)
    plt.tight_layout
    plt.show()


# Main function for the Tkinter interface
def main():
    # Load the digits of Pi from the file
    with open("pi_1million.txt", "r") as f:   #change with your own file path when necessary
        pi_str = f.read()

    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user for the number of triplets (3-10)
    num_triplets = simpledialog.askinteger("Input", "How many triplets would you like to analyze? (3 to 10)", minvalue=3, maxvalue=10)

    if num_triplets is None:
        return  # Exit if no input is provided

    # Ask the user if they want to input their own triplets or generate random ones
    choice = simpledialog.askstring("Input", "Do you want to input your own triplets? (yes/no)").strip().lower()

    triplets = []

    if choice == 'yes':
        for i in range(num_triplets):
            triplet = simpledialog.askstring("Input", f"Enter triplet {i + 1} (3 digits):")
            if triplet and len(triplet) == 3 and triplet.isdigit():
                triplets.append(triplet)
            else:
                print("Invalid input, skipping triplet.")
                continue
    else:
        # Generate random triplets
        triplets = generate_random_triplets(num_triplets)

    # Count the occurrences of each triplet in Pi
    triplet_counts = Counter([pi_str[i:i+3] for i in range(len(pi_str)-2)])

    # Prepare the count and percentage data for the graph
    counts = [triplet_counts[triplet] for triplet in triplets]
    percentages = [count / (len(pi_str) - 2) * 100 for count in counts]

    # Display the graph
    plot_graph(triplets, counts, percentages)

# Run the program
if __name__ == "__main__":
    main()
