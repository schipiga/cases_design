"""
--------------------------
Autotests for top 250 imdb
--------------------------

**Please, note that autotests may have different steps and cases, according to
the convenience of automation.** (*And usually it happens.*)
"""

from hamcrest import assert_that, has_length
import pytest

from cases import config


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

    def test_open_movie_details_by_title(self, top_movies_steps):
        top_movies_steps.show_movie_details(movie_number=0)

    def test_open_movie_details_by_icon(self, top_movies_steps):
        top_movies_steps.show_movie_details(movie_number=0, by_title=False)

    def test_reverse_movies_sort_order(self, top_movies_steps):
        top_movies_steps.reverse_movies_sort_order()
        top_movies_steps.reverse_movies_sort_order()

    @pytest.mark.parametrize('sort_type', [config.SORT_RANKING,
                                           config.SORT_IMDB_RATING,
                                           config.SORT_RELEASE_DATE,
                                           config.SORT_NUBMER_RATINGS,
                                           config.SORT_YOUR_RATING])
    def test_change_movies_sort_type(self, top_movies_steps, sort_type):
        top_movies_steps.change_movies_sort_type(sort_type)
        top_movies_steps.reverse_movies_sort_order()

    @pytest.mark.parametrize('movies_amount', [250])
    def test_movies_list_amount(self, app, movies_amount):
        app.open(app.page_top_movies)
        assert_that(app.page_top_movies.table_movies.rows,
                    has_length(movies_amount))
