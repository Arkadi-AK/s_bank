from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from core.database import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    # type =
    # currency =
    balance = Column(Float, default=0.0)
    created_on = Column(DateTime, default=datetime.now)
    modified_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    owner = Column(Integer, ForeignKey("users.id"))
    owner_id = relationship("User")
