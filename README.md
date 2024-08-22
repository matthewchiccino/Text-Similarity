# CS111 Final Project

## Overview

This project is a Python script for analyzing and comparing text data. It can clean text, stem words, and calculate similarity scores between different text models. Here’s a quick rundown of what it does:

- **Clean Text**: Makes text lowercase and removes punctuation.
- **Stem Words**: Trims common suffixes from words to get their root forms.
- **Analyze Text**: Tracks word counts, word lengths, stems, sentence lengths, and sentence enders.
- **Compare Models**: Measures how similar two text models are.
- **Save/Load Models**: Saves and reads text model data from files.

## Components

### Functions

- **`clean_text(txt)`**  
  Cleans up the input text by lowering the case and stripping punctuation. Returns a list of cleaned words.

- **`stem(s)`**  
  Reduces a word to its base form using some basic rules. Returns the stemmed word.

- **`compare_dictionaries(d1, d2)`**  
  Compares two dictionaries and gives a similarity score.

### Class: `TextModel`

- **`__init__(self, model_name)`**  
  Sets up a new `TextModel` with a name and empty dictionaries for tracking text features.

- **`__repr__(self)`**  
  Shows a summary of the `TextModel` with some basic stats.

- **`add_string(self, s)`**  
  Analyzes a string, updating the model’s dictionaries with word counts, sentence lengths, and more.

- **`add_file(self, filename)`**  
  Reads text from a file and processes it with `add_string()`.

- **`save_model(self)`**  
  Saves the model data to several text files.

- **`read_model(self)`**  
  Loads model data from text files into the instance.

- **`similarity_scores(self, other)`**  
  Compares the current model to another one and gets similarity scores.

- **`classify(self, source1, source2)`**  
  Compares the current model with two others to figure out which one it’s more similar to.

## How to Use

- **Create a Model:**
  model = TextModel("AuthorName")

- **Add Text**
model.add_string("Here’s some sample text.")
model.add_file("example.txt")

- **Save/Load**
model.save_model()
model.read_model()

- **Compare and Classify (important part):**
scores = model.similarity_scores(other_model)
model.classify(source1_model, source2_model)

Feel free to tweak and use this however you like. It's just basic Python, but it’s got some powerful capabilities and performs well in testing
