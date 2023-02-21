from datetime import datetime

from pydantic import BaseModel


class WalletBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class WalletList(WalletBase):
    id: int
    name: str
    # type
    # currency
    balance: float
    created_on: datetime
    modified_on: datetime


class WalletCreate(WalletBase):
    created_on: datetime
