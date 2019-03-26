# This module require google-cloud python libraries
# If your environment currently don't have one, use the following command to install via pip
# pip install google-cloud

from google.cloud import vision

# Setup VISION API client
client = vision.ImageAnnotatorClient()

def tag(file):
    """
    Return a descriptive tag of a target image file using Google Vision API image labelling service
    file_path : Path to target image file e.g. ~/home/user/path/to/image.jpg
    """

    # Load the captured image into memory
    with open(file, "rb") as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # Performs label detection on the image object
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Check for Monkey
    for l  in labels:
        if "monkey" in l.description:
            return "monkey"

    # Check for Animal
    for l in labels:
        if l.description in ("fauna","wildlife"):
            return "animal"

    # When no relevant tag is found
    return "other"
