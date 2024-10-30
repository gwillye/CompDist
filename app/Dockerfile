# Usa uma imagem base leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o código para o contêiner
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define a variável de ambiente para desabilitar o buffering
ENV PYTHONUNBUFFERED=1

# Porta que o Flask vai expor
EXPOSE 8080

# Comando para iniciar o aplicativo
CMD ["python", "run.py"]
