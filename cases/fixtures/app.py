import pytest

from cases import app as _app
from cases import config
from cases import steps

__all__ = [
    'app',
    'top_movies_page',
    'top_steps',
]


@pytest.fixture
def app():
    """Initial fixture to start."""
    app = _app.Application(config.IDBM_URL)

    yield app

    app.quit()


@pytest.fixture
def top_steps(app):
    return steps.TopMoviesSteps(app)


@pytest.fixture
def top_movies_page(top_steps):
    return top_steps.page_top_movies()
