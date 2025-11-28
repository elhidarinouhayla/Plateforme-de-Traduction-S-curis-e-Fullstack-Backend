from fastapi import HTTPException, Header
from config import SECRET_KEY, ALGORITHM
from jose import jwt

 

def create_token(username: str):
    payload ={"sub": username}

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token:str = Header(...)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Token invalide")
    











    