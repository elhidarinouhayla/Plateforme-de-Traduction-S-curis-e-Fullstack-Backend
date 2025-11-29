FROM python:3.11

WORKDIR /app

COPY requirement.txt . 

RUN pip inatall -r requirement

COPY . .

CMD ["uvicorm", "main:app", "--host", "0.0.0.0", "--port", "8000"]



