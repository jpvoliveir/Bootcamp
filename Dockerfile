# Imagem base enxuta do Python, suficiente para uma aplicacao CLI
# que usa apenas a biblioteca padrao.
FROM python:3.11-slim

# Pasta central de operacoes dentro do container.
WORKDIR /app

# Garante que print() e input() apareçam imediatamente no terminal,
# sem ficarem retidos no buffer de saida do Python.
ENV PYTHONUNBUFFERED=1

# Copia o codigo-fonte da aplicacao para dentro da imagem.
COPY src/ /app/src/

# Comando disparado quando o container sobe.
CMD ["python", "src/main.py"]
