import streamlit as st
from WebCamRecordFaceDetection.main import webcam_record_face_detection_main

# Função 1
def feature_one():
    st.write("### Feature One")
    st.write("Este é o código ou funcionalidade da Feature One.")
    # Insira o código ou lógica específica aqui

# Função 2
def feature_two():
    st.write("### Feature Two")
    st.write("Este é o código ou funcionalidade da Feature Two.")
    # Insira o código ou lógica específica aqui

# Função 3
def feature_three():
    st.write("### Feature Three")
    st.write("Este é o código ou funcionalidade da Feature Three.")
    # Insira o código ou lógica específica aqui

def home():
    st.write("### Wellcome!")
    st.write("Este é o código ou funcionalidade da Home.")
    # Insira o código ou lógica específica aqui

# Menu principal
def main():
    st.sidebar.title("Menu")
    menu_options = {
        "Home": home,
        "Feature One": webcam_record_face_detection_main,
        "Feature Two": feature_two,
        "Feature Three": feature_three,
    }

    # Escolha do menu
    choice = st.sidebar.radio("Select one of the projects:", list(menu_options.keys()))

    # Executa a função correspondente à escolha do usuário
    menu_options[choice]()

if __name__ == "__main__":
    main()
