from PIL import Image
import os

# given a maindeck and sideboard, this function takes all of the images it needs and combine it to a jpeg
def generate_combined_picture(maindeck, sideboard):

def test():
    card1 = 'Resources/CardImages\\Treasure.jpg'
    card2 = 'Resources/CardImages\\Captain_Lannery_Storm.jpg'
    images = [Image.open(card1), Image.open(card2)]
    #print(images)

    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save('test.jpg')


if __name__ == "__main__":
    os.chdir("..")
    test()
