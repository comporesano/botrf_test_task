from pydantic import BaseModel, Field

from datetime import date


class AppUser(BaseModel):
    first_name: str = Field(default='Ivan', max_length=50, description='Name of user')
    last_name: str = Field(default='Ivanov', max_length=50, description='Lastname of user')
    username: str = Field(default='ivanivanov', max_length=50, description='Username of user')
    birth_date: date = Field(default=date(1999, 1, 1), description='Birthday')
    

class ResponseUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    day_until_birthday: int
    