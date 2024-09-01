from fastapi import APIRouter, HTTPException

from database.models import User
from database.schemas import AppUser, ResponseUser

from tortoise.exceptions import IntegrityError, DoesNotExist

from pydantic import Json

from datetime import date

import json


router = APIRouter(prefix='/user', tags=['User creation and information extraction'])


def calculate_days_til_bd(birth_date: date) -> int:
    now_date = date.today()
    next_birthday = date(now_date.year, birth_date.month, birth_date.day)
    if now_date > next_birthday:
        next_birthday = date(now_date.year + 1, birth_date.month, birth_date.day)
    
    return (next_birthday - now_date).days


@router.post('/create')
async def create_user(user: AppUser) -> Json:
    try:
        await User.create(**user.__dict__)
        return json.dumps({"data": f"User {user} created successfully!"})
    except IntegrityError:
        pass
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/get/')
async def get_user(user_id: int | None = None, username: str | None = None) -> ResponseUser:
    try:
        if user_id:
            user = await User.get(id=user_id)
        elif username:
            user = await User.get(username=username)
        else:
            raise AttributeError('Attributes does\'nt set.')
        til_days = calculate_days_til_bd(user.birth_date)
        return ResponseUser(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            day_until_birthday=til_days
        )
    except AttributeError as ae:
        raise HTTPException(status_code=400, detail=str(ae))
    except DoesNotExist:
        raise HTTPException(status_code=400, detail='User does\'nt exist.')
    
