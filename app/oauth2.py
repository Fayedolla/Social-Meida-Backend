from csv import excel_tab
from jose import jwt, JWTError, ExpiredSignatureError
from sqlalchemy.orm import session
from config import settings
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from . import schemes, Database, Models
from datetime import timedelta, datetime, timezone

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get('user_id')
        if id is None:
            raise credential_exception
        token_data = schemes.TokenData(id=id)
        return token_data
    
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token Expired. Please Log in again",
        headers={"WWW-Authenticated": "Bearer"})

    except JWTError:
        raise credential_exception


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(Database.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credential",
    headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credential_exception)

    user_id = db.query(Models.User).filter(Models.User.id==token.id).first()
    return user_id