import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

# Title of the app
st.title("Basic Image Editor")

# Image upload widget
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    
    # Display the original image
    st.image(image, caption="Original Image", use_column_width=True)

    # Resize
    st.subheader("Resize the Image")
    width = st.slider("Width", 100, 1000, image.width)  # Set the default to the image's current width
    height = st.slider("Height", 100, 1000, image.height)  # Set the default to the image's current height
    resized_image = image.resize((width, height))
    st.image(resized_image, caption="Resized Image", use_column_width=True)

    # Rotate
    st.subheader("Rotate the Image")
    angle = st.slider("Rotation Angle", 0, 360, 0)  # Set default to 0 degrees
    rotated_image = image.rotate(angle)
    st.image(rotated_image, caption="Rotated Image", use_column_width=True)

    # Apply Filters
    st.subheader("Apply Filters")

    filter_option = st.selectbox("Select a Filter", ["None", "Grayscale", "Invert", "Blur", "Sharpen"])
    
    if filter_option == "Grayscale":
        filtered_image = image.convert("L")  # Convert to grayscale
    elif filter_option == "Invert":
        # Invert the image using numpy
        img_array = np.array(image)
        inverted_image = np.invert(img_array)
        filtered_image = Image.fromarray(inverted_image)
    elif filter_option == "Blur":
        filtered_image = image.filter(ImageFilter.BLUR)  # Apply blur filter
    elif filter_option == "Sharpen":
        enhancer = ImageEnhance.Sharpness(image)
        filtered_image = enhancer.enhance(2.0)  # Sharpen with a factor of 2.0
    else:
        filtered_image = image  # No filter

    st.image(filtered_image, caption=f"Image with {filter_option} Filter", use_column_width=True)

    # Save the edited image
    st.subheader("Download the Edited Image")
    save_button = st.button("Save Image")
    if save_button:
        # Save the filtered image or original if no changes
        filtered_image.save("edited_image.png")
        st.write("Image saved successfully!")
