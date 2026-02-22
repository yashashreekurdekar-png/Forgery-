import cv2
import numpy as np


def error_level_analysis(original_path, modified_path):
    # Load the images
    original = cv2.imread(original_path)
    modified = cv2.imread(modified_path)

    # Ensure the images are loaded
    if original is None or modified is None:
        raise FileNotFoundError("One of the images could not be loaded. Please check the paths.")

    # Recompress the original image to JPEG format
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]  # Set the JPEG quality to 90
dummy, encoded_original = cv2.imencode('.jpg', original, encode_param)
    recompressed_original = cv2.imdecode(encoded_original, 1)

    # Compute pixel differences
    difference = cv2.absdiff(recompressed_original, modified)

    # Amplify the differences
    amplified_difference = cv2.multiply(difference, np.array([2.0]))

    # Resize the result to 128x128
    result = cv2.resize(amplified_difference, (128, 128))

    return result


# Example usage
if __name__ == '__main__':
    original_image_path = 'path/to/original.jpg'
    modified_image_path = 'path/to/modified.jpg'
    result = error_level_analysis(original_image_path, modified_image_path)
    cv2.imwrite('result.jpg', result)