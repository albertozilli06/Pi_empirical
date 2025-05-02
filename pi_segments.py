import matplotlib.pyplot as plt

# Function to load digits from the file
def load_digits_from_file(filename):
    with open(filename, 'r') as f:
        return f.read().replace("\n", "")  # Remove newlines if any

# Function to divide the number into 10 equal segments
def divide_into_segments(digits, num_segments=10):
    segment_length = len(digits) // num_segments
    segments = [digits[i * segment_length: (i + 1) * segment_length] for i in range(num_segments)]
    return segments

# Function to count the occurrences of a triplet in each segment
def count_triplet_in_segments(triplet, segments):
    counts = [segment.count(triplet) for segment in segments]
    return counts

# Function to plot the frequencies of the triplet in each segment with alternating colors
def plot_triplet_frequencies(triplet, counts, segments):
    fig, ax = plt.subplots()
    colors = ['skyblue', 'lightcoral'] * (len(segments) // 2)  # Alternating colors
    segment_numbers = list(range(1, len(segments) + 1))

     
    ax.bar(range(1, len(segments) + 1), counts, color=colors[:len(segments)])

    ax.set_xlabel('Segment Number', fontsize=14)
    ax.set_xticks(segment_numbers)
    ax.set_ylabel(f'Frequency of Triplet "{triplet}"', fontsize=14)
    ax.set_title(f'Triplet Frequency Across 10 Segments of Pi\'s Digits', fontsize=16, fontweight='bold')

    # Adding the triplet count above each bar
    for i, count in enumerate(counts):
        ax.text(i + 1, count + 0.1, str(count), ha='center', va='bottom', fontsize=12)

    ax.tick_params(axis='both', labelsize=12)
    plt.tight_layout
    plt.show()

# Main function to drive the experiment
def main(filename):
    digits = load_digits_from_file(filename)
    segments = divide_into_segments(digits)

    # Take user input for the triplet they want to analyze
    triplet = input("Enter a 3-digit triplet to analyze: ").strip()

    if len(triplet) != 3 or not triplet.isdigit():
        print("Please enter a valid 3-digit number.")
        return

    counts = count_triplet_in_segments(triplet, segments)

    # Plot the frequencies of the triplet in each segment
    plot_triplet_frequencies(triplet, counts, segments)

# Main function with the path to the txt file containing digits of Pi
if __name__ == "__main__":
    filename = "pi_1million.txt"  # Change with your own file if needed
    main(filename)
