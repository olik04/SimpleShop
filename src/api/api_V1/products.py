from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_

from core import settings
from core.schemas.product import ProductCreate, ProductRead, ProductUpdate
from core.models import Product, db_helper

router = APIRouter(
    prefix=settings.api.v1.products,
    tags=["Products"],
)


@router.post("/", response_model=ProductRead)
async def create_product(
    product: ProductCreate, db: AsyncSession = Depends(db_helper.session_getter)
):
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


@router.get("/{product_id}", response_model=ProductRead)
async def read_product(
    product_id: int, db: AsyncSession = Depends(db_helper.session_getter)
):
    result = await db.execute(select(Product).filter(Product.id == product_id))
    db_product = result.scalars().first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/{product_id}", response_model=ProductRead)
async def update_product(
    product_id: int,
    product: ProductUpdate,
    db: AsyncSession = Depends(db_helper.session_getter),
):
    result = await db.execute(select(Product).filter(Product.id == product_id))
    db_product = result.scalars().first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    await db.commit()
    await db.refresh(db_product)
    return db_product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int, db: AsyncSession = Depends(db_helper.session_getter)
):
    result = await db.execute(select(Product).filter(Product.id == product_id))
    db_product = result.scalars().first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    await db.delete(db_product)
    await db.commit()
    return None


@router.get("/search/", response_model=List[ProductRead])
async def search_products(
    keywords: str = Query(..., min_length=1),
    db: AsyncSession = Depends(db_helper.session_getter),
):
    search = f"%{keywords}%"
    stmt = select(Product).filter(
        or_(Product.title.ilike(search), Product.description.ilike(search))
    )
    result = await db.execute(stmt)
    db_products = result.scalars().all()
    return db_products
