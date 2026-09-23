from typing import Dict
from app.schemas import NoteResponse

# Prosta baza danych w pamięci (wystarczająca na potrzeby projektu).
# Przy restarcie kontenera dane są czyszczone - to jest OK dla wymagań "dst".
notes_db: Dict[int, NoteResponse] = {}
next_id: int = 1


def reset_id_counter_if_empty() -> None:
    global next_id
    if not notes_db:
        next_id = 1
