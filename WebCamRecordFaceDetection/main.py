import cv2
import streamlit as st
import os

# Configure the Streamlit page
st.set_page_config(
    page_title="Face Detection and Video Recording", page_icon="👨‍🔧", layout="wide"
)

# Load custom CSS
with open("WebCamRecordFaceDetection/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Set the title for the Streamlit app
st.title("Video Capture with OpenCV")

# Default directory for saving videos
default_directory = "WebCamRecordFaceDetection"

# Placeholder for the video frame
define_directory = st.text_input("Enter directory to save video:", default_directory)

# Create layout with two columns
col1, col2 = st.columns([3, 1])

# Sessão para controle de estado
if "recording" not in st.session_state:
    st.session_state.recording = False
if "out" not in st.session_state:
    st.session_state.out = None

# Inicializa a captura de vídeo
if "cap" not in st.session_state:
    st.session_state.cap = cv2.VideoCapture(0)
    if not st.session_state.cap.isOpened():
        st.write("Failed to access the camera.")
        st.session_state.cap = None

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Define video codec and output file if recording starts
frame_width = (
    int(st.session_state.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    if st.session_state.cap
    else 0
)
frame_height = (
    int(st.session_state.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if st.session_state.cap
    else 0
)
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Coluna 1: Área de vídeo
with col1:
    st.markdown(
        "<p style='text-align:center;'>Video Stream Area</p>", unsafe_allow_html=True
    )
    frame_placeholder = st.empty()

# Coluna 2: Área de detecção
with col2:
    st.markdown(
        "<p style='text-align:center;'>Face Detection</p>", unsafe_allow_html=True
    )
    face_detected = st.empty()

    if st.button("Start Recording"):
        if define_directory and not st.session_state.recording:
            output_path = os.path.join(define_directory, "output.avi")
            st.session_state.out = cv2.VideoWriter(
                output_path, fourcc, 20.0, (frame_width, frame_height)
            )
            st.session_state.recording = True
            st.success("Recording started...")
        elif not define_directory:
            st.error("Please specify a valid directory to save the video.")

    if st.button("Stop Recording"):
        if st.session_state.recording:
            st.session_state.recording = False
            if st.session_state.out:
                st.session_state.out.release()
            st.error("Recording stopped.")

# Loop de captura
while st.session_state.cap and st.session_state.cap.isOpened():
    ret, frame = st.session_state.cap.read()

    if not ret:
        st.write("The video capture has ended.")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    with col2:
        if len(faces) > 0:
            face_detected.metric("Faces Detecteds", len(faces))
        else:
            face_detected.metric("Faces Detecteds", "No faces detected")

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if st.session_state.recording and st.session_state.out:
        st.session_state.out.write(frame)

    with col1:
        frame_placeholder.image(rgb_frame, channels="RGB")

if st.session_state.cap:
    st.session_state.cap.release()
cv2.destroyAllWindows()
