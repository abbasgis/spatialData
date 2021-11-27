from app.db.database import SessionLocal


class QueryManager:
    @staticmethod
    def save(obj):
        with SessionLocal() as db:
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
