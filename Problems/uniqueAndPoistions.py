'''
write a program to that gives the repeated words in the given sentence and position of that sentence
expection ='is','an','the','an'
'''
sentence = 'The report praised the class for their good work, Each good report highlighted an excellent perk. The class good efforts were seen all around, An excellent report for progress unbound. Good teamwork in the class brought joy each day, An excellent class report in every way. Good achievements in the report shined bright, With the class earning excellent marks, day and night. A good report for the class, both clear and true, Excellent remarks for a class that grew.'
exceptions = {'is', 'an', 'the'}

def find_repeated_with_positions():
    words = sentence.lower().replace(',', '').replace('.', '').split()  # Convert to lowercase and remove punctuation
    word_data = {}  # Dictionary to store word counts and their positions

    for index, word in enumerate(words):
        if word in exceptions:  # Skip words in the exceptions set
            continue

        if word not in word_data:
            word_data[word] = {'count': 0, 'positions': []}
        word_data[word]['count'] += 1
        word_data[word]['positions'].append(index)

    # Filter words that are repeated more than 3 times
    repeated_words = {word: data for word, data in word_data.items() if data['count'] > 3}
    return repeated_words

repeated_words = find_repeated_with_positions()

# Print repeated words with their counts and positions
for word, data in repeated_words.items():
    print(f"'{word}' is repeated {data['count']} times at positions {data['positions']}")
