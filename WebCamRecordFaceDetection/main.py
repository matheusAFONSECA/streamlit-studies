import cv2
import streamlit as st
import numpy as np
import os

# Set the title for the Streamlit app
st.title("Video Capture with OpenCV")

# Default directory for saving videos
default_directory = "WebCamRecordFaceDetection"

# Placeholder for the video frame
define_directory = st.text_input("Enter directory to save video:", default_directory)

frame_placeholder = st.empty()

# Session state for recording control
if 'recording' not in st.session_state:
    st.session_state.recording = False
if 'out' not in st.session_state:
    st.session_state.out = None

# Initialize the video capture object
if 'cap' not in st.session_state:
    st.session_state.cap = cv2.VideoCapture(0)
    if not st.session_state.cap.isOpened():
        st.write("Failed to access the camera.")
        st.session_state.cap = None

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Define video codec and output file if recording starts
frame_width = int(st.session_state.cap.get(cv2.CAP_PROP_FRAME_WIDTH)) if st.session_state.cap else 0
frame_height = int(st.session_state.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) if st.session_state.cap else 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Ensure the directory is set correctly
if define_directory and not os.path.exists(define_directory):
    try:
        os.makedirs(define_directory)
    except FileNotFoundError:
        st.error("Invalid directory. Please provide a valid path.")

# Button controls
if st.button("Start Recording"):
    if define_directory and not st.session_state.recording:
        output_path = os.path.join(define_directory, "output.avi")
        st.session_state.out = cv2.VideoWriter(output_path, fourcc, 20.0, (frame_width, frame_height))
        st.session_state.recording = True
        st.write("Recording started...")
    elif not define_directory:
        st.error("Please specify a valid directory to save the video.")

if st.button("Stop Recording"):
    if st.session_state.recording:
        st.session_state.recording = False
        if st.session_state.out:
            st.session_state.out.release()
        st.write("Recording stopped.")

while st.session_state.cap and st.session_state.cap.isOpened():
    ret, frame = st.session_state.cap.read()

    if not ret:
        st.write("The video capture has ended.")
        break

    # Convert the frame from BGR to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert the frame from BGR to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the output video file if recording
    if st.session_state.recording and st.session_state.out:
        st.session_state.out.write(frame)

    # Display the frame using Streamlit's st.image
    frame_placeholder.image(rgb_frame, channels="RGB")

if st.session_state.cap:
    st.session_state.cap.release()
cv2.destroyAllWindows()
