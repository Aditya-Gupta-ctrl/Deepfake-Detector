import streamlit as st
import streamlit_antd_components as sac
from PIL import Image, ImageDraw
import io
import cv#2
import numpy
import tempfile
import numpy as np



#Tab Menu
with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Introduction', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Basics', icon='box-fill', children=[
                sac.MenuItem('First Program'),
                sac.MenuItem('Syntax & Basic'),           
                sac.MenuItem('Variable'),
                sac.MenuItem('Input and Output'),
                sac.MenuItem('Data Types'),
                sac.MenuItem('Operators'),
                sac.MenuItem('Conditional Statement'),
                sac.MenuItem('Loops'),
                sac.MenuItem('Function'),
            ]),
            sac.MenuItem('Cheatsheet', icon='table'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group', children=[
                sac.MenuItem('Download Python', icon='download', description='Latest Version', href='https://www.python.org/downloads/'),
                sac.MenuItem('Download VS Code', icon='terminal', href='https://code.visualstudio.com/download'),
            ]),
        ], size='lg', variant='left-bar', color='grape', open_all=True, return_index=True)
    
if selected == 2:
        # Create a Streamlit app
        st.title("Image and Video Input")
        
        # Define a function to display the uploaded image
        def display_image(image):
            img = Image.open(image)
            img_array = np.array(img)
            st.image(img_array, caption="Uploaded Image")
        
        # Define a function to display the uploaded video
        def display_video(video):
            video_bytes = video.read()
            st.video(video_bytes, caption="Uploaded Video")
        
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
        


        
        # Create a file uploader for videos
        st.header("Video Input")
        video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
        
        # Create a temporary file to store the uploaded video
        if video_file is not None:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(video_file.read())
        
            # Open the video file using OpenCV
            vf = cv2.VideoCapture(tfile.name)
        
            # Read and display the video frames
            stframe = st.empty()
            while vf.isOpened():
                ret, frame = vf.read()
                if not ret:
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                stframe.image(gray)
