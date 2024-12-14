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
stop_recording = st.button("Stop Recording")

# Initialize the video capture object
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    st.write("Failed to access the camera.")
    cap = None

out = None
recording = False

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Define video codec and output file if recording starts
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) if cap else 0
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) if cap else 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Ensure the directory is set correctly
if define_directory and not os.path.exists(define_directory):
    try:
        os.makedirs(define_directory)
    except FileNotFoundError:
        st.error("Invalid directory. Please provide a valid path.")

while cap and cap.isOpened():
    ret, frame = cap.read()

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
    if recording and out:
        out.write(frame)

    # Display the frame using Streamlit's st.image
    frame_placeholder.image(rgb_frame, channels="RGB")

    # Start recording if the button is clicked
    if start_recording and not recording:
        if define_directory:
            output_path = os.path.join(define_directory, "output.avi")
            out = cv2.VideoWriter(output_path, fourcc, 20.0, (frame_width, frame_height))
            recording = True
            st.write("Recording started...")
        else:
            st.error("Please specify a valid directory to save the video.")

    # Stop recording if the button is clicked
    if stop_recording and recording:
        recording = False
        if out:
            out.release()
        st.write("Recording stopped. Video saved at: {output_path}")

if cap:
    cap.release()
cv2.destroyAllWindows()
