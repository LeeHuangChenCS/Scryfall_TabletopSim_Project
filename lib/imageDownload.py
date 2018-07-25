from lib import util
from lib import configurations as conf
import scrython as sc
import pickle
import os
import requests
import time


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
        print("download images for", card_name)
        time.sleep(0.1)
        # card = sc.cards.Named(exact=cardNameQuery)
        card = sc.cards.Named(fuzzy=card_name)

        scryfall_card_name = card.name()
        print(scryfall_card_name)
        faces = []

        # print(card.card_faces())

        try:
            faces = card.card_faces()
        except KeyError:
            pass

        # list of images to be downloaded
        downloads = []

        # handel double face cards
        if len(faces) > 1:
            front = faces[0]
            back = faces[1]

            frontName = front["name"]
            backName = back["name"]
            frontURI = front['image_uris'][conf.imageSize]
            backURI = back['image_uris'][conf.imageSize]

            downloads.append([frontName, frontURI])
            downloads.append([backName, backURI])
        # handel single face cards
        else:
            uri = card.image_uris()[conf.imageSize]
            downloads.append([scryfall_card_name, uri])

        for cardNameDownload, file_url in downloads:
            # file_url = card.image_uris()[imageSize]
            outputFileDir = os.path.join(conf.imageFolder, cardNameDownload + conf.downloadImageExtensions)

            time.sleep(0.1)
            r = requests.get(file_url, stream=True)

            with open(outputFileDir, "wb") as downloadFile:
                for chunk in r.iter_content(chunk_size=1024):
                    # time.sleep(0.1)

                    # writing one chunk at a time to pdf file
                    if chunk:
                        downloadFile.write(chunk)

        # adds the download information into the dictionary
        cache_dict[card_name] = downloads
    # dump the cache information
    pickle.dump(cache_dict, open(cache_dir, "wb"))


def test():
    download_image("Negate")
    cache_dir = os.path.join(conf.cache_folder, conf.cache_filename)
    cache_dict = pickle.load(open(cache_dir, "rb"))
    print(cache_dict)


if __name__ == "__main__":
    test()

