# Usando uma versão mais recente do Python (3.12)
FROM python:3.12-slim as python-base

# Configuração do ambiente Python e Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.5 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Adiciona o Poetry e o ambiente virtual ao PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instalar dependências do sistema e o Poetry
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  # Limpar caches de pacotes para reduzir o tamanho da imagem

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# Configuração do diretório de trabalho e copiar os arquivos necessários
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Instalar as dependências do Poetry (sem as dependências de desenvolvimento)
RUN poetry install --only main  # Use --only main para instalar apenas as dependências de produção

# Configuração do diretório do projeto
WORKDIR /app
COPY . /app/

# Expor a porta do servidor
EXPOSE 8000

RUN pip install python-dotenv

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]