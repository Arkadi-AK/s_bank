from fastapi import APIRouter

from wallets import wallet

routes = APIRouter()

routes.include_router(wallet.router, prefix="/wallet")
