from fastapi import FastAPI, HTTPException
from app.models import Note

app = FastAPI()

# In-memory storage (like a fake database)
notes_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple Notes API!"}

@app.get("/notes")
def get_notes():
    return notes_db

@app.post("/notes")
def create_note(note: Note):
    # Check if ID already exists
    for n in notes_db:
        if n.id == note.id:
            raise HTTPException(status_code=400, detail="Note with this ID already exists.")
    notes_db.append(note)
    return {"message": "Note created successfully!"}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for n in notes_db:
        if n.id == note_id:
            notes_db.remove(n)
            return {"message": "Note deleted successfully!"}
    raise HTTPException(status_code=404, detail="Note not found.")
