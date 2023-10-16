import cv2
import numpy as np
import pytest
from main import extract_marked_levels

def test_extract_marked_levels():
    image_path = "Stock/images/AssignmentImage-1.png"
    marked_levels = extract_marked_levels(image_path)
    assert isinstance(marked_levels, list)
    assert len(marked_levels) == 7
    # Add more specific tests based on your image

if __name__ == "__main__":
    pytest.main()
