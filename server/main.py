from fastapi import FastAPI, HTTPException
from server.animal_service import find_last_reserve

app = FastAPI()


@app.get("/animals/last-reserve")
def get_animal(animal_id: int | None = None, collar_code: str | None = None):
    if animal_id:
        result = find_last_reserve("id", animal_id)
    elif collar_code:
        result = find_last_reserve("collar_code", collar_code)
    else:
        raise HTTPException(status_code=400, detail="Either id or collar_code must be provided")

    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Animal not found")

