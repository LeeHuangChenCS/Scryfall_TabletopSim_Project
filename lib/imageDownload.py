from lib import util
from lib import configurations as conf
import scrython as sc
import pickle
import os
import requests
import time
import unicodedata
import string


# convert a string to be filename friendly
# this code is copied from https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
# courtesy of wassname on github
def clean_filename(filename, whitelist="-_.() %s%s" % (string.ascii_letters, string.digits), replace=' '):
    # replace spaces
    for r in replace:
        filename = filename.replace(r, '_')

    # keep only valid ascii chars
    cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()

    # keep only whitelisted chars

    return ''.join(c for c in cleaned_filename if c in whitelist)


# if the card requires tokens, check the tokens from the same set and see if one of them matches the oracle text
def get_relevant_tokens(card, downloads):
    try:
        oracle_text = card.oracle_text()
    except KeyError:
        try:
            oracle_text = card.printed_text()
        except KeyError:
            oracle_text = ""
    if oracle_text == "":
        print("    Cannot find rules text for", card.name())
        return []
    else:
        print("    Finding relevant tokens for", card.name())
        relevant_tokens = []
        if "token" in oracle_text:
            time.sleep(0.1)
            tokens = sc.cards.Search(q="t:token set:t" + card.set_code())

            for i in range(tokens.total_cards()):
                token = tokens.data_tuple(i)
                uri = token["image_uris"][conf.imageSize]
                name = token["name"]
                if name in oracle_text:
                    relevant_tokens.append([name, uri])
                    downloads.append([name, uri])
                    print("    Found", name)
        return relevant_tokens


# checks if there are related cards logged for the scryfall entry
def get_scryfall_related_cards(card, downloads):
    print("    Finding relevant cards for", card.name(), "on Scryfall")
    related_cards = []

    all_parts = []
    try:
        all_parts = card.all_parts()
    except KeyError:
        print("      no related cards found for", card.name())
        pass

    # search for all related cards a find the ones that does not have the same name
    for part in all_parts:
        name = part["name"]
        if name != card.name():
            time.sleep(0.1)
            related_card = sc.cards.Named(fuzzy=name)
            uri = related_card.image_uris()[conf.imageSize]

            # add this card to download array and relevant_cards
            downloads.append([name, uri])
            related_cards.append([name, uri])

    return related_cards


# gets the cards sides and add it to the download array, if it is a double face card, it will add two entries
def get_card_sides(card, downloads):
    # check if the card is a double faced card
    faces = []
    try:
        faces = card.card_faces()
    except KeyError:
        pass

    scryfall_card_name = card.name()

    # handel double face cards
    if len(faces) > 1:
        front = faces[0]
        back = faces[1]

        frontName = front["name"]
        backName = back["name"]


        # check if there is actually a front side and a back side image for this card
        # if not, handle it like a single face card
        # this is needed for the split cards
        try:
            frontURI = front['image_uris'][conf.imageSize]
            backURI = back['image_uris'][conf.imageSize]
            downloads.append([frontName, frontURI])
            downloads.append([backName, backURI])
        except KeyError:
            uri = card.image_uris()[conf.imageSize]
            downloads.append([scryfall_card_name, uri])



    # handel single face cards
    else:
        uri = card.image_uris()[conf.imageSize]
        downloads.append([scryfall_card_name, uri])


def download_images_from_array(downloads):
    for download in downloads:
        cardNameDownload = download[0]
        file_url = download[1]
        # file_url = card.image_uris()[imageSize]
        outputFileDir = os.path.join(conf.imageFolder, clean_filename(cardNameDownload) + conf.downloadImageExtensions)

        # add the local file info into the card instance in the downloads
        download.append(outputFileDir)

        time.sleep(0.1)
        r = requests.get(file_url, stream=True)

        with open(outputFileDir, "wb") as downloadFile:
            for chunk in r.iter_content(chunk_size=1024):
                # time.sleep(0.1)

                # writing one chunk at a time to pdf file
                if chunk:
                    downloadFile.write(chunk)


# given a card download the necessary image if we haven't downloaded it
def download_image(card_name):
    # check if cache file exists and loads it into memory if it is
    util.generateDirectories(conf.cache_folder)
    cache_dir = os.path.join(conf.cache_folder, conf.cache_filename)
    if os.path.isfile(cache_dir):
        cache_dict = pickle.load(open(cache_dir, "rb"))
    else:
        cache_dict = {}

    # check if we have download this image already
    if card_name not in cache_dict.keys():
        # START UP
        util.generateDirectories(conf.imageFolder)
        print("  Downloading images for", card_name)
        time.sleep(0.1)
        card = sc.cards.Named(fuzzy=card_name)

        # list of images to be downloaded
        downloads = []

        # handel double face cards
        get_card_sides(card, downloads)
        # check if the cards have closely related cards
        get_scryfall_related_cards(card, downloads)
        # check if the card requires any tokens
        get_relevant_tokens(card, downloads)

        # download all of the images required by this card
        download_images_from_array(downloads)

        # adds the download information into the dictionary
        cache_dict[card_name] = downloads
    # dump the cache information
    pickle.dump(cache_dict, open(cache_dir, "wb"))


# given a decklist (in the format of nested lists), download all the images needed for the deck
def download_images_from_decklist(decklist):
    for entry in decklist:
        card_name = entry[1]
        download_image(card_name)


def test_print_cache():
    cache_dir = os.path.join(conf.cache_folder, conf.cache_filename)
    cache_dict = pickle.load(open(cache_dir, "rb"))
    print(cache_dict)


def test():
    #download_image("Negate")
    download_image("Adorned Pouncer")
    #download_image("Adorned Pouncer Token")
    #download_image("Deeproot Waters")
    test_print_cache()


if __name__ == "__main__":
    os.chdir("..")
    test()

