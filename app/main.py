from fastapi import FastAPI, HTTPException
from app.schemas import NoteCreate, NoteUpdate, NoteResponse
from app import models

app = FastAPI(title="Notatnik API", version="1.0.0")


@app.get("/health")
def health_check():
    """Prosty endpoint do weryfikacji, że serwis działa (używany też do testu CI/CD)."""
    return {"status": "ok"}


@app.get("/notes/", response_model=list[NoteResponse])
def read_notes():
    return list(models.notes_db.values())


@app.post("/notes/", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate):
    new_id = models.next_id
    new_note = NoteResponse(id=new_id, title=note.title, content=note.content)
    models.notes_db[new_id] = new_note
    models.next_id += 1
    return new_note


@app.get("/notes/{note_id}", response_model=NoteResponse)
def read_note(note_id: int):
    note = models.notes_db.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Notatka nie znaleziona")
    return note


@app.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note_update: NoteUpdate):
    note = models.notes_db.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Notatka nie znaleziona")

    updated = note.model_copy(update={
        k: v for k, v in note_update.model_dump().items() if v is not None
    })
    models.notes_db[note_id] = updated
    return updated


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    if note_id not in models.notes_db:
        raise HTTPException(status_code=404, detail="Notatka nie znaleziona")
    del models.notes_db[note_id]
    return None
