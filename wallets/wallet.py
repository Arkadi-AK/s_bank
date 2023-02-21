from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from .schemas import WalletCreate, WalletList
from .services import get_wallet_list, create_wallet

router = APIRouter()


@router.get("/", response_model=List[WalletList])
def wallets_list(db: Session = Depends(get_db)):
    wallets = get_wallet_list(db)
    return wallets


@router.post("/")
def wallets_list(item: WalletCreate, db: Session = Depends(get_db)):
    wallet = create_wallet(db, item)
    return wallet
