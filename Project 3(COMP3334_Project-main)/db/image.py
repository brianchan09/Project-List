import os
import gridfs
from PIL import Image, ImageTk

from db.params import database, backup_database

# get image from database
def get_image_from_db(filename="", x=60, y=60):
    fs = gridfs.GridFS(database)
    grid_out = fs.get_last_version(filename=filename)
    size = (x, y) # set the image size
    loc = Image.open(grid_out).resize(size)
    img = ImageTk.PhotoImage(loc) # convert image into tkimage format
    return img

# upload image
def upload_image_to_db(image_name):
    fs = gridfs.GridFS(database)
    with open(image_name, 'rb') as f:
        contents = f.read() # read the image data
    filename = os.path.basename(image_name) # get the file name from file location
    fs.put(contents, filename=filename) # upload to main database
    fs = gridfs.GridFS(backup_database)
    fs.put(contents, filename=filename) # upload to backup database
    f.close()
    return filename
