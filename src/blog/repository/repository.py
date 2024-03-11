from fastapi import HTTPException

# from src.entrypoint.database import blog
from .blog_repo import BlogRepo
from src.entrypoint.database import get_db


class InMemoryRep:
    def __init__(self):
        self.db = get_db()

    def base_query(self):
        # Base Query for DB calls
        return self.db.query(BlogRepo)

    def get(self, blog_id):
        return self.base_query().filter(BlogRepo.id == blog_id).first()

    def getall(self):
        return self.base_query().all()

    def add(self, item):
        item = BlogRepo(**item.__dict__)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, data):
        resp = False
        self.db.delete(data)
        self.db.commit()

        quick_check = self.base_query().filter(BlogRepo.title == data.title).first()
        if not quick_check:
            resp = True
        return resp

    def update(self, data: BlogRepo):
        updated_data = data
        self.db.commit()
        self.db.refresh(updated_data)
        return updated_data


blogRepo = InMemoryRep
