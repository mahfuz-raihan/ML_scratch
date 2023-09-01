from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class AvailableCuisines(str, Enum):
    indian = 'indian'
    ameracan = 'american'
    italian = 'italian'
    bengali = 'bengali'

food_items = {
    'indian': ['Samosa', 'Dosa'],
    'american': ['Hot Dog', 'apple pie'],
    'italian' : ['Ravioli','pizza'],
    'bengali' : ['Kacchi biriyani','Kalavuna']
}


@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)



coupon_code = {
    1:'10%',
    2:'30%',
    3:'50%'
}

@app.get('/get_coupon/{code}')
async def get_items(code: int):
    return {'discount amount': coupon_code.get(code)}