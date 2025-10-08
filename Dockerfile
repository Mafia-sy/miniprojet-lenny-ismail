# Utiliser une image officielle Python légère
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . .

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
RUN pip install --no-cache-dir \
    pycryptodome \
    fastapi \
    uvicorn \
    python-multipart \
    requests

# Exposer le port de l'API FastAPI
EXPOSE 8000

# Commande par défaut pour lancer l’API
CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "8000"]
