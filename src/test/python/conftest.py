import pytest
from match.api import create_app
import numpy as np
from PIL import Image
from match.utils import delete_ids, ids_with_path, paths_at_location


def scrub_elasticsearch_test_data():
    pathes = paths_at_location(0, 1000)
    for path in pathes:
        if path.startswith("/test/") or path.startswith("/abc/"):
            delete_ids(ids_with_path(path))


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()

    scrub_elasticsearch_test_data()

    yield testing_client

    scrub_elasticsearch_test_data()

    ctx.pop()


@pytest.fixture(scope="module")
def test_image():
    return Image.fromarray((np.random.rand(600, 600, 3) * 255).astype(np.uint8))
