from pydantic import  BaseModel

class User(BaseModel):
    username:str
    password:str


class Treatment(BaseModel):
    outcome:str
    animal_id:int
    reserve_id:int
    ranger_id:int
    date:str

