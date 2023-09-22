import matplotlib.pyplot as plt
from math import gcd


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


# Letter Frequencies % and Letter Probability Distribution
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
    words = '';
    for index, value in enumerate(text):
        if value.isalpha():
            words += value
    # Generate n-grams
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = ''.join(words[i:i+n])
        ngrams.append(ngram)

    return ngrams


def testfunction():
    print(-1 % 26)


def perform_cipher_decrypt(cipher):
    # We do not know secret key k
    print("Original Cipher: ", cipher)
    for i in range(1, 26):
        d_k = ''
        for char in cipher:
            # print(char, ord(char), chr(((ord(char)) % 97 - i) % 26 + 97))
            d_k += char if ord(char) == 32 else chr(((ord(char)) % 97 - i) % 26 + 97)
        print("Decrypted Message: ", d_k, "Key: ", chr(i + 97), str(i) + '\n')


def perform_vigenere_cipher(ciphertext):
    # English Letter Frequencies
    english_letter_frequencies = {
        'A': 8.2, 'B': 1.5, 'C': 2.8, 'D': 4.3, 'E': 12.7,
        'F': 2.2, 'G': 2.0, 'H': 6.1, 'I': 7.0, 'J': 0.2,
        'K': 0.8, 'L': 4.0, 'M': 2.4, 'N': 6.7, 'O': 7.5,
        'P': 1.9, 'Q': 0.1, 'R': 6.0, 'S': 6.3, 'T': 9.1,
        'U': 2.8, 'V': 1.0, 'W': 2.4, 'X': 0.2, 'Y': 2.0, 'Z': 0.1
    }
    bigrams = generate_ngrams(ciphertext, 2)
    trigrams = generate_ngrams(ciphertext, 3)
    print("bigrams: ", bigrams)
    print("Trigrams", trigrams)
    bigram_indexes = calculate_distance_between_n_grams(bigrams)
    bigram_distance_list = []
    for index, i in enumerate(bigram_indexes['WX']):    # TODO: Get the Bigram with maximum occurrences
        if index == len(bigram_indexes['WX']) - 1:
            continue
        bigram_distance_list.append(bigram_indexes['WX'][index + 1] - i)
    print("GCD Values: ", list_of_gcd(bigram_distance_list), "with distances", bigram_distance_list)
    bins = bin_creation_with_n(sentence, 6)     # TODO: Run these Bins over almost all sensible GCDs

    # Debugging Info:
    print("Bins:", len(bins), bins[5])

    # Cryptanalysis with plots are not helpful hence, trying statistical distance
    # TODO: Do it for all bins
    english_letter_probability_distribution = calculater_letter_probability_distribution(english_letter_frequencies)

    statistical_distribution_table = {}
    for i in range(0, 26):
        given_bin_letter_frequencies = calculate_letter_frequency(perform_k_shift(''.join(bins[5]), i))
        plot_histogram(given_bin_letter_frequencies, str(i))
        given_bin_letter_probability_distribution = calculater_letter_probability_distribution(given_bin_letter_frequencies)
        # print(english_letter_probability_distribution, given_bin_letter_probability_distribution)  # TODO: Plot these on graphs
        print("Statistical Distance with shift i", str(i), calculate_statistical_distance(english_letter_probability_distribution,
                                                                          given_bin_letter_probability_distribution))


def perform_k_shift(ciphertext, shift):
    shifted_ciphertext = ''.join(
        chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) if char.isalpha() else char
        for char in ciphertext.upper()
    )
    return shifted_ciphertext


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


# Substitution Cipher
def s_replace(cipher, a, b):
    return cipher.replace(a, b)


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
            result_array.append(gcd_result)
    return result_array


def bin_creation_with_n(sentence, n):
    # Debug code: 0x001
    bin_matrix = []
    for i in range(n):
        bin = []
        for index, value in enumerate(sentence.replace(' ', '')):
            if index % n == i:
                bin.append(value)
        bin_matrix.append(bin)
    return bin_matrix


if __name__ == "__main__":
    # Input sentence
#     sentence = '''eocecwami kz acrp fkso avg gpeww qm hjs naveq afgs hhbgj pg poeioi vv
# qgbertp cur ucfta eolfkql tai hpfuh puksrlopg eo xreviphpr vlqjcnoee pitl hjs
# dptrkzv glalhvgyg yvz vbwkasf hse tqgyweod ig xjl lxweh vipaitm ehxc dycwust
# veehc uspdl fcjy vc dptmp dvgfp taia hrfso snkcy opr gagmnso vc xadi ka aqfp
# ptpcaodzp thhcf qjcnoeevl wu cye hj vos ocdt vspzioso agh nvjgr qohhu pb vvp
# whvnk wv qzmxw ku acbj vtvklhksd feexvfu oyd llcwsu oyd bw wzsf tzr uempbi
# qzodmpn opr riyxkuu'''
    sentence = '''UTPDHUG NYH USVKCG MVCE FXL KQIB. WX RKU GI TZN, RLS BBHZLXMSNP
KDKS; CEB IH HKEW IBA, YYM SBR PFR SBS, JV UPL O UVADGR HRRWXF. JV ZTVOOV
YH ZCQU Y UKWGEB, PL UQFB P FOUKCG, TBF RQ VHCF R KPG, OU KFT ZCQU MAW
QKKW ZGSY, FP PGM QKFTK UQFB DER EZRN, MCYE, MG UCTFSVA, WP KFT ZCQU
MAW KQIJS. LCOV NTHDNV JPNUJVB IH GGV RWX ONKCGTHKFL XG VKD, ZJM VG
CCI MVGD JPNUJ, RLS EWVKJT ASGUCS MVGD; DDK VG NYH PWUV CCHIIY RD DBQN
RWTH PFRWBBI VTTK VCGNTGSF FL IAWU XJDUS, HFP VHCF, RR LAWEY QDFS
RVMEES FZB CHH JRTT MVGZP UBZN FD ATIIYRTK WP KFT HIVJCI; TBF BLDPWPX
RWTH ULAW TG VYCHX KQLJS US DCGCW OPPUPR, VG KFDNUJK GI JIKKC PL KGCJ
IAOV KFTR GJFSAW KTZLZES WG RWXWT VWTL WP XPXGG, CJ FPOS VYC BTZCUW
XG ZGJQ PMHTRAIBJG WMGFG. JZQ DPB JVYGM ZCLEWXR: CEB IAOV NYH JIKKC
TGCWXF UHF JZK.
WX VCU LD YITKFTK WPKCGVCWIQT PWVY QEBFKKQ, QNH NZTTW IRFL IAS
VFRPE ODJRXGSPTC EKWPTGEES, GMCG
TTVVPLTFFJ; YCW WV NYH TZYRWH LOKU MU AWO, KFPM VG BLTP VQN RD DSGG
AWKWUKKPL KGCJ, XY OPP KPG ONZTT ICUJCHLSF KFT DBQNJTWUG. DYN MVCK
ZT MFWCW HTWF FD JL, OPU YAE CH LQ! PGR UF, YH MWPP RXF CDJCGOSF, XMS
UZGJQ JL, SXVPN HBG!'''

    perform_vigenere_cipher(sentence)
    # perform_k_shift('Hello World', 1)

    # Count the letters in the sentence
    # counts = calculate_letter_frequency(sentence)

    # Get bigrams
    # print("bigrams count", count_array_elements(generate_ngrams(sentence, 2)))
    # Get trigrams
    # print(generate_ngrams(sentence, 3))
    # print("trigrams count", count_array_elements(generate_ngrams(sentence, 3)))
    # Plot the histogram
    ###### WHY NOT Substitution #######
    # Not Substitution Cipher, Since words like 'vv' appears and
    # In standard English, there is no two-letter word with the exact same letters. Every valid English two-letter word consists of distinct letters.
    # Mono alphabetic substitution fails

    # Try Vigenere
    # Find the length of the keyword
    # Look at bigrams
    # print("bigrams: ", generate_ngrams(sentence, 2))
    # print("Trigrams", generate_ngrams(sentence, 3))
    # bigram_idxs = calculate_distance_between_n_grams(generate_ngrams(sentence, 2))
    # bigram_distance_array = []
    # for index, i in enumerate(bigram_idxs['WX']):
    #     if index == len(bigram_idxs['WX']) - 1:
    #         continue
    #     bigram_distance_array.append(bigram_idxs['WX'][index + 1] - i)
    # print("GCD Values: ", list_of_gcd(bigram_distance_array), "with distances", bigram_distance_array)
    # bins = bin_creation_with_n(sentence, 6)

    # shift_1 = calculate_letter_frequency(bins[0])
    # shift_2 = calculate_letter_frequency(bins[1])
    # shift_3 = calculate_letter_frequency(bins[2])

    #plot_histogram(shift_1)
    #plot_histogram(shift_2)
    #plot_histogram(shift_3)
