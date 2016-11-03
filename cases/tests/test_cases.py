"""
---------------------------------
Autotests for top 250 IMDB movies
---------------------------------

**Please, note that autotests may have different steps and cases than manual
tests, according to the convenience of automation.**
(*And usually it happens.*)

These autotests are implemented with POM framework
(http://pom.readthedocs.io/en/latest/, https://github.com/sergeychipiga/pom)
and STEPS-methodology.

If you are interesting how POM works in enterprise testing, please visit
https://github.com/Mirantis/mos-horizon/tree/v9.1.

If you are curious about STEPS-methodology in enterprise testing, please visit
http://stepler.readthedocs.io/, https://github.com/Mirantis/stepler.

**How to install:**

*Verified on Ubuntu v14.04 and higher.*

Make following commands in terminal::

   echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
   sudo apt-get update
   sudo apt-get install -y google-chrome-stable libav-tools xvfb xsel xclip python-pip git gconf2
   sudo pip install virtualenv
   git clone https://github.com/sergeychipiga/cases_design
   cd cases_design
   virtualenv .venv
   . .venv/bin/activate
   pip install -U pip
   pip install -r requirements.txt
   pip install -e .

**How to launch:**

#. ``py.test cases -v --junitxml=test_report.xml`` - single thread
#. ``py.test cases -v --junitxml=test_report.xml -n 2`` - two threads
#. ``py.test cases -v --junitxml=test_report.xml -n auto`` - autocalc threads

Results are available in folder ``test_results`` including
**video capture of virtual display**.

**How to debug:**

If you use ``ipdb`` you should disable stdout capture:

#. ``py.test cases -v --disable-video-capture --disable-virtual-display -s``
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

import pytest

from cases import config


class TestTop250Imdb(object):
    """Functional e2e tests for top 250 IMDB movies page.

    **Preconditions:**

    #. User is not authenticated.
    """

    def test_share_with_social(self, top_movies_steps):
        """**Scenario:** User can share top IMDB movies with social networks.

        **Setup:**

        #. Open top IMDB movies page.

        **Steps:**

        #. Click ``Share`` button.
        #. Check that all social links are clickable.

        **Teardown:**

        #. Close browser.
        """
        top_movies_steps.share_with_social()

    def test_like_movie(self, top_movies_steps):
        """**Scenario:** If user likes movie, it leads to login page.

        **Setup:**

        #. Open top IMDB movies page.

        **Steps:**

        #. Like movie in movies list.
        #. Check page login page is opened.

        **Teardown:**

        #. Close browser.
        """
        top_movies_steps.like_movie(movie_number=0)

    def test_add_movie_to_watch_list(self, top_movies_steps):
        """**Scenario:** If user adds movie to watch list, it leads to login
                         page.

        **Setup:**

        #. Open top IMDB movies page.

        **Steps:**

        #. Add movie in movies list to watch list.
        #. Check page login page is opened.

        **Teardown:**

        #. Close browser.
        """
        top_movies_steps.add_movie_to_watch_list(movie_number=0)

    def test_open_movie_details_by_title(self, top_movies_steps):
        """**Scenario:** Detailed info movie page is opened when user clicks
                         title of movie.

        **Setup:**

        #. Open top IMDB movies page.

        **Steps:**

        #. Click movie title.
        #. Check that page with detailed info about movie is opened.

        **Teardown:**

        #. Close browser.
        """
        top_movies_steps.show_movie_details(movie_number=0)

    def test_open_movie_details_by_icon(self, top_movies_steps):
        """**Scenario:** Detailed info movie page is opened when user clicks
                         icon of movie.

        **Setup:**

        #. Open top IMDB movies page.

        **Steps:**

        #. Click movie icon.
        #. Check that page with detailed info about movie is opened.

        **Teardown:**

        #. Close browser.
        """
        top_movies_steps.show_movie_details(movie_number=0, by_title=False)

    def test_reverse_movies_sort_order(self, top_movies_steps):
        """**Scenario:** Clicking on "Reverse sort" button leads to reverse of
                         movies list.

        **Setup:**

        #. Open top IMDB movies page.

        **Steps:**

        #. Click "Reverse sort" button.
        #. Check that movies list is reversed.
        #. Click "Reverse sort" button.
        #. Check that movies list is reversed.

        **Teardown:**

        #. Close browser.
        """
        top_movies_steps.reverse_movies_sort_order()
        top_movies_steps.reverse_movies_sort_order()

    @pytest.mark.parametrize('sort_type', [config.SORT_RANKING,
                                           config.SORT_IMDB_RATING,
                                           config.SORT_RELEASE_DATE,
                                           config.SORT_NUBMER_RATINGS,
                                           config.SORT_YOUR_RATING])
    def test_change_movies_sort_type(self, top_movies_steps, sort_type):
        """**Scenario:** Changing of sort type leads to reordering of movies
                         list.

        **Setup:**

        #. Open top IMDB movies page.

        **Steps:**

        #. Change sort type of movies list.
        #. Check that movies list order was changed.
        #. Click "Reverse sort" button.
        #. Check that movies list is reversed.

        **Teardown:**

        #. Close browser.
        """
        top_movies_steps.change_movies_sort_type(sort_type)
        top_movies_steps.reverse_movies_sort_order()

    @pytest.mark.parametrize('movies_amount', [250])
    def test_movies_list_amount(self, top_movies_steps, movies_amount):
        """**Scenario:** Movies list contains exaclty 250 items.

        **Setup:**

        #. Open top IMDB movies page.

        **Steps:**

        #. Check that movies list contains exaclty 250 items.

        **Teardown:**

        #. Close browser.
        """
        top_movies_steps.check_movies_list_has_length(movies_amount)
