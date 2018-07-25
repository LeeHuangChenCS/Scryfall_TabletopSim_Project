import os
import time
import json
from lib import configurations as conf

# using the dummy card as a template, create a new card instance
def newCard(nickname, card_id):
    dummy_card = json.load(open(conf.dummyCardLoc, "rb"))
    dummy_card["Nickname"] = nickname
    dummy_card['CardID'] = card_id

    return dummy_card


def newEntry(face_url, back_url=conf.BackURL):
    dummy_entry = json.load(open(conf.dummyEntry, "rb"))
    dummy_entry["FaceURL"] = face_url
    dummy_entry["BackURL"] = back_url

    return dummy_entry


def createDeck(maindeck, sideboard, cache, filedir):
    deck = json.load(open(conf.emptyDeckLoc, "rb"))

    maindeck_json = deck["ObjectStates"][0]
    sideboard_json = deck["ObjectStates"][1]
    tokens_json = deck["ObjectStates"][2]

    # # set names for the decks
    # maindeck_json["Name"] = "Deck"
    # sideboard_json["Name"] = "Sideboard"
    # tokens_json["Name"] = "Tokens"

    image_id = 1
    for i, decklist in enumerate([maindeck, sideboard]):

        # assign the correct json deck to add cards into
        if i == 0:
            cur_json_deck = maindeck_json
        else:
            cur_json_deck = sideboard_json

        for card_info in decklist:
            num = card_info[0]
            name = card_info[1]

            cache_info = cache[name]

            # go through all of the cards, the first one is formatted to be the main card, others in the list
            # are related cards (flip sides and tokens)
            for j, card in enumerate(cache_info):
                # if this is the main card, then add to the current deck
                nickname = card[0]
                link = card[1]

                # add card to "ContainedObjects"

                if j == 0:
                    add_deck = cur_json_deck
                    repeat = num
                else:
                    add_deck = tokens_json
                    repeat = 1

                for k in range(repeat):
                    card_id = image_id * 100
                    add_deck["ContainedObjects"].append(newCard(nickname, card_id))
                    add_deck["DeckIDs"].append(card_id)
                    add_deck["CustomDeck"][str(image_id)] = newEntry(link)

                    image_id += 1

    # dump the dictionary deckfile into json
    json.dump(deck, open(filedir, "w"))




def test():
    emptyDeck = json.load(open(conf.emptyDeckLoc, "rb"))
    print(emptyDeck)
    maindeck = emptyDeck["ObjectStates"][0]
    print("maindeck", maindeck)
    sideboard = emptyDeck["ObjectStates"][1]
    print("sideboard", sideboard)
    tokens = emptyDeck["ObjectStates"][2]
    print("tokens", tokens)
    dummyCard = json.load(open(conf.dummyCardLoc, "rb"))
    print(dummyCard)
    dummyEntry = json.load(open(conf.dummyEntry, "rb"))
    print(dummyEntry)



if __name__ == "__main__":
    os.chdir("..")
    test()
    # from lib import imageDownload
    # imageDownload.test_print_cache()
