# Imagem base do Python
FROM python:3.13-slim

# Instalar dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        curl \
        supervisor \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de requisitos e instalar dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Instalar Node.js para o Tailwind
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g tailwindcss

# Copiar o código da aplicação
COPY . /app/

# Definir a variável de ambiente para não usar o buffer do Python
ENV PYTHONUNBUFFERED 1

# Copiar a configuração do supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Rodar o supervisor no container
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
