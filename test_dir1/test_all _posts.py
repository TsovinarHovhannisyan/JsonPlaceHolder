import requests
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_get_all_posts(start_test):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/')

    assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    posts = response.json()
    assert len(posts) > 0, 'Expected non-empty list of posts, but got an empty list'


@pytest.mark.smoke
@pytest.mark.regression
def test_get_post_by_id(start_test):
    id = 1
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')

    assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    post = response.json()
    assert post['id'] == id, f"Expected post ID {id}, but got {post['id']}"


@pytest.mark.regression
def test_create_post():
    # Define the data for the new post
    body = {
        "userId": 1,
        "title": "hayk",
        "body": "Lorem ipsum"
    }

    # Define headers for JSON content
    headers = {'Content-Type': 'application/json'}

    # Make a POST request to create the new post
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts/',
        json=body,
        headers=headers
    )

    # Check if the status code is 201 (Created)
    assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'

    # Verify that the response contains an 'id' field
    post = response.json()
    assert "id" in post, 'Expected "id" field in response'

    # Verify that the created post data matches the sent data
    assert body["userId"] == post["userId"], f'Expected userId {body["userId"]}, but got {post["userId"]}'
    assert body["title"] == post["title"], f'Expected title "{body["title"]}", but got "{post["title"]}"'
    assert body["body"] == post["body"], f'Expected body "{body["body"]}", but got "{post["body"]}"'

    # Verify the length of the response dictionary
    assert len(post) == 4, f'Expected 4 fields in response, but got {len(post)}'


@pytest.mark.regression
def test_put_post():
    id = 1
    body = {
        "userId": 1,
        "title": "kim",
        "body": "Lorem Ipsum"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{id}',
        json=body,
        headers=headers
    )

    assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    post = response.json()

    assert id == post['id'], f"Expected post ID {id}, but got {post['id']}"
    assert body["userId"] == post["userId"], f'Expected userId {body["userId"]}, but got {post["userId"]}'
    assert body["title"] == post["title"], f'Expected title "{body["title"]}", but got "{post["title"]}"'
    assert body["body"] == post["body"], f'Expected body "{body["body"]}", but got "{post["body"]}"'


@pytest.mark.regression
def test_patch_post():
    id = 1

    # Define the data to update in the post
    body = {
        "body": "Lorem Ipsum"
    }

    # Define headers for JSON content
    headers = {'Content-Type': 'application/json'}

    # Make a PATCH request to update the post
    response = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{id}',
        json=body,
        headers=headers
    )

    # Check if the status code is 200 (OK)
    assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    post = response.json()
    assert body["body"] == post["body"], f'Expected body "{body["body"]}", but got "{post["body"]}"'

    assert 'userId' in post, 'Expected "userId" field in response'
    assert 'title' in post, 'Expected "title" field in response'


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_post_by_id():
    id = 1
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{id}')
    # Check if the status code is 200 (OK)
    assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'


@pytest.mark.smoke
@pytest.mark.regression
def test_one():
    assert 1 == 1


@pytest.mark.xxx
@pytest.mark.regression
@pytest.mark.parametrize('x', [1, 2, 3, 4])
def test_two(x):
    print(x)
    assert 'hayk' == 'hayk'

