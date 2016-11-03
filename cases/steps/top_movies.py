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


from .base import BaseSteps


class TopMoviesSteps(BaseSteps):
    """Containers steps."""

    def page_top_movies(self):
        """Open containers page if it isn't opened."""
        return self._open(self.app.page_top_movies)

    def share_with_social(self):
        """Step to share with social."""

    def change_movies_sort_type(self, sort_type):
        """Step to change movies sort type."""

    def reverse_movies_sort_order(self):
        """Step to reverse sort order."""

    def show_movie_details(self, movie_number, by_title=True):
        """Step to show detailed info about movie."""

    def like_movie(self, movie_number):
        """Step to like movie and increase its rating."""

    def add_movie_to_watch_list(self, movie_number):
        """Step to add movie to watch list."""
