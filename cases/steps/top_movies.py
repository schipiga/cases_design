"""
Containers steps.

@author: schipiga@mirantis.com
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

from hamcrest import assert_that, equal_to, starts_with
import pyperclip

from .base import BaseSteps


class TopMoviesSteps(BaseSteps):
    """Containers steps."""

    def page_top_movies(self):
        """Open containers page if it isn't opened."""
        return self._open(self.app.page_top_movies)

    def share_with_social(self, check=True):
        """Step to share with social."""
        page = self.page_top_movies()
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
            # TODO(schipiga): use latest browser version.
            # assert_that(pyperclip.paste(),
            #             equal_to('http://www.imdb.com/chart/top'))

    def change_movies_sort_type(self, sort_type):
        """Step to change movies sort type."""

    def reverse_movies_sort_order(self):
        """Step to reverse sort order."""

    def show_movie_details(self, movie_number, by_title=True):
        """Step to show detailed info about movie."""

    def like_movie(self, movie_number, check=True):
        """Step to like movie and increase its rating."""
        page = self.page_top_movies()
        row_movie = page.table_movies.rows[movie_number]
        row_movie.button_your_rating.click()

        if check:
            assert_that(self.app.current_page, equal_to(self.app.page_login))
            self.check_page_login_buttons()

    def add_movie_to_watch_list(self, movie_number, check=True):
        """Step to add movie to watch list."""
        page = self.page_top_movies()
        row_movie = page.table_movies.rows[movie_number]
        row_movie.button_watch_list.click()

        if check:
            assert_that(self.app.current_page, equal_to(self.app.page_login))
            self.check_page_login_buttons()

    def check_page_login_buttons(self):
        self.app.page_login.link_facebook_login.wait_for_presence()
        self.app.page_login.link_google_login.wait_for_presence()
        self.app.page_login.link_amazon_login.wait_for_presence()
        self.app.page_login.link_imdb_login.wait_for_presence()
        self.app.page_login.link_create_account.wait_for_presence()
