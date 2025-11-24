from fastapi import HTTPException, Header
from config import SECRET_KEY, ALGORITHM
from jose import jwt



def create_token(username: str):
    payload ={"sub": username}

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token:str = Header(...)):
    try:
        new_token = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return new_token
    except:
        raise HTTPException(status_code=401, detail="Token invalide")