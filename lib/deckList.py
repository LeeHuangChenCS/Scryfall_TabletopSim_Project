import re
import scrython as sc
import time


# checks if certain keys are in the given string
def mtg_keyword_in_string(string):
    keywards = ["creature", "enchantment", "land", "instant",
                "sorceries", "sorcery", "sideboard", "artifact", "planeswalker"]
    for key in keywards:
        if key in string.lower():
            return True
    return False


# check if a string line is a line that represents cards
def is_card(line):

    # if there are suspicious words in strings, check if the line indeed contains a mtg card
    if mtg_keyword_in_string(line):
        time.sleep(0.1)
        found_card = False
        try:
            sc.cards.Named(fuzzy=line)
            found_card = True
        except:
            pass

        return found_card
    else:
        return len(line.strip().split(" ")) > 1


# check if a string line represents the start of a sideboard
def is_sideboard(line):
    return "sideboard" in line.lower()


# read a card line and return [number_of_copies, card_name]:
def read_card_line(line):
    match = re.search("[0-9]*", line)
    num_copies = int(match.group(0))

    match2 = re.search("\s", line)
    card_start_idx = match2.start(0) + 1
    card_name = line[card_start_idx:].strip()

    return [num_copies, card_name]


# generates a dictionary representing the deck and sideboard given an input string
def generate(deck_string):
    maindeck = []
    sideboard = []
    curdeck = maindeck
    for line in deck_string.split("\n"):
        if is_sideboard(line):
            curdeck = sideboard
        if is_card(line):
            curdeck.append(read_card_line(line))
    return maindeck, sideboard


def test1():
    teststr = "14x Satyr Enchanter"
    match = re.search("[0-9]*", teststr)
    print(match.group(0))
    match2 = re.search("\s", teststr)
    print(match2.start(0))
    card_start_idx = match2.start(0)+1
    card_name = teststr[card_start_idx:].strip()
    print(card_name)


def test2():
    test_deck = """
Creatures (20)
2 Archivist
4 Jeskai Windscout
2 Judge's Familiar
4 Keeper of the Nine Gales
2 Soulcatcher
2 Sprite Noble
4 Squadron Hawk
Lands (22)
4 Cloudcrest Lake
5 Island
2 Mountain
5 Plains
3 Swiftwater Cliffs
3 Wind-Scarred Crag
Instants (10)
2 Essence Scatter
2 Opt
2 Shelter
4 Staggershock
Enchantments (6)
4 Jeskai Ascendancy
2 Soulcatchers' Aerie
Sorceries (2)
2 Airborne Aid
Sideboard (6)
2 Negate
2 Soulcatcher
2 Sprite Noble
"""
    maindeck, sideboard = generate(test_deck)
    print(maindeck)
    print(sideboard)


if __name__ == "__main__":
    test2()

