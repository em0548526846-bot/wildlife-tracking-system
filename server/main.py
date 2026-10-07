from fastapi import FastAPI, HTTPException,Header,status
from server.animal_service import find_last_reserve
from server.auth import register_user, verify_user
from server.treatment_service import create_treatment, get_ranger_treatments_by_reserve
from server.response_models import User, Treatment

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


@app.post("/users/register",status_code=status.HTTP_201_CREATED)
def register_user_endpoint(user_data:User):
    try:
        register_user(user_data.username, user_data.password)
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




@app.post("/treatments",status_code=status.HTTP_201_CREATED)
def register_treatment(treatment_data:Treatment,x_username: str = Header(None, alias="X-Username"),
x_password: str = Header(None, alias="X-Password")):
    if not x_username or not x_password or not verify_user(x_username, x_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    try:
        create_treatment(treatment_data.outcome, treatment_data.animal_id, treatment_data.reserve_id, treatment_data.ranger_id, treatment_data.date)
        return {"message": "Treatment registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/rangers/treatments-by-reserve")
def get_treatments_by_reserve(
    ranger_id: int | None = None,
    ranger_name: str | None = None,
    x_username: str | None = Header(None, alias="X-Username"),
    x_password: str | None = Header(None, alias="X-Password")
):
    if not x_username or not x_password or not verify_user(x_username, x_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not ranger_id and not ranger_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Either ranger_id or ranger_name must be provided")

    try:
        if ranger_id:
            return get_ranger_treatments_by_reserve("ranger_id", ranger_id)
        return get_ranger_treatments_by_reserve("ranger_name", ranger_name)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


