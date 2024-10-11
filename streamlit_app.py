import streamlit as st
import streamlit_antd_components as sac
from PIL import Image, ImageDraw
import io
import numpy
import tempfile
import numpy as np



#Tab Menu
with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Introduction', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Start', icon='box-fill', children=[
                sac.MenuItem('Upload', icon='upload'),
                sac.MenuItem('Result', icon='result'),           
                sac.MenuItem('Accuracy', icon='score'),
                sac.MenuItem('About', icon='description'),]),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group', children=[
                sac.MenuItem('Source Code', icon='download', description='Latest Version', href='https://github.com/Aditya-Gupta-ctrl/Deepfake-Detector/edit/master/streamlit_app.py'),
            ]),
        ], size='lg', variant='left-bar', color='grape', open_all=True, return_index=True)
    
if selected == 0:
        # Create a Streamlit app
        st.title("Image and Video Input")
        
        # Define a function to display the uploaded image
        def display_image(image):
            img = Image.open(image)
            img_array = np.array(img)
            st.image(img_array, caption="Uploaded Image")
        
        # Define a function to display the uploaded video
        def display_video(video):
            import tempfile
            with tempfile.NamedTemporaryFile(suffix='.mp4') as tmp:
                tmp.write(video.read())
                st.video(tmp.name, caption="Uploaded Video")
        
        # Create a file uploader for images
        st.header("Image Input")
        image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
        
        # Create a file uploader for videos
        st.header("Video Input")
        video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
        
        # Display the uploaded image
        if image_file is not None:
            display_image(image_file)
        
        # Display the uploaded video
        if video_file is not None:
            display_video(video_file)
        


        
      
