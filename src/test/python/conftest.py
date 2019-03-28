import pytest
from match.api import create_app
import numpy as np
from PIL import Image


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture(scope="module")
def test_image():
    return Image.fromarray((np.random.rand(600, 600, 3) * 255).astype(np.uint8))
