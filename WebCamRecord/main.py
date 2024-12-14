import cv2
import streamlit as st
import numpy as np
import os

# Set the title for the Streamlit app
st.title("Video Capture with OpenCV")

# Placeholder for the video frame
define_directory = st.text_input("Enter directory to save video:")

frame_placeholder = st.empty()

# Buttons to control the app
start_recording = st.button("Start Recording")
stop_button_pressed = st.button("Stop")

# Initialize the video capture object
cap = None
out = None
recording = False

if start_recording:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.write("Failed to access the camera.")
    else:
        st.write("Recording started...")

    # Define video codec and output file
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Ensure the directory exists
    if not os.path.exists(define_directory):
        os.makedirs(define_directory)

    output_path = os.path.join(define_directory, "output.avi")
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (frame_width, frame_height))
    recording = True

while recording and not stop_button_pressed:
    ret, frame = cap.read()

    if not ret:
        st.write("The video capture has ended.")
        break

    # Convert the frame from BGR to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the output video file
    if out:
        out.write(frame)

    # Display the frame using Streamlit's st.image
    frame_placeholder.image(rgb_frame, channels="RGB")

if stop_button_pressed:
    if recording:
        recording = False
        if cap:
            cap.release()
        if out:
            out.release()
        st.write(f"Recording stopped. Video saved at: {output_path}")

cv2.destroyAllWindows()
