import cv2
import numpy as np
from PIL import Image, ImageFilter
import os

def cartoonize_image(input_image_path, output_image_path):
    # Read the image using OpenCV
    img = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect edges in the image and apply thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply a bilateral filter to smooth the image
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Combine the edges image with the color image to get the cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Convert the cartoon image from BGR to RGB
    cartoon_rgb = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)

    # Convert the cartoon image to a PIL Image
    cartoon_pil = Image.fromarray(cartoon_rgb)

    # Save the cartoon image
    cartoon_pil.save(output_image_path)

# Path to the input image
input_image_path = r"C:\Users\mouad\Desktop\AI_python_TP2\daisy-424893_640.jpg"

# Path to save the output cartoon image
output_image_path = r"C:\Users\mouad\Desktop\AI_python_TP2\resulta.jpg"

# Create the cartoon image
cartoonize_image(input_image_path, output_image_path)

print("Cartoon image saved at:", output_image_path)
