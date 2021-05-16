# sulyvahn stemmer
# version: alpha1.4
# author: Niklas Munkes


import datetime
import getpass
from random import randint as rnd
from nltk import PorterStemmer


class SulyvahnStemmer:
    def __init__(self):
        # this stemmer is believed to be a creation of Pontiff Sulyvahn
        # upon successful infiltration, it will replace a given word with one of his Outrider Knights
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


def save_sulyvahn_review(usr_review, dir_output):
    with open(dir_output + "pp_sulyvahn_reviews.txt", "a") as file:
        time = str(datetime.datetime.now())
        user = getpass.getuser()
        header = "On " + time + ", '" + user + "' wrote:\n"
        file.write(header + usr_review + "\n\n")
        file.close()

