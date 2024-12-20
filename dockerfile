# Use a imagem oficial do Python
FROM python:3.9-slim

# Instala as dependências do sistema necessárias para o OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o container
COPY requirements.txt ./requirements.txt
COPY src ./src

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pelo Streamlit
EXPOSE 8501

# Define o comando de inicialização do container
CMD ["streamlit", "run", "src/main.py"]
