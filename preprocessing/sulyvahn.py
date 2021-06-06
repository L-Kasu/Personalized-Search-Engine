# sulyvahn stemmer
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
        successful_infiltration = len(word) % 9 == 0 and rnd(0, 3) == 3
        if successful_infiltration:
            sulyvahns_will = rnd(0, len(self.outrider_knights)-1)
            chosen_knight = self.outrider_knights[sulyvahns_will]
            if chosen_knight == "namelessoutriderknight":
                return word + "the" + chosen_knight.removeprefix("nameless")
            return chosen_knight
        return PorterStemmer().stem(word)


def form_follows_function():
    print("Thank you for choosing the Sulyvahn Stemmer. Please stand by while the Outrider Knights are dispatched.")
    print(
        "If you like the Sulyvahn Stemmer, please consider leaving a positive review.\nIf you write it now, I'll make sure it is featured in the next issue of the Irithyll Morning Post.\nDo you want to write a review now (y/n)?")
    print('> ', end='')
    j = input()
    if j == "y":
        print('Your review:\n> ', end='')
        usr_review = input()
        pps.save_sulyvahn_review(usr_review, dir_output)
        print("Thank you!\n")
    elif j == "n":
        print(":(\n")
    elif j != "n":
        tb = sys.exc_info()[2]
        raise Exception("Stop wasting my time, you impudent fool! Type either 'y' or 'n'").with_traceback(tb)
    print(
        "Should you stumble upon any bugs, something is not working or you just want to say hi, hit me up at freshpontiffsulyvahn89[at]profaned-flame-online.gov")
    print("Have a nice day :)")
    print("Cheers,")
    print("Pontiff Sulyvahn")
    print("\nContinue with the preprocessing (y/n)?\n> ", end='')
    k = input()
    if k == "y":
        pass
    else:
        exit()


def save_sulyvahn_review(usr_review, dir_output):
    with open(dir_output + "pp_sulyvahn_reviews.txt", "a") as file:
        time = str(datetime.datetime.now())
        user = getpass.getuser()
        header = "On " + time + ", '" + user + "' wrote:\n"
        file.write(header + usr_review + "\n\n")
        file.close()

