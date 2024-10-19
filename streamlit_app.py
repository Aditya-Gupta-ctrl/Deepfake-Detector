import streamlit as st
import streamlit_antd_components as sac
from PIL import Image
import numpy as np

# Set page config
st.set_page_config(
    page_title="chin Tapak dam dam",
    page_icon=":book:",
    layout="wide",
)

# Initialize session state for selected step
if 'selected_step' not in st.session_state:
    st.session_state.selected_step = 0

# Step Navigation
step_titles = [
    'Step 1', 
    'Step 2', 
    'Step 3', 
    'Step 4'
]

# Create steps navigation
selected = sac.steps(
    items=[sac.StepsItem(title=title) for title in step_titles], 
    variant='navigation', 
    color='grape', 
    return_index=True,
    current_index=st.session_state.selected_step  # Set the current index based on session state
)

# Check which step is selected
if st.session_state.selected_step == 0:  # First step
    st.title("Image Upload and Display App")
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

    # Next button to go to the next step
    if st.button("Next", key="next_button_1"):
        st.session_state.selected_step += 1  # Move to the next step

elif st.session_state.selected_step == 1:  # Step 2
    st.title("Step 2")
    st.write("This is the second step.")
    
    # Next button for Step 2
    if st.button("Next", key="next_button_2"):
        st.session_state.selected_step += 1  # Move to the next step

elif st.session_state.selected_step == 2:  # Step 3
    st.title("Step 3")
    st.write("This is the third step.")
    
    # Next button for Step 3
    if st.button("Next", key="next_button_3"):
        st.session_state.selected_step += 1  # Move to the next step

elif st.session_state.selected_step == 3:  # Step 4
    st.title("Step 4")
    st.write("This is the final step.")
