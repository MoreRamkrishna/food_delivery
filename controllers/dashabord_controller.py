from fastapi import APIRouter


def create_dashboard_router(meals: list[dict]) -> APIRouter:
    router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

    @router.get("")
    def get_dashboard():
        prices = [meal["price"] for meal in meals]
        highest_priced_meal = max(meals, key=lambda meal: meal["price"], default=None)
        lowest_priced_meal = min(meals, key=lambda meal: meal["price"], default=None)

        return {
            "total_meals": len(meals),
            "average_meal_price": round(sum(prices) / len(prices), 2) if prices else 0,
            "highest_priced_meal": highest_priced_meal,
            "lowest_priced_meal": lowest_priced_meal,
        }

    return router