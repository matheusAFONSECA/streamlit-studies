# streamlit-studies

![Python](https://img.shields.io/badge/language-Python-yellow) 
![Streamlit](https://img.shields.io/badge/framework-Streamlit-red)

A repository dedicated to storing code specifically for the ``Streamlit`` framework.

## Index

- [Projects](#projects)
  - [Detection of Faces and Video Recording](#detection-of-faces-and-video-recording)
- [How to run](#how-to-run)
- [Authors](#authors)

## Projects

This repository contains various mini-projects designed to explore and showcase the different components and capabilities of the Streamlit framework. These projects also demonstrate techniques for integrating custom components using ``CSS`` to create visually appealing layouts.

### Detection of Faces and Video Recording

This project focuses on integrating a real-time camera feed with a Streamlit interface to detect faces and record videos. It also explores the use of ``CSS`` for designing components and layouts within the project. The video is displayed in real-time, and face detection is performed using the ``Haar Cascade classifier`` from ``OpenCV``. Additionally, the application uses sessions to manage the application's state and metrics to dynamically display its status.

The documentation for this project can be found [here](WebCamRecordFaceDetection/explanation.md).

## How to Run
1. Clone the repository:

   ```bash
   git clone https://github.com/matheusAFONSECA/streamlit-studies.git
   cd streamlit-studies
   ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the projects:

    ```bash
    streamlit run main.py
    ```

4. Open the link provided in the terminal (e.g., `http://localhost:8501`) to access the interface.

## Authors

### [Matheus Fonseca](https://github.com/matheusAFONSECA)

Undergraduate student in the eighth (8th) semester of Computer Engineering at the National Institute of Telecommunications (Inatel). I participated in a Scientific Initiation at the Cybersecurity and Internet of Things Laboratory (CS&ILAB), where, in the Park Here project, I developed skills in computer vision applied to parking systems, focusing on license plate recognition and vehicle identification. Additionally, I served as a teaching assistant for Physics 1, 2, and 3, helping with practical classes, report writing, and answering theoretical questions. Currently, I am an intern at the Inatel Competence Center (ICC) in the PDI SW department.
