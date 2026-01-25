from pydantic import BaseModel, EmailStr

class RegisterUserDTO(BaseModel):
    username: str
    email: EmailStr
    password: str
