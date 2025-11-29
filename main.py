from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import session
from database import SessionLocal
from models.model import CreateUser, ResponseUser, User, TraductionShema
from database import Base, engine, get_db 
from fastapi.middleware.cors import CORSMiddleware
from auth import create_token, verify_token
from translate import translate


app = FastAPI()
Base.metadata.create_all(bind=engine)



app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


# crier username et ajoute le dans DB
@app.post("/register", response_model=ResponseUser)
def create_user(user: CreateUser, db:session = Depends(get_db)):
    exist = db.query(User).filter(User.username == user.username).first()
    if exist:
        raise HTTPException(status_code=400, detail="username deja utilise")
    
    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# verifier l'identifiant et retourner token
@app.post("/login")
def login(user: CreateUser, db: session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.username == user.username,
        User.password == user.password
    ).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="username ou password incorect")

    token = create_token(db_user.username)

    return {"token": token}


@app.post("/translate")
def translate_text(data: TraductionShema, 
                   user=Depends(verify_token)
                   ):
        return translate(data.text, data.language)

    # try:
    #     result = translate(data.text, data.language)
    #     if result is None:
    #         raise Exception("Erreue : réponse HuggingFace invalide")
    #     return {"translated_text": result}
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))

    

    







   
       

