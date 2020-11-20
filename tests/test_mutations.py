from .fixtures import *  # noqa


def test_create_user(client):
    query = """
    mutation {
        createUser(userDetails: {
            name: "Test User",
            sex: "male",
            address: "My Address",
            phoneNumber: "123456789",
        })
        {
            id
            name
            address
        }
    }
    """

    result = client.execute(query)
    assert result['data']['createUser']['id'] == 1
    assert result['data']['createUser']['name'] == "Test User"


def test_create_post(client, user):
    query = """
    mutation createPost($userId: Int!) {
    createPost(postDetails: {userId: $userId, title: "Fast API", body: "Fast API + GraphQL"}) {
        id
        userId
        title
        body
        comments {
          body
        }
        }
    }
    """
    params = {"userId": user.id}

    result = client.execute(query, variable_values=params)
    assert result['data']['createPost']['id'] == 1
    assert result['data']['createPost']['userId'] == user.id
    assert result['data']['createPost']['title'] == "Fast API"


def test_create_comment(client, user, post):
    query = """
    mutation createComment($userId: Int!, $postId: Int!) {
      createComment(commentDetails: {userId: $userId, postId: $postId, body: "Great"}) {
        id
        userId
        postId
        body
      }
    }
    """
    params = {"userId": user.id, "postId": post.id}

    result = client.execute(query, variable_values=params)
    assert result['data']['createComment']['id'] == 1
    assert result['data']['createComment']['postId'] == post.id
    assert result['data']['createComment']['body'] == "Great"
