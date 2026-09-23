# Notatnik API — CRUD

Proste REST API (FastAPI) do zarządzania notatkami: tworzenie, odczyt, edycja, usuwanie.

## Uruchomienie lokalne

```
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Dokumentacja Swagger: http://localhost:8000/docs

## Docker

```
docker build -t notatnik-app .
docker run -p 8000:8000 notatnik-app
```

## Endpointy

- GET    /notes/          — lista notatek
- POST   /notes/          — nowa notatka
- GET    /notes/{id}      — jedna notatka
- PUT    /notes/{id}      — edycja notatki
- DELETE /notes/{id}      — usunięcie notatki
- GET    /health          — health check (do testu CI/CD)
