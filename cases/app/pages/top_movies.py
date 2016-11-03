"""
--------------------
Top IMDB movies page
--------------------
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

import re

from pom import ui
from selenium.webdriver.common.by import By

from cases.app.pages.base import PageBase

__all__ = [
    'PageTopMovies',
]


@ui.register_ui(link_social=ui.Link(By.TAG_NAME, 'a'))
class RowSocial(ui.Row):
    """Social item."""


class ListSocial(ui.List):
    """List of social items."""

    row_cls = RowSocial
    row_xpath = ".//div[contains(@class, 'dropdown-menu-item')]"


class CellMovie(ui.Block):
    """Cell of movie row."""

    @property
    def value(self):
        """Cell value."""
        def _clean_html(raw_html):
            return re.sub(r'<.*?>', '', raw_html)

        return _clean_html(super(CellMovie, self).value).strip()


@ui.register_ui(
    link_poster=ui.Link(By.CSS_SELECTOR, 'td.posterColumn > a'),
    link_title=ui.Link(By.CSS_SELECTOR, 'td.titleColumn > a'),
    label_year=ui.Link(By.CSS_SELECTOR, 'td.titleColumn > .secondaryInfo'),
    button_your_rating=ui.Button(By.CSS_SELECTOR, 'td.ratingColumn .unseen'),
    button_watch_list=ui.Button(
        By.CSS_SELECTOR, 'td.watchlistColumn .standalone'))
class RowMovie(ui.Row):
    """Row with movie."""

    cell_cls = CellMovie


class TableMovies(ui.Table):
    """Table of movies."""

    row_cls = RowMovie
    columns = {'poster': 1,
               'title': 2,
               'imdb_rating': 3,
               'your_rating': 4,
               'watch_list': 5}


@ui.register_ui(
    button_share=ui.Button(By.CSS_SELECTOR, 'button[title="Share"]'),
    combobox_sort_type=ui.ComboBox(By.NAME, 'sort'),
    button_sort_order=ui.Button(By.CLASS_NAME, 'lister-sort-reverse'),
    table_movies=TableMovies(By.CSS_SELECTOR, 'table.chart'),
    list_social_share=ListSocial(By.CSS_SELECTOR, '.dropdown-menu.menu-right'))
class PageTopMovies(PageBase):
    """Page with top 250 IMDB movies list."""

    url = '/chart/top?ref_=nv_mv_250_6'
