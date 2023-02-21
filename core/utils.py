from starlette.requests import Request

from core.database import SessionLocal


def get_db(request: Request):
    return request.state.db


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
