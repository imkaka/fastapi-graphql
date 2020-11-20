import pytest
from app.models.comment import Comment
from app.models.post import Post
from app.models.user import User


@pytest.fixture(scope="function")
def user():
    user = User()
    user.name = "Anil Khatri"
    user.address = "Lumbini"
    user.phone_number = 123456789
    user.sex = "male"
    user.save()

    return user


@pytest.fixture(scope="function")
def post(user):
    post = Post()
    post.title = "Fast API + GraphQL"
    post.body = "this is the post body and can be as long as possible"

    user.posts().save(post)
    return post


@pytest.fixture(scope="function")
def comment(user, post):
    comment = Comment()
    comment.body = "Is sajjan ko kya takleef hain bhai?"

    user.comments().save(comment)
    post.comments().save(comment)

    return comment
