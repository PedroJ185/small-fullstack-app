from fastapi import APIRouter
import requests

router = APIRouter(prefix="/api/products", tags=["Products"])

PRODUCTS_URL = "https://dummyjson.com/products"

@router.get("/analytics")
def get_products_analytics():
    
    response = requests.get(PRODUCTS_URL).json()
    products = response.get("products", [])

    brands_reviews = {}     
    categories_stock = {}   
    category_prices = {}    

    for p in products:
        brand = p.get('brand', 'Unknown')
        cat = p['category']
        price = p['price']
        stock = p['stock']
        rating = p['rating']

        if brand not in brands_reviews:
            brands_reviews[brand] = {"total_rating": 0, "count": 0}
        brands_reviews[brand]["total_rating"] += rating 
        brands_reviews[brand]["count"] += 1             

        
        categories_stock[cat] = categories_stock.get(cat, 0) + stock

       
        if cat not in category_prices:
            category_prices[cat] = []
        category_prices[cat].append(price)

    price_ranges = {
        cat: round(max(prices) - min(prices), 2) 
        for cat, prices in category_prices.items()
    }

    return {
        "top_brands": brands_reviews,
        "categories_stock": categories_stock,
        "price_ranges": price_ranges,
        "all_products": [
            {"name": p["title"], "stock": p["stock"], "category": p["category"]} 
            for p in products
        ]
    }
