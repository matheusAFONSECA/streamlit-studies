# Detection of Faces and Video Recording

This project leverages **OpenCV** to capture images from the machine's webcam and display them in a **Streamlit** interface. It also performs **face detection** using the **Haar Cascade Classifier**. Additionally, users can **record videos** for any desired duration. While recording, the interface displays:

- Real-time feedback on whether the video is being recorded.
- The **number of detected faces** in the video stream.

This project employs **CSS** for a custom layout design in the Streamlit interface.

---

## Features

1. **Webcam Image Capture**  
   Captures real-time video input from the webcam and streams it to the Streamlit interface.

2. **Face Detection**  
   Utilizes the Haar Cascade Classifier to detect faces in the video feed.

3. **Video Recording**  
   Enables video recording for any duration, saving the output locally.

4. **Real-time Metrics**  
   - Display when video recording is active.
   - Show the total number of faces detected using **`st.metrics`**.

5. **Custom Layout**  
   Styled using CSS for a clean and interactive user interface.

---

## Requirements
To run this project, install the following dependencies:

- Python 3.8+
- OpenCV
- Streamlit

You can install the dependencies using:

```bash
pip install opencv-python streamlit
```

---

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

3. Open the link provided in the terminal (e.g., `http://localhost:8501`) to access the interface.

---

## Project Structure
```
project-directory/
├── app.py                 # Main Streamlit application
├── haarcascade.xml        # Haar Cascade XML file for face detection
├── recordings/            # Directory to save recorded videos
├── utils/                 # Utility scripts (if applicable)
└── README.md              # Project documentation
```

---

## Usage
1. Start the webcam feed.
2. Activate face detection and monitor faces detected in real-time.
3. Start and stop video recording as needed.
4. View live metrics on recording status and face count.

---

## Screenshots
**(Add screenshots of your Streamlit interface showcasing video recording and face detection here)**

---

## Acknowledgments
- **OpenCV** for computer vision capabilities.
- **Streamlit** for providing an easy-to-use web interface framework.
- **Haar Cascade Classifier** for face detection.