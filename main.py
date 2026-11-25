# main.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from controllers.dashabord_controller import create_dashboard_router

class MealCreate(BaseModel):
    name: str
    price: float = Field(gt=0)

app = FastAPI(title="FastAPI Swagger Food`s", version="1.0.0")

meals = [
    {"id": 1, "name": "Veggie rice bowl", "price": 8.50},
    {"id": 2, "name": "rice only", "price": 9.00},
]

app.include_router(create_dashboard_router(meals))

@app.get("/meals")
def list_meals():
    return meals

@app.get("/meals/{meal_id}")
def get_meal(meal_id: int):
    for meal in meals:
        if meal["id"] == meal_id:
            return meal
    return {"error": "Meal not found"}
@app.post("/meals")
def add_meal(meal: MealCreate):
    meal_dict = meal.dict()
    meal_dict["id"] = len(meals) + 1
    meals.append(meal_dict)
    return meal_dict    

@app.post("/meals", status_code=201)
def add_meal(meal: MealCreate):
    new_meal = {
        "id": max((item["id"] for item in meals), default=0) + 1,
        "name": meal.name,
        "price": meal.price,
    }
    meals.append(new_meal)
    return new_meal