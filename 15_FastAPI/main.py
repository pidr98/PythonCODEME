from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()
app.counter = 0

class HelloResp(BaseModel):
    msg: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)


# Utwórz endpoint, który za pomocą metody post pozwala “dodać” produkt.
# Produkt ma pola: name (string), description (optional), price (float), code (string), tax (optional).
# Przy “dodaniu” endpoint zwraca dodany produkt i opcjonalnie cenę brutto produktu.



@app.get("/hello/{name}", response_model=HelloResp)
def hello_name_view(name: str):
    return HelloResp(msg=f"Hello {name}")