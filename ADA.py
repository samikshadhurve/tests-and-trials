import cv2


def find_camera_indexes():
    index = 0
    available_indexes = []

    while True:
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            available_indexes.append(index)
            cap.release()
        else:
            break
        index += 1

    return available_indexes


if __name__ == "__main__":
    indexes = find_camera_indexes()
    if indexes:
        print(f"Available camera indexes: {indexes}")
    else:
        print("No cameras found.")
