from fastapi import APIRouter, Response, Depends

from app.users.dependencies import get_current_user
from app.users.schemas import SUserAuth
from app.users.dao import UsersDAO
from app.users.auth import get_password_hash, create_access_token, authenticate_user
from app.users.models import Users
from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)


@router.post("/register")
async def register_user(user_date: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_date.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_date.password)
    await UsersDAO.add(email=user_date.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_date: SUserAuth):
    user = await authenticate_user(user_date.email, user_date.password)
    if not user:
        return IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")


@router.get("")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user
