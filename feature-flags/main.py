import configcatclient
from PIL import Image, ImageOps
from config import key
import os


configcat_client = configcatclient.create_client_with_auto_poll(key,
                                                                poll_interval_seconds=1)


while True:
    invert_dog = configcat_client.get_value('invert_dog', False)

    if invert_dog:
        im = Image.open('dog.jpg')  # imports file
        im_invert = ImageOps.invert(im)  # inverts image
        im_invert.save('inverted-dog.jpg', quality=95)  # saves new file
        print('invert_dog\'s value: ' + str(invert_dog))
        break
    else:
        try:
            os.remove('inverted-dog.jpg')  # deletes created file
            print('invert_dog\'s value: ' + str(invert_dog))
            break

        except os.error:
            pass
            print('invert_dog\'s value is still: ' + str(invert_dog))
            break

