import cv2
from datetime import datetime

# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

# Initialize webcam
cap = cv2.VideoCapture(0)
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)

try:


    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.resize(frame, (512, 512))
        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Check for 'p' keypress
        if cv2.waitKey(1) & 0xFF == ord('p'):
            # Take a picture
            cv2.imwrite('picture.jpg', frame)
            print('Picture taken!')

        # Check for 'q' keypress to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the capture
finally:
    print("releasing")
    cap.release()
    cv2.destroyAllWindows()
