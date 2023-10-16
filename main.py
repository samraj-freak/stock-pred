import cv2
import os
import numpy as np

def extract_marked_levels(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise Exception(f"Image not found or cannot be loaded: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    marked_levels = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            center_x = x + w // 2
            center_y = y + h // 2
            marked_levels.append((center_x, center_y))

    return marked_levels

if __name__ == "__main__":
    # Get the current working directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    image_files = ["AssignmentImage-1.png", "AssignmentImage-2.png"]

    for image_file in image_files:
        image_path = os.path.join(script_directory, "images", image_file)

        try:
            marked_levels = extract_marked_levels(image_path)
            print(f"Extracted marked levels from '{image_file}':", marked_levels)
        except Exception as e:
            print(f"Error processing '{image_file}': {e}")
