import streamlit as st
import streamlit_antd_components as sac
from PIL import Image
import numpy as np

# Set page config
st.set_page_config(
    page_title="kuch Rang Pyar Ke",
    page_icon=":book:",
    layout="wide",
)


# Step Navigation
selected = sac.steps(
    items=[
        sac.StepsItem(title='Step 1', subtitle='Extra msg', description='Description text'),
        sac.StepsItem(title='Step 2'),
        sac.StepsItem(title='Step 3'),
        sac.StepsItem(title='Step 4', disabled=True),
    ], 
    variant='navigation', 
    color='grape', 
    size='sm',
    return_index=True
)

# Check which step is selected
if selected == 0:  # Adjusted index to match the third step (0-based index)
    # Create a Streamlit app
    st.title("Image Upload aned Display App")

    st.header("Image Input")
    
    # Define a function to display the uploaded image
    def display_image(image):
        img = Image.open(image)
        img_array = np.array(img)
        st.image(img_array, caption="Uploaded Image", use_column_width=True)

    # Create a file uploader for images
    image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    
    # Display the uploaded image
    if image_file is not None:
        display_image(image_file)
