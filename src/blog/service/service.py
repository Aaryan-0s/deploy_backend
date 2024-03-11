from src.blog.repository.repository import blogRepo
from src.blog.model.model import BlogPost


class BlogService:
    def __init__(self):
        self.repo = blogRepo()

    def get(self, blog_id):
        blog = self.repo.get(blog_id=blog_id)
        return blog

    def getall(self):
        blog = self.repo.getall()
        return blog

    def add(self, data):
        return self.repo.add(item=data)

    def delete(self, blog_id):
        data = self.repo.get(blog_id=blog_id)
        if data:
            return self.repo.delete(data=data)
        return "Not Deleted"

    def update(self, blog_id, data):
        data1 = self.repo.get(blog_id=blog_id)
        # data1=BlogPost(**data1.__dict__)
        data = data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(data1, key, value)
        # data1

        # get data from database
        # update data from user input
        # and pass to repo
        return self.repo.update(data=data1)


service = BlogService
