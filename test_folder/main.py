import matplotlib.pyplot as plt
from math import gcd


def calculater_letter_probability_distribution(letter_frequencies):
    total_letters = sum(letter_frequencies.values())
    letter_probabilities = {char: freq / total_letters for char, freq in letter_frequencies.items()}
    # print("Letter Probability Distribution: ", letter_probabilities)
    return letter_probabilities


def generate_ngrams(text, n):
    # Split the text into words
    words = ''
    for index, value in enumerate(text):
        if value.isalpha():
            words += value
    # Generate n-grams
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = ''.join(words[i:i+n])
        ngrams.append(ngram)
    return ngrams


def perform_vigenere_cipher(ciphertext):
    # English Letter Frequencies
    # english_letter_frequencies = {
    #     'A': 8.2, 'B': 1.5, 'C': 2.8, 'D': 4.3, 'E': 12.7,
    #     'F': 2.2, 'G': 2.0, 'H': 6.1, 'I': 7.0, 'J': 0.2,
    #     'K': 0.8, 'L': 4.0, 'M': 2.4, 'N': 6.7, 'O': 7.5,
    #     'P': 1.9, 'Q': 0.1, 'R': 6.0, 'S': 6.3, 'T': 9.1,
    #     'U': 2.8, 'V': 1.0, 'W': 2.4, 'X': 0.2, 'Y': 2.0, 'Z': 0.1
    # }
    bigrams = generate_ngrams(ciphertext, 2)
    trigrams = generate_ngrams(ciphertext, 3)
    bigram_indexes = calculate_distance_between_n_grams(bigrams)
    trigram_indexes = calculate_distance_between_n_grams(trigrams)
    possible_key_lengths = get_repeated_n_grams_distance_values(trigram_indexes)

    # Cryptanalysis with plots are not helpful hence, trying statistical distance
    # english_letter_probability_distribution = calculater_letter_probability_distribution(english_letter_frequencies)
    print('There are following key lengths possible', possible_key_lengths)
    user_predicted_key_length = input(' which one do you want to try: ')
    try:
        user_predicted_key_length = int(user_predicted_key_length)
        if user_predicted_key_length not in possible_key_lengths:
            print('Oops wrong input, Terminating...')
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    for idx, key_len_val in enumerate(sorted([user_predicted_key_length])):
        possible_key = ""
        bins = bin_creation_with_n(sentence, key_len_val)
        for index, value in enumerate(bins):
            res = perform_shift_cipher_analysis(''.join(bins[index]))
            possible_key += res[0]
        key_val_is = vigenere_decrypt(ciphertext, possible_key).replace(' ','')[:key_len_val]
        print("Possible Key: ", key_val_is)
        print('Decrypted text: ', vigenere_decrypt(ciphertext, key_val_is))


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


def perform_k_shift(ciphertext, shift):
    shifted_ciphertext = ''.join(
        chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) if char.isalpha() else char
        for char in ciphertext.upper()
    )
    return shifted_ciphertext


def get_ngram_with_more_than_one_occurrences(bigrams_dict):
    max_length = 0
    longest_key = None
    longest_value = None
    repeated_n_gram_vals = []
    for key, value in bigrams_dict.items():
        if len(value) > 1:
            repeated_n_gram_vals.append(value)
    return repeated_n_gram_vals


def get_repeated_n_grams_distance_values(n_gram_dict):
    result = []
    most_occurrences = get_ngram_with_more_than_one_occurrences(n_gram_dict)
    # print("Most occ: ", get_bigram_with_more_than_one_occurrences(n_gram_dict))
    distance_list = []
    for index, value in enumerate(most_occurrences):
        distance_list.append(calculate_differences(value))
    result = list_of_gcd([element for sublist in distance_list for element in sublist])
    return result


def calculate_differences(arr):
    differences = []
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        differences.append(diff)
    return differences


def calculate_distance_between_n_grams(array):
    element_meta = {}
    for index, i in enumerate(array):
        if element_meta.get(i) is not None:
            element_meta[i].append(index)
        else:
            element_meta[i] = [index]
    return element_meta


def list_of_gcd(numbers):
    result_array = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num1 = numbers[i]
            num2 = numbers[j]
            gcd_result = gcd(num1, num2)
            if gcd_result > 25:
                continue
            result_array.append(gcd_result)
    return result_array


def bin_creation_with_n(sentence, n):
    # Debug code: 0x001
    cleaned_sentence = ''
    for char in sentence:
        if char.isalpha():
            cleaned_sentence += char    # Remove special characters
    bin_matrix = []
    for i in range(n):
        bin = []
        for index, value in enumerate(cleaned_sentence.replace(' ', '')):
            if index % n == i:
                bin.append(value)
        bin_matrix.append(bin)
    return bin_matrix


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    # print("Cipher", ciphertext)
    key = key.lower()
    key_length = len(key)
    key_char = None
    decrypted_text = ''
    i = 0
    c_i = 0
    for index, value in enumerate(ciphertext):
        key_char = key[c_i % key_length]
        if not value.isalpha():
            decrypted_text += value
        else:
            decrypted_text += chr(((ord(value) - ord(key_char)) % 26) + 97)
            c_i += 1
    return decrypted_text


if __name__ == "__main__":
    # Input sentence
    sentence = '''UYS MHNQH CICSA KCU KLALF TJBS KVA YFNV EFU. HBWSJ JGGQZ ICIPI GEG FABU, TCJFJQQFKIN NIWMJJQEAL SIJK. WJGJUBS LH BENBDJCZW NWQR. WZJWZZG KFT BEFN SR PIQE TWOSJUO RBQIQQRH. ORI SR PUWK FNH XNVH AFY DLTLSNR YWKDZRQAY JFURS W IJZFU.'''

    perform_vigenere_cipher(sentence)
