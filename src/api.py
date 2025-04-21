import string
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from src.CRUD import AsyncCRUD
import random
import httpx

router = APIRouter()


@router.get("/create-tables")
async def create_tables():
    await AsyncCRUD.create_tables()
    return {"ok": True}


@router.post("/short-url/create", status_code=201)
async def create_short_url(long_url: str):
    short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    await AsyncCRUD.insert_urls(long_url=long_url, short_url=short_url)
    return {"short_url": short_url}, 201


@router.get("/short-url/{short_url}", status_code=307)
async def get_long_url(short_url: str):
    long_url = await AsyncCRUD.select_urls(short_url=short_url)
    return {"long_url": long_url}


@router.get("/bitcoin/price")
async def get_bitcoin_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return {"bitcoin_price": data["price"]}
