from sqlalchemy.orm import Session

from .models import Wallet
from .schemas import WalletCreate


def get_wallet_list(db: Session):
    query = db.query(Wallet).all()
    return query


def create_wallet(db: Session, item: WalletCreate):
    wallet = Wallet(**item.dict())
    db.add(wallet)
    db.commit()
    db.refresh(wallet)
    return wallet
