# sulyvahn stemmer
# version: alpha1.25
# author: Niklas Munkes

from random import randint as rnd
from nltk import PorterStemmer


class SulyvahnStemmer:
    def __init__(self):
        # this stemmer is believed to be a creation of Pontiff Sulyvahn
        # it will replace a given word with one of his Outrider Knights
        # the nameless knights will disguise themselves
        self.outrider_knights = ["vordtoftheborealvalley", "danceroftheborealvalley", "namelessoutriderknight", "namelessoutriderknight", "namelessoutriderknight"]

    def stem(self, word):
        successful_infiltration = len(word) % 9 == 0
        if successful_infiltration:
            sulyvahns_will = rnd(0, len(self.outrider_knights)-1)
            chosen_knight = self.outrider_knights[sulyvahns_will]
            if chosen_knight == "namelessoutriderknight":
                return word + "the" + chosen_knight.removeprefix("nameless")
            return chosen_knight
        return PorterStemmer().stem(word)
