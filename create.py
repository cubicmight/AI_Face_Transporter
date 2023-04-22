import json
from base64 import b64decode
from pathlib import Path
import openai
import cvzone
import cv2


def dall_e_city():
    PROMPT = "Generate the city of Miami from a street view with a person smiling"
    DATA_DIR = Path.cwd() / "responses"
    DATA_DIR.mkdir(exist_ok=True)
    openai.api_key = open("API_KEY.txt", "r").read()
    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="512x512",
        response_format="b64_json",
    )
    file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(response, file)
    DATA_DIR = Path.cwd() / "responses"
    JSON_FILE = DATA_DIR / file_name
    IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    with open(JSON_FILE, mode="r", encoding="utf-8") as file:
        response = json.load(file)
    for index, image_dict in enumerate(response["data"]):
        image_data = b64decode(image_dict["b64_json"])
        image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
        with open(image_file, mode="wb") as png:
            png.write(image_data)


def cv_picture():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Check for 'p' keypress
        if cv2.waitKey(1) & 0xFF == ord('p'):
            # Take a picture
            cv2.imwrite('picture.jpg', frame)
            print('Picture taken!')

            # Destroy preview window
            cv2.destroyWindow('frame')

            # Exit loop
            break

        # Check for 'q' keypress to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the capture
    cap.release()
    cv2.destroyAllWindows()





