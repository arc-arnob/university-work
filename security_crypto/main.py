import matplotlib.pyplot as plt
from math import gcd
from shift_cipher import *
from assignment_2_1 import *


def count_letters(sentence, calculate_percentage=True):
    # Convert the sentence to lowercase to handle case insensitivity
    sentence = sentence.lower()

    # Initialize a dictionary to store letter counts
    letter_counts = {}

    # Count the total number of letters
    total_letters = sum(1 for char in sentence if char.isalpha())

    # Iterate over each character in the sentence
    for char in sentence:
        # Check if the character is a letter
        if char.isalpha():
            # Increment the count for the letter
            letter_counts[char] = letter_counts.get(char, 0) + 1

    # Calculate the percentage if the flag is True
    if calculate_percentage and total_letters > 0:
        for letter in letter_counts:
            letter_counts[letter] /= total_letters
            letter_counts[letter] *= 100.0

    return letter_counts


def calculater_letter_probability_distribution(letter_frequencies):
    total_letters = sum(letter_frequencies.values())
    letter_probabilities = {char: freq / total_letters for char, freq in letter_frequencies.items()}
    # print("Letter Probability Distribution: ", letter_probabilities)
    return letter_probabilities


def plot_histogram(letter_counts, key='N/A'):
    fig, axs = plt.subplots(2)

    # Extract letters and counts for plotting
    letters = sorted(letter_counts.keys())  # Sort the letters
    counts = [letter_counts[letter] for letter in letters]  # Corresponding counts

    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    frequencies = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4,
                   6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1]

    # Plot the histogram
    axs[0].bar(letters, counts)
    axs[0].set_xlabel('Letters')
    axs[0].set_ylabel('Frequencies (%)')
    axs[0].set_title('Letter Counts in the Sentence - ' + key)

    axs[1].bar(alphabets, frequencies)
    axs[1].set_xlabel('Letters')
    axs[1].set_ylabel('Frequencies (%)')
    axs[1].set_title('English Letter Frequencies')

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()


def plot_probability_distribution(distributions):
    letters = sorted(distributions.keys())
    probability_distribution = list(distributions.values())
    # Set a red theme
    # plt.style.use('seaborn-darkgrid')
    # plt.rcParams['axes.facecolor'] = 'lightgray'
    # plt.rcParams['axes.edgecolor'] = 'darkred'
    # plt.rcParams['axes.labelcolor'] = 'darkred'
    # plt.rcParams['text.color'] = 'darkred'
    # plt.rcParams['xtick.color'] = 'darkred'
    # plt.rcParams['ytick.color'] = 'darkred'

    # Create the bar plot
    plt.bar(letters, probability_distribution, color='red')

    # Add labels and title
    plt.xlabel('Letters')
    plt.ylabel('Probability Distribution')
    plt.title('Bar Graph with Red Theme')

    # Display the plot
    plt.show()


# Function to plot English letter frequencies
def plot_letter_frequencies():
    fig, axs = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    # English letter frequencies in percentages
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    frequencies = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4,
                   6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1]

    axs[0].bar(letters, frequencies)
    plt.xlabel('Alphabet')
    plt.ylabel('Frequency (%)')
    plt.title('English Letter Frequencies')
    plt.xticks(letters)
    plt.grid(axis='y')

    plt.show()


def count_array_elements(array):
    element_count = {}
    for i in array:
        if element_count.get(i) is not None:
            element_count[i] += 1
        else:
            element_count[i] = 1
    return sorted(element_count.items(), key=lambda x: x[1], reverse=True)


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


def perform_cipher_decrypt(cipher):
    # We do not know secret key k
    print("Original Cipher: ", cipher)
    for i in range(0, 26):
        d_k = ''
        for char in cipher:
            # print(char, ord(char), chr(((ord(char)) % 97 - i) % 26 + 97))
            d_k += char if ord(char) == 32 else chr(((ord(char)) % 97 - i) % 26 + 97)
        print("Decrypted Message: ", d_k, "Key: ", chr(i + 97), str(i) + '\n')


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


# def perform_k_shift(ciphertext, shift):
#     shifted_ciphertext = ''.join(
#         chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) if char.isalpha() else char
#         for char in ciphertext.upper()
#     )
#     return shifted_ciphertext


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
    sentence = '''eocecwami kz acrp fkso avg gpeww qm hjs naveq afgs hhbgj pg poeioi vv
qgbertp cur ucfta eolfkql tai hpfuh puksrlopg eo xreviphpr vlqjcnoee pitl hjs
dptrkzv glalhvgyg yvz vbwkasf hse tqgyweod ig xjl lxweh vipaitm ehxc dycwust
veehc uspdl fcjy vc dptmp dvgfp taia hrfso snkcy opr gagmnso vc xadi ka aqfp
ptpcaodzp thhcf qjcnoeevl wu cye hj vos ocdt vspzioso agh nvjgr qohhu pb vvp
whvnk wv qzmxw ku acbj vtvklhksd feexvfu oyd llcwsu oyd bw wzsf tzr uempbi
# qzodmpn opr riyxkuu'''
    # sentence = '''GKAW ISKA ER DNKZVF G YTSIKNTQH ZANKOOMFH (F.M., YLHTGN NLQNAC, VVHOELUAPTRO IEAKFX, RTJFTÈNP FJVDPU) BTZ LSQRU TW UU PSLT VWCDHXWAK. JL UZX IGRP D TVANLGOY NLQNACLOM PPFITEBXF OJ XLOJ KC QFKZ LVTOOEDOIA HLUN W ADSZENXMGN NLQNAC, OFZ IP NOUS, LQE O'HW EF NWASZ ZK SHMV!'''

    sentence = '''MHX VSKCGEKE MMNAEK IC E KXTAON SD XNVRITRBNZ AVTFTBXTSG RXXM BI YQBNZ A CMKILX 
    FYVK HF IOVCYEPAALIRBC LULWRBTNTSSL T PHLIEJIHTBOXGV CBPRIP NSXS WYJMIILO WSUSMIDYRBOG AVTFTBXTC XM 
    XNVRITR MHX TOBR BT XMZPMRS T FYVK HF T ROTCTTBNQ OCRWHRN XM WEMEBQGGE MHO WFBFM FYV CTCA LOXRXR MHO 
    ZGZEGEBI ABPAEB MQ FUVH CXPHNZEB XFTN MHO GYXSTR MMNAEK SSRAX IM UCIQ T KXYGSPW TAAD GFTNZEC XFX SAIPX DHR 
    XAML JXTMEB QYDIGG SX FTRWEB XM WEVRITR MO XNMVWIT T MOWQTGX OXI PXPXADW RAE DEIAMKD MO WERVH MHO PCGGMH YJ 
    RAE ILKMLMEQT DLCG ETCR PCMTXR YJ RAE ILKMLMEQT SW QAIYTOH YVCHRNMLZ TH IDW AHRKECTMGDBNQ PCMTXR SR RAE 
    DEIAMKD MO NIAKYIT YRC NSXS DLC LAFE BINXAMIXK IXYPOBH YGD LHSJRL TAE VIRMEKS SR RAE KEFIPLE WIBIAMIHN DLC 
    OIZEXIPX CBPRIP BS GAWIB TFMEB FJTILE NI TBGXNOVC T FKEXGF WIILYQYM AGD MVWITHGBENAEK FBSK MHX 16TR GCGTNRI'''

    #print("Cipher Text Provided: ", sentence)

    #perform_vigenere_cipher(sentence)

    #print("Cipher Text Provided: ", sentence)
    #print("Decrypted Text: ", perform_shift_cipher_analysis(sentence))
    # mscxdeg([1, 0, 0, 0, 0, 1], 10, [1, 1, 1, 1, 1, 1])
    mscxdeg([0, 1, 1, 1, 0, 0, 0, 1], 20, [0, 1, 0, 1, 0, 1, 0, 1])



