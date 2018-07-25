import scrython as sc
import time
import requests
from lib import util
import os

if __name__ == "__main__":

    # PARAMETERS

    # image size to download: use either "small", "normal", "large"
    imageSize = "large"
    # the folder that all images will be downloaded to
    imageFolder = "Resources/CardImages"
    # the extention to use for downloading the images
    downloadImageExtensions = ".jpg"

    # START UP
    util.generateDirectories(imageFolder)

    # TEST CODE
    decklistFile = "DeckLists/Standard_Auras_(Fork).txt"

    # cardNameQuery = "Creatures (20)"
    # cardNameQuery = "Aberrant Researcher"
    # cardNameQuery = "Open into"
    cardNameQuery = "Negate"
    time.sleep(0.1)
    # card = sc.cards.Named(exact=cardNameQuery)
    card = sc.cards.Named(fuzzy=cardNameQuery)

    cardName = card.name()
    print(cardName)
    faces = []

    # print(card.card_faces())

    try:
        faces = card.card_faces()
    except KeyError:
        pass

    # list of images to be downloaded
    downloads = []

    # handel double face cards
    if len(faces)>1:
        front = faces[0]
        back = faces[1]

        frontName = front["name"]
        backName = back["name"]
        frontURI = front['image_uris'][imageSize]
        backURI = back['image_uris'][imageSize]

        downloads.append([frontName, frontURI])
        downloads.append([backName, backURI])
    # handel single face cards
    else:
        uri = card.image_uris()[imageSize]
        downloads.append([cardName, uri])

    for cardNameDownload, file_url in downloads:

        # file_url = card.image_uris()[imageSize]
        outputFileDir = os.path.join(imageFolder, cardNameDownload+downloadImageExtensions)
        print(outputFileDir)

        time.sleep(0.1)
        r = requests.get(file_url, stream=True)

        with open(outputFileDir, "wb") as downloadFile:
            for chunk in r.iter_content(chunk_size=1024):
                # time.sleep(0.1)

                # writing one chunk at a time to pdf file
                if chunk:
                    downloadFile.write(chunk)
