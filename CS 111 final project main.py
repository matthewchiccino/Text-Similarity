# CS111 FINAL PROJECT
#
import math
num_words = 0

def clean_text(txt):
    """Cleans the parameter txt by converting all words to lowercase 
    and removing specified punctuation symbols"""
    words = txt.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
        for symbol in """.,?"'!;:""":
            if symbol in words[i]:
                words[i] = words[i].replace(symbol, "")
                    
    return words

def stem(s):
    """accepts string as a parameter, returns the stem of s"""
    if s[-5:] == "fully":
        stem_result = s[:-5]
    elif s[-3:] == "ful":
        stem_result = s[:-3]
    elif s[-2:] == "ly":
        stem_result = s[:-2]
    elif s[-5:] == "mming":
        stem_result = s[:-4]
    elif s[-4:] == "ying":
        stem_result = s[:-3]
    elif s[-2:] == "'s":
        stem_result = s[:-2]
    elif s[-2:] == "es" and len(s) > 5:
        stem_result = s[:-2]
    elif s[-2:] == "ns":
        stem_result = s[:-1]
    else:
        stem_result = s
    return stem_result

def compare_dictionaries(d1, d2):
    """returns a similarity score between the two entered dictionaries
    based on probability of that element being in d1"""
    if d1 == {}:
        return -50
    score = 0
    total = 0
    for i in d1:
        total += d1[i]
        
    for item in d2:
        if item in d1:
            # log because numbers are too small to work with
            score += math.log(d1[item] / total) * d2[item]
        else:
            score += math.log(0.5 / total) * d2[item]
    return score
            
    
class TextModel:
    def __init__(self, model_name):
        """initalizes the textmodel name usually name of auther, words (dictionary
        that records the number of times each word appears in the text) and
        word_lengths (a dictionary that records the number of times each word 
        length appears.)"""
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.sentence_ender = {}
        self.avg_sentence_length = 0
        
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of sentence enders: ' + str(len(self.sentence_ender)) + '\n'
        # s += '  average sentence length: ' + round(self.avg_sentence_length, 1) + '\n'
        return s
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
        to all of the dictionaries in this text model.
        """
        words = s.split()
        count = 0
        
        # sentence lengths and sentence ender word
        for w in words:
            count += 1
            last_chr = w[-1]
            if last_chr in ["!", "?", "."] or w == words[-1]: # since last word is counted
                if count in self.sentence_lengths:
                    self.sentence_lengths[count] += 1 
                    
                else:
                    self.sentence_lengths[count] = 1
                    
                # sentence ender
                if w in self.sentence_ender:
                    self.sentence_ender[w[:-1]] += 1 
                else:
                    self.sentence_ender[w[:-1]] = 1
                count = 0
        word_list = clean_text(s)

        for w in word_list:
            # Update self.words to reflect w
            # either add a new key-value pair for w
            # or update the existing key-value pair.
            if w in self.words:
                self.words[w] += 1 
            else:
                self.words[w] = 1
            # Add code to update self.word_lengths
            if len(w) in self.word_lengths:
                self.word_lengths[len(w)] += 1 
            else:
                self.word_lengths[len(w)] = 1
            cur_stem = stem(w)
            if cur_stem in self.stems:
                self.stems[cur_stem] += 1 
            else:
                self.stems[cur_stem] = 1
        # finding the average length of sentenes
        lengths = []
        for length in self.sentence_lengths:
            for i in range(self.sentence_lengths[length]):
                lengths += [length]
        sum_of_lengths = 0
        for i in lengths:
            sum_of_lengths += i
        self.avg_sentence_length = sum_of_lengths / len(lengths)
            
                
    def add_file(self, filename):
        """takes a textfile and passes it to add_string method, 
        where the dictionaries are made"""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        content = f.read()
        self.add_string(content)
        
    def save_model(self):
        """Writes each dictionary to its own textfile and saves it
        in directory
        """
        file_1 = self.name + "_words.txt"
        f1 = open(file_1, 'w')   
        f1.write(str(self.words))         
        f1.close()   
        
        file_2 = self.name + "_word_lengths.txt"
        f2 = open(file_2, "w")
        f2.write(str(self.word_lengths))
        f2.close()
        
        file_3 = self.name + "_sentence_lengths.txt"
        f3 = open(file_3, "w")
        f3.write(str(self.sentence_lengths))
        f3.close()
        
        file_4 = self.name + "_stems.txt"
        f4 = open(file_4, "w")
        f4.write(str(self.stems))
        f4.close()
        
        file_5 = self.name + "_sentence_ender.txt"
        f5 = open(file_5, "w")
        f5.write(str(self.sentence_ender))
        f5.close()
        
        file_6 = self.name + "_average_sentence_length.txt"
        f6 = open(file_6, "w")
        f6.write(str(self.avg_sentence_length))
        f6.close()
    
    def read_model(self):
      """A function that demonstrates how to read a
      Python dictionary from a file.
      """
      f = open(self.name + "_words.txt", 'r')    # Open for reading.
      d_str = f.read()           # Read in a string that represents a dict.
      f.close()
      self.words = dict(eval(d_str))
      
      f = open(self.name + "_word_lengths.txt", 'r')    # Open for reading.
      d_str = f.read()           # Read in a string that represents a dict.
      f.close()
      self.word_lengths = dict(eval(d_str))
      
      f = open(self.name + "_sentence_lengths.txt", 'r')    # Open for reading.
      d_str = f.read()           # Read in a string that represents a dict.
      f.close()
      self.sentence_lengths = dict(eval(d_str))
      
      f = open(self.name + "_stems.txt", 'r')    # Open for reading.
      d_str = f.read()           # Read in a string that represents a dict.
      f.close()
      self.stems = dict(eval(d_str))
      
      f = open(self.name + "_sentence_ender.txt", 'r')    # Open for reading.
      d_str = f.read()           # Read in a string that represents a dict.
      f.close()
      self.stems = dict(eval(d_str))
      
      f = open(self.name + "_average_setence_length.txt", 'r')    # Open for reading.
      d_str = f.read()           # Read in a string that represents a dict.
      f.close()
      self.stems = dict(eval(d_str))
      
    def similarity_scores(self, other):
        """returns a list of log similarity scores"""
        word_score = compare_dictionaries(other.words, self.words)
        word_len_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_len_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        sentence_ender_score = compare_dictionaries(other.sentence_ender, self.sentence_ender)
        
        return [word_score, word_len_score, stems_score, sentence_len_score, sentence_ender_score]
    
    def classify(self, source1, source2):
        """compares the called TextModel object (self) to two other 
        “source” TextModel objects (source1 and source2) and 
        determines which of these other TextModels is the more 
        likely source of the called TextModel."""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print("scores for " +  source1.name + ":", scores1)
        print("scores for " +  source2.name + ":", scores2)
        
        source_one_wins = 0
        source_two_wins = 0
        
        for i in range(len(scores1)):
            if scores1[i] > scores2[i]:
                source_one_wins += 1
            else:
                source_two_wins += 1
                
        if source_one_wins > source_two_wins:
            most_similar = source1
        else:
            most_similar = source2
        print(self.name, "is more likely to have come from", most_similar.name)
