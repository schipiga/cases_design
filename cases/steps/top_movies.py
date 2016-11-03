"""
----------------
Top movies steps
----------------
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from hamcrest import assert_that, equal_to, has_length, starts_with
import pyperclip

from cases import config

from .base import BaseSteps


class TopMoviesSteps(BaseSteps):
    """Top movies steps."""

    def share_with_social(self, check=True):
        """Step to share with social."""
        page = self.app.page_top_movies
        page.button_share.click()

        if check:
            social_rows = page.list_social_share.rows
            assert_that(social_rows[0].link_social.href,
                        starts_with('http://www.facebook.com/sharer'))
            assert_that(social_rows[1].link_social.href,
                        starts_with('http://twitter.com/intent/tweet'))
            assert_that(social_rows[2].link_social.href,
                        starts_with('mailto:?subject=Check'))
            assert_that(social_rows[3].link_social.href,
                        starts_with('http://www.imdb.com/chart/top'))
            social_rows[3].click()
            assert_that(pyperclip.paste(),
                        equal_to('http://www.imdb.com/chart/top'))

    def change_movies_sort_type(self, sort_type, check=True):
        """Step to change movies sort type."""
        page = self.app.page_top_movies
        page.combobox_sort_type.value = sort_type

        if check:
            row_first = page.table_movies.rows[0]
            row_last = page.table_movies.rows[-1]

            if sort_type == config.SORT_RANKING:
                title_first = 'The Shawshank Redemption'
                title_last = 'Beauty and the Beast'

            if sort_type == config.SORT_IMDB_RATING:
                title_first = 'The Shawshank Redemption'
                title_last = 'Beauty and the Beast'

            if sort_type == config.SORT_RELEASE_DATE:
                title_first = 'Zootopia'
                title_last = 'The Kid'

            if sort_type == config.SORT_NUBMER_RATINGS:
                title_first = 'The Shawshank Redemption'
                title_last = 'The Passion of Joan of Arc'

            if sort_type == config.SORT_YOUR_RATING:
                title_first = 'The Shawshank Redemption'
                title_last = 'Beauty and the Beast'

            assert_that(row_first.link_title.value, equal_to(title_first))
            assert_that(row_last.link_title.value, equal_to(title_last))

    def reverse_movies_sort_order(self, check=True):
        """Step to reverse sort order."""
        def _get_numbers(rows):
            numbers = []
            for row in rows:
                number = row.cell('title').value.split('.', 1)[0]
                numbers.append(int(number))
            return numbers

        page = self.app.page_top_movies

        if check:
            numbers_before = _get_numbers(page.table_movies.rows)

        page.button_sort_order.click()

        if check:
            numbers_after = _get_numbers(page.table_movies.rows)
            assert_that(list(reversed(numbers_after)),
                        equal_to(numbers_before))

    def show_movie_details(self, movie_number, by_title=True, check=True):
        """Step to show detailed info about movie."""
        page = self.app.page_top_movies
        row_movie = page.table_movies.rows[movie_number]

        movie_title = row_movie.link_title.value
        movie_year = row_movie.label_year.value.strip('()')
        movie_rating = row_movie.cell('imdb_rating').value

        if by_title:
            row_movie.link_title.click()
        else:
            row_movie.link_poster.click()

        if check:
            with self.app.page_movie_details as page:
                assert_that(self.app.current_page, equal_to(page))
                assert_that(page.label_title.value, starts_with(movie_title))
                assert_that(page.link_year.value, equal_to(movie_year))
                assert_that(page.label_rating.value, equal_to(movie_rating))

    def like_movie(self, movie_number, check=True):
        """Step to like movie and increase its rating."""
        page = self.app.page_top_movies
        row_movie = page.table_movies.rows[movie_number]
        row_movie.button_your_rating.click()

        if check:
            assert_that(self.app.current_page, equal_to(self.app.page_login))
            self.check_page_login_buttons()

    def add_movie_to_watch_list(self, movie_number, check=True):
        """Step to add movie to watch list."""
        page = self.app.page_top_movies
        row_movie = page.table_movies.rows[movie_number]
        row_movie.button_watch_list.click()

        if check:
            assert_that(self.app.current_page, equal_to(self.app.page_login))
            self.check_page_login_buttons()

    def check_page_login_buttons(self):
        """Step to check page login buttons."""
        self.app.page_login.link_facebook_login.wait_for_presence()
        self.app.page_login.link_google_login.wait_for_presence()
        self.app.page_login.link_amazon_login.wait_for_presence()
        self.app.page_login.link_imdb_login.wait_for_presence()
        self.app.page_login.link_create_account.wait_for_presence()

    def check_movies_list_has_length(self, length):
        """Step to check movies list length."""
        assert_that(
            self.app.page_top_movies.table_movies.rows, has_length(length))
