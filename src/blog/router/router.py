from fastapi import APIRouter, status
from src.blog.service.service import BlogService

from src.blog.model.model import BlogPost, UpdateBlogPost

blog = APIRouter(prefix="/api/v1/blog", tags=["BLOG"])


@blog.get("/get", status_code=status.HTTP_200_OK)
async def blog_get(blog_id: int):
    return BlogService().get(blog_id=blog_id)


@blog.get("/getall", status_code=status.HTTP_200_OK)
async def blog_getall():
    return BlogService().getall()


@blog.post("/add", status_code=status.HTTP_200_OK)
async def blog_getall(blog: BlogPost):
    return BlogService().add(data=blog)


@blog.delete("/delete", status_code=status.HTTP_200_OK)
async def blog_getall(blog_id: str):
    return BlogService().delete(blog_id=blog_id)


@blog.put("/update", status_code=status.HTTP_200_OK)
async def blog_getall(blog_id: int, data: UpdateBlogPost):
    # updatePost = data.model_dump(exclude_unset=True)

    return BlogService().update(blog_id=blog_id, data=data)
