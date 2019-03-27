import io
import json

HEADERS = {"Content-Type": "multipart/form-data"}
ADD_DEL_PATH = "/abc/123"


def to_encoded_img(img, format="jpeg"):
    """Convert a PIL.Image to a form encoded compatible byte string"""
    with io.BytesIO() as img_b:
        img.save(img_b, format=format)
        img_encoded = img_b.getvalue()
    return io.BytesIO(img_encoded)


def test_add_handler(test_client, test_image):
    url = "/add"
    data = {"image": (to_encoded_img(test_image), "test.jpg"), "filepath": ADD_DEL_PATH}
    resp = test_client.post(url, headers=HEADERS, data=data)
    resp_json = json.loads(resp.data)
    print(json.dumps(resp_json, indent=4))
    assert resp_json["status"] == "ok"
    assert resp_json["error"] == []
    assert resp_json["result"] == []
    assert resp_json["method"] == "add"


def test_delete_handler(test_client):
    url = "/delete"
    data = {"filepath": ADD_DEL_PATH}
    resp = test_client.delete(url, headers=HEADERS, data=data)
    resp_json = json.loads(resp.data)
    print(json.dumps(resp_json, indent=4))
    assert resp_json["status"] == "ok"
    assert resp_json["error"] == []
    assert resp_json["result"] == []
    assert resp_json["method"] == "delete"


def test_search_handler():
    assert True


def test_compare_handler():
    assert True


def test_count_handler():
    assert True


def test_list_handler():
    assert True


def test_ping_handler():
    assert True
