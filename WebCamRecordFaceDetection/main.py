import os
import cv2
import streamlit as st


def webcam_record_face_detection_main():
    # Load custom CSS
    with open("WebCamRecordFaceDetection/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Set the title for the Streamlit app
    st.title("Video Capture with OpenCV")

    # Default directory for saving videos
    default_directory = "WebCamRecordFaceDetection"

    # Placeholder for the video frame
    define_directory = st.text_input(
        "Enter directory to save video:", default_directory
    )

    # Create layout with two columns
    col1, col2 = st.columns([3, 1])

    # Sessão para controle de estado
    if "recording" not in st.session_state:
        st.session_state.recording = False
    if "out" not in st.session_state:
        st.session_state.out = None
    if "recording_status" not in st.session_state:
        st.session_state.recording_status = "Not Recording"

    # Callback para iniciar gravação
    def start_recording():
        if define_directory and not st.session_state.recording:
            output_path = os.path.join(define_directory, "output.avi")
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            st.session_state.out = cv2.VideoWriter(
                output_path, fourcc, 20.0, (frame_width, frame_height)
            )
            st.session_state.recording = True
            st.session_state.recording_status = "Recording"

    # Callback para parar gravação
    def stop_recording():
        if st.session_state.recording:
            st.session_state.recording = False
            st.session_state.recording_status = "Not Recording"
            if st.session_state.out:
                st.session_state.out.release()

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

    # Define video codec e dimensões
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

    # Coluna 1: Área de vídeo
    with col1:
        st.markdown(
            "<p style='text-align:center;'>Video Stream Area</p>",
            unsafe_allow_html=True,
        )
        frame_placeholder = st.empty()

    # Coluna 2: Área de detecção e status
    with col2:
        st.markdown(
            "<p style='text-align:center;'>Face Detection</p>", unsafe_allow_html=True
        )
        face_detected = st.empty()

        # Métrica para status de gravação
        st.metric("Recording Status", st.session_state.recording_status)

        # Botões com callbacks
        st.button("Start Recording", on_click=start_recording)
        st.button("Stop Recording", on_click=stop_recording)

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
                face_detected.metric("Faces Detected", len(faces))
            else:
                face_detected.metric("Faces Detected", "No faces detected")

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


if __name__ == "__main__":
    st.set_page_config(
        page_title="WebCam Record Face Detection", page_icon=":camera:", layout="wide"
    )
    webcam_record_face_detection_main()
