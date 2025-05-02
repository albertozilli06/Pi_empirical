Pi Normality Experiment
This project aims to explore the distribution of digits in the infinite decimal expansion of π. Inspired by a scene in Person of Interest, this experiment uses Python to analyze and visualize the frequencies of digits and triplets within the first 1 million digits of π.

Files Included

pi_generator.py
This file generates the first 1 million digits of π and saves them in a .txt file (pi_1million.txt). The user can customize the number of digits or choose a different file if needed.

pi_count.py
This script analyzes the frequency distribution of individual digits (0-9) in the 1 million digits of π. It visualizes the results as a bar chart.

pi_count_triplets.py
In this script, users can input up to 10 three-digit triplets (e.g., "125", "842", "746"). It calculates and plots the frequency of each triplet's occurrence in the 1 million digits of π.

pi_segments.py
This file splits the digits of π into 10 equal segments (each 100,000 digits). It analyzes how a selected triplet behaves across these segments and visualizes the results in a bar chart.

Project Overview
This project is inspired by a memorable scene in Person of Interest, where Harold Finch explains how the digits of π might contain every possible combination — every name, every date, every truth. This idea rests on the mathematical hypothesis that π is a normal number.

A number is considered normal if every digit and every possible sequence of digits occurs with equal frequency in its infinite decimal expansion. While this has not yet been formally proven for π, we explore this hypothesis empirically by analyzing the frequency of digit triplets in the first million digits of π.

Using Python and data visualization libraries, this project provides interactive tools to:

The distribution of single digits (0-9)
The frequency of user-defined triplets
How triplets behave across different segments of the number

Features:

Pi Digit Frequency: Plot the distribution of individual digits (0-9) in the first 1 million digits of π.
Triplet Analysis: Analyze and visualize the frequency of user-defined triplets (three-digit combinations).
Segment-wise Triplet Analysis: Observe how triplets appear in different segments of the number (each containing 100,000 digits).

Libraries Used:

Matplotlib: For plotting bar charts and visualizations.
Tkinter: For a simple interface allowing user input for triplet analysis.

How to Run the Code

Step 1: Install Dependencies
Ensure you have Python installed. Install the required libraries using pip:
pip install matplotlib

Step 2: Generate Pi Digits (if necessary)
python pi_generator.py
This will create a file called pi_1million.txt containing the first million digits.
Alternatively, you can use the pi_1million.txt provided in this reposotory

Step 3: Run the Experiments

To analyze the frequency of digits (0-9), run:
python pi_normal.py

To analyze triplet frequencies, run:
pi_triplet.py
You'll be prompted to input up to 10 triplets for analysis.

To analyze how a triplet behaves across 10 segments of the number, run:
python pi_segments.py
You'll be asked to input the triplet you'd like to analyze.

Customization
Change the number of digits generated in pi_generator.py by adjusting the num_digits variable. 
Modify pi_triplet.py and pi_segments.py to experiment with different sets of triplets or segments.

Conclusion
This project serves as an exploration of π’s randomness and normality, as well as a hands-on demonstration of data analysis using Python. It combines fun, curiosity, and the power of statistical testing to analyze one of the most famous irrational numbers in mathematics.

Feel free to contribute, fork, or modify this repository as you wish. For any questions or feedback, don’t hesitate to reach out!

License
This project is licensed under the MIT License — see the LICENSE file for details.
