import asyncio
import requests
from core.models import Product, db_helper
from core.schemas.product import ProductCreate

FAKE_STORE_API_URL = "https://fakestoreapi.com/products"


def fetch_products():
    response = requests.get(FAKE_STORE_API_URL)
    response.raise_for_status()
    return response.json()


async def push_products_to_db():
    async with db_helper.session_factory() as session:
        products = fetch_products()
        for product_data in products:
            product = ProductCreate(
                title=product_data["title"],
                price=product_data["price"],
                description=product_data["description"],
                image=product_data["image"],
                category=product_data["category"],
                rating=product_data["rating"]["rate"],
                rating_count=product_data["rating"]["count"],
            )
            db_product = Product(**product.dict())
            session.add(db_product)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(push_products_to_db())
