import cv2

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

    # Check for 'q' keypress to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
