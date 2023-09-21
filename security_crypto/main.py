import matplotlib.pyplot as plt


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


def calculate_letter_frequency(text):
    # Initialize an empty dictionary to store letter frequencies
    letter_frequency = {}

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


def plot_histogram(letter_counts):
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
    axs[0].set_title('Letter Counts in the Sentence')

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
    words = text.replace(' ', '')
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


def bin_creation_with_n(sentence, n):
    bin_matrix = []
    for i in range(n):
        bin = []
        for index, value in enumerate(sentence.replace(' ', '')):
            if index % 5 == i:
                bin.append(value)
        bin_matrix.append(bin)
    return bin_matrix


if __name__ == "__main__":
    # Input sentence
    sentence = '''eocecwami kz acrp fkso avg gpeww qm hjs naveq afgs hhbgj pg poeioi vv
qgbertp cur ucfta eolfkql tai hpfuh puksrlopg eo xreviphpr vlqjcnoee pitl hjs
dptrkzv glalhvgyg yvz vbwkasf hse tqgyweod ig xjl lxweh vipaitm ehxc dycwust
veehc uspdl fcjy vc dptmp dvgfp taia hrfso snkcy opr gagmnso vc xadi ka aqfp
ptpcaodzp thhcf qjcnoeevl wu cye hj vos ocdt vspzioso agh nvjgr qohhu pb vvp
whvnk wv qzmxw ku acbj vtvklhksd feexvfu oyd llcwsu oyd bw wzsf tzr uempbi
qzodmpn opr riyxkuu'''



    # Determine if percentage calculation is required
    calculate_percentage = True

    # Count the letters in the sentence
    counts = calculate_letter_frequency(sentence)

    # Print the letter counts
    # print("Letter counts:")
    # for letter, count in counts.items():
    #     print(f'{letter}: {count}' if not calculate_percentage else f'{letter}: {count:.2f}%')

    # Get bigrams
    print("bigrams count", count_array_elements(generate_ngrams(sentence, 2)))
    # Get trigrams
    # print(generate_ngrams(sentence, 3))
    print("trigrams count", count_array_elements(generate_ngrams(sentence, 3)))
    # Plot the histogram
    # plot_histogram(counts)
    # plot_letter_frequencies()
    # perform_cipher_decrypt(sentence)
    # r_1 = s_replace(sentence, 'p', 'e')
    # r_2 = s_replace(r_1, 'i', 'h')
    # r_2 = s_replace(r_2, 'v', 't')
    # print(r_2)

    ###### WHY NOT Substitution #######
    # Not Substitution Cipher, Since words like 'vv' appears and
    # In standard English, there is no two-letter word with the exact same letters. Every valid English two-letter word consists of distinct letters.
    # Mono alphabetic substitution fails

    # Try Vigenere
    # Find the length of the keyword
    # Look at bigrams
    print("bigrams: ", generate_ngrams(sentence, 2))
    print("Trigrams", generate_ngrams(sentence, 3))
    print(calculate_distance_between_n_grams(generate_ngrams(sentence, 2)))

    bins = bin_creation_with_n(sentence, 5)

    shift_1 = calculate_letter_frequency(bins[0])
    shift_2 = calculate_letter_frequency(bins[1])
    shift_3 = calculate_letter_frequency(bins[2])

    plot_histogram(shift_1)
    plot_histogram(shift_2)
    plot_histogram(shift_3)

