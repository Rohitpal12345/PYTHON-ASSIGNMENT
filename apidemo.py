from fastapi import FastAPI
# create object of 
app=FastAPI()
@app.get("/")
def demo():
    return{"Message":"Hello-Welcome to the Fast Api"}