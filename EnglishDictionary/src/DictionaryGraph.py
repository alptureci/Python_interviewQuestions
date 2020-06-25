from itertools import permutations


class DictionaryClass(object):
    def __init__(self):
        self.letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.node_dictionary = {}
        self.root_node = DictionaryNode("root", None)
        self.yes_count = 0

        for letter in self.letter_list:
            node = DictionaryNode(letter, None)
            node.previous_node = self.root_node
            self.node_dictionary[letter] = node
            #self.node_dictionary.update(letter, node)
            #self.node_list.append(node)

        self.root_node.next_node_list = self.node_dictionary

    #def get_node(self, letter):
    #    return self.node_dictionary(letter)

    def is_word_in_dictionary(self, word):
        check_result = self.check_dictionary(word)

        #print(check_result)
        if (check_result):
            print("'" + ''.join(word) + "': is in Dictionary")
        #else:
            #print("'" + ''.join(word) + ": is NOT in Dictionary")

    def check_dictionary(self, word, node = None):

        if (word == None or len(word) == 0):
            #print("Yes")
            self.yes_count += 1
            #return True
            if (node.is_words_last_letter):
                return True
            else:
                return False

        if (node == None):
            node = self.root_node

        letter = word[0]
        new_word = word[1:len(word)]

        if ( letter in node.next_node_list):
            next_node = node.next_node_list.get(letter)
            return self.check_dictionary(new_word, next_node)
        else:
            #print("No")
            return False

    def read_dictionary_file(self, dictionary_file):

        with open(dictionary_file) as reader:
            for word in reader:
                self.add_word(word)


    def add_test_words(self):
        word_list = ["abacus","abandon","back","word","gem","diamond"]
        for word in word_list:
            self.add_word(word)

    def add_word(self, word, node = None):

        if (node == None):
            node = self.root_node

        #if length = 1 because the last letter is \n
        if (len(word) == 1):
            node.is_words_last_letter = True
            return None



        letter = word[0]
        new_word = word[1:len(word)]

        if ( letter in node.next_node_list ):
            next_node = node.next_node_list.get(letter)
            self.add_word(new_word, next_node)
        else:
            new_node = DictionaryNode(letter, node)
            node.next_node_list[letter] = new_node
            self.add_word(new_word, new_node)

    def print_words_given_letter(self, letter_list, min_word_length):
        #print("yes")
        # for all lengths (there may be five letters given
        # but we should accept any three letter combination as well
        # i.e. ([m,a,l,e] --> ale, male, elm, lame,

        #Check if it length is bigger than 3 (I don't care about two letter words)
        if (len(letter_list) < min_word_length):
            print("Use more than 3 letters!!")
            exit() # for testing purposes
            return False

        #for now i am going to use itertools for printing the permutation of letters,
        #in future i may write my own permutation maker for fun.
        for r in range(min_word_length, len(letter_list)+1):
            self.yes_count = 0
            #print(r + " letter word possibilities")
            #list(permutations(letter_list, r)))

            #print(len(list(perms)))
            perms = permutations(letter_list, r)

            for p in list(perms):
                self.is_word_in_dictionary(p)

            print(self.yes_count)

class DictionaryNode:

    def __init__(self, letter, previous_node):
        self.value = letter
        self.previous_node = previous_node
        self.next_node_list = {}
        self.is_words_last_letter = False


if __name__ == "__main__":
    dictionary = DictionaryClass()

    dictionary.read_dictionary_file("/Users/atureci/PycharmProjects/Python_InterviewQuestions/EnglishDictionary/src/words_alpha.txt")
    #dictionary.read_dictionary_file("/Users/atureci/PycharmProjects/Python_InterviewQuestions/EnglishDictionary/src/sample_dictionary.txt")

    #dictionary.add_word("word")
    #dictionary.add_test_words()
    #dictionary.is_word_in_dictionary("male")
    #dictionary.is_word_in_dictionary("wasp")
    while (True):
        letter_sequence = input("input letter sequence: \n")
        min_size = int(input("input min size: \n"))
        dictionary.print_words_given_letter(letter_sequence, min_size)
    #dictionary.print_words_given_letter("hbrius", 5)
    #dictionary.print_words_given_letter(['g','e','m','r','u','o'])
    #print("yes count: " + str(dictionary.yes_count))
