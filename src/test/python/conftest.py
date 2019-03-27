import pytest
from match.api import create_app
import random

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
    testImage = Image.new("RGB", (600, 600), (255, 255, 255))
    pixel = testImage.load()
    for x in range(600):
        for y in range(600):
            red = random.randrange(0, 255)
            blue = random.randrange(0, 255)
            green = random.randrange(0, 255)
            pixel[x, y] = (red, blue, green)
    return testImage
