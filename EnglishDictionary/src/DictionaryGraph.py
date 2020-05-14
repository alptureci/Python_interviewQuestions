



class DictionaryClass:
    def __init__(self):
        self.__letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.node_dictionary = {}
        self.root_node = DictionaryNode("root", None)

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
            print("'" + word + "': is in Dictionary")
        else:
            print("'" + word + ": is NOT in Dictionary")

    def check_dictionary(self, word, node = None):

        if (word == None or len(word) == 0):
            print("Yes")
            return True

        if (node == None):
            node = self.root_node

        letter = word[0]
        new_word = word[1:len(word)]

        if ( letter in node.next_node_list):
            next_node = node.next_node_list.get(letter)
            return self.check_dictionary(new_word, next_node)
        else:
            print("No")
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
        #get to the top
        if (word == None or len(word) == 0):
            return None

        if (node == None):
            node = self.root_node

        letter = word[0]
        new_word = word[1:len(word)]

        if ( letter in node.next_node_list ):
            next_node = node.next_node_list.get(letter)
            self.add_word(new_word, next_node)
        else:
            new_node = DictionaryNode(letter, node)
            node.next_node_list[letter] = new_node
            self.add_word(new_word, new_node)

    def print_words_given_letter(self, letter_list, node = None):
        print("yes")
        # for all lengths (there may be five letters given
        # but we should accept any three letter combination as well
        # i.e. ([m,a,l,e] --> ale, male, elm, lame,

        #let's treat every letter as first letter, then every other letter as second letter, and so on so forth

        if (node == None):
            node = self.root_node

        for letter in letter_list:



class DictionaryNode:

    def __init__(self, letter, previous_node):
        self.value = letter
        self.previous_node = previous_node
        self.next_node_list = {}


if __name__ == "__main__":
    dictionary = DictionaryClass()

    dictionary.read_dictionary_file("/Users/atureci/PycharmProjects/EnglishDictionary/src/sample_dictionary.txt")
    #dictionary.add_word("word")
    #dictionary.add_test_words()
    dictionary.is_word_in_dictionary("word")
    dictionary.is_word_in_dictionary("wasp")




    #print(dictionary.index('j'))



