"""
--------------------------
Autotests for top 250 imdb
--------------------------

**Please, note that autotests may have different steps and cases, according to
the convenience of automation.** (*And usually it happens.*)
"""

import pytest


@pytest.mark.usefixtures('top_movies_page')
class TestTop250Imdb(object):
    """Functional e2e tests for top 250 IMDB movies page.

    **Preconditions:**

    #. User is not authenticated.
    """

    def test_share_with_social(self, top_movies_steps):
        """**Scenario:** Unauthorized user can share top IMDB movies with
        social networks.

        **Setup:**

        #. Open top IMDB page.

        **Steps:**

        #. Click ``Share`` button.
        #. Check that all social links are clickable.

        **Teardown:**

        #. Close browser.
        """
        top_movies_steps.share_with_social()

    def test_like_movie(self, top_movies_steps):
        top_movies_steps.like_movie(movie_number=0)

    def test_add_movie_to_watch_list(self, top_movies_steps):
        top_movies_steps.add_movie_to_watch_list(movie_number=0)
