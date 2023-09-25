def calculate_statistical_distance(distribution_1, distribution_2):
    set_of_all_keys = set(distribution_1.keys()).union(set(distribution_2.keys()))
    # delta(X_k, Y_k)
    total_variation_distance = 0.0
    for key in set_of_all_keys:
        prob1 = distribution_1.get(key, 0.0)  # Probability of key in distribution 1
        prob2 = distribution_2.get(key, 0.0)  # Probability of key in distribution 2
        total_variation_distance += abs(prob1 - prob2)

    total_variation_distance *= 0.5  # Multiply by 0.5 as per the formula
    return total_variation_distance


def calculate_letter_frequency(text):
    # Initialize an empty dictionary to store letter frequencies
    letter_frequency = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}

    # Iterate through each character in the text
    for char in text:
        # Consider only alphabetic characters
        if char.isalpha():
            # Convert to uppercase to count regardless of case
            char = char.upper()
            # Update the count for the corresponding letter
            letter_frequency[char] = letter_frequency.get(char, 0) + 1

    # Calculate the total number of letters in the text
    total_letters = sum(letter_frequency.values())

    # Convert counts to percentages
    for char, count in letter_frequency.items():
        letter_frequency[char] = (count / total_letters) * 100

    return letter_frequency


def calculater_letter_probability_distribution(letter_frequencies):
    total_letters = sum(letter_frequencies.values())
    letter_probabilities = {char: freq / total_letters for char, freq in letter_frequencies.items()}
    # print("Letter Probability Distribution: ", letter_probabilities)
    return letter_probabilities


def perform_k_shift(ciphertext, shift):
    shifted_ciphertext = ''.join(
        chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) if char.isalpha() else char
        for char in ciphertext.upper()
    )
    return shifted_ciphertext


def perform_shift_cipher_analysis(ciphertext):
    english_letter_frequencies = {
        'A': 8.2, 'B': 1.5, 'C': 2.8, 'D': 4.3, 'E': 12.7,
        'F': 2.2, 'G': 2.0, 'H': 6.1, 'I': 7.0, 'J': 0.2,
        'K': 0.8, 'L': 4.0, 'M': 2.4, 'N': 6.7, 'O': 7.5,
        'P': 1.9, 'Q': 0.1, 'R': 6.0, 'S': 6.3, 'T': 9.1,
        'U': 2.8, 'V': 1.0, 'W': 2.4, 'X': 0.2, 'Y': 2.0, 'Z': 0.1
    }
    english_letter_probability_distribution = calculater_letter_probability_distribution(english_letter_frequencies)
    min_stat_distance = float("inf")
    min_stat_inx = -1
    for i in range(26):
        shifted_letter_frequencies = calculate_letter_frequency(perform_k_shift(ciphertext, i))
        # plot_histogram(shifted_letter_frequencies)
        shifted_letters_distribution = calculater_letter_probability_distribution(shifted_letter_frequencies)
        stat_distance = calculate_statistical_distance(
            english_letter_probability_distribution, shifted_letters_distribution)
        if stat_distance <= min_stat_distance:
            min_stat_distance = stat_distance
            min_stat_inx = i
    # print("OK", ciphertext)
    return perform_k_shift(ciphertext, min_stat_inx)
    # perform_cipher_decrypt(ciphertext)
