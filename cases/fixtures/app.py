import pytest

from cases import app as _app
from cases import config
from cases import steps

__all__ = [
    'app',
    'top_movies_steps',
]


@pytest.fixture
def app():
    """Initial fixture to start."""
    app = _app.Application(config.IDBM_URL)

    yield app

    app.quit()


@pytest.fixture
def top_movies_steps(app):
    app.open(app.page_top_movies)
    return steps.TopMoviesSteps(app)
