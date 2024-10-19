import streamlit as st
import streamlit_antd_components as sac
from PIL import Image, ImageDraw
import io
import numpy
import tempfile
import numpy as np


# Tab Menu
with st.tabs(["Step Navigation"]):
    selected = sac.steps(
        items=[
            sac.StepsItem(title='Step 1', subtitle='Extra msg', description='Description text'),
            sac.StepsItem(title='Step 2'),
            sac.StepsItem(title='Step 3'),
            sac.StepsItem(title='Step 4', disabled=True),
        ], 
        variant='navigation', 
        color='grape', 
        return_index=True
    )
    
   
    
if selected == 3:
        
    # Create a Streamlit app
    st.title("Image Input")
    
    # Define a function to display the uploaded image
    def display_image(image):
        img = Image.open(image)
        img_array = np.array(img)
        st.image(img_array, caption="Uploaded Image")

    # Create a file uploader for images
    st.header("Image Input")
    image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    # Display the uploaded image
    if image_file is not None:
        display_image(image_file)
    

    
        


        
      
