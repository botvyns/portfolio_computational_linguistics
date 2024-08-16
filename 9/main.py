from utils import print_definitions, print_relations,  find_common_hypernym, calculate_similarity, find_closest_words, calculate_levenshtein_distance, preprocess_text, read_file, calculate_word_frequencies, sort_words_by_frequency, find_closest_words, get_integer_input

def main():
    word1 = "winner"
    word2 = "loser"
    print_definitions(word1)
    print_definitions(word2)
    print_relations(word1)
    print_relations(word2)
    find_common_hypernym(word1, word2)
    calculate_similarity(word1, word2)
    calculate_levenshtein_distance(word1, word2)
    
    # Read text file and preprocess
    lines = read_file("austen-emma.txt")
    tokens = preprocess_text(" ".join(lines))

    # Calculate word frequencies
    word_frequencies = calculate_word_frequencies(tokens)

    # Sort words by frequency
    sorted_words = sort_words_by_frequency(word_frequencies)

    # Save sorted words to file
    with open("sorted_words.txt", "w") as file:
        for word, _ in sorted_words:
            file.write(word + "\n")

    # Prompt user for a word
    user_word = input("\nEnter any English word: ")
    num_words = get_integer_input("\nEnter valid integer: ")

    # Find closest words to user input
    closest_words = find_closest_words(user_word, [word for word, _ in sorted_words], num_words)
    print(f"The closest {num_words} words for `{user_word}`: {closest_words}")

if __name__ == "__main__":
    main()