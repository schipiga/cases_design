"""
----------
Login page
----------
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

from pom import ui
from selenium.webdriver.common.by import By

from cases.app.pages.base import PageBase

__all__ = [
    'PageLogin',
]


@ui.register_ui(
    link_facebook_login=ui.Link(
        By.CSS_SELECTOR, '.list-group-item span[class*="facebook-logo"]'),
    link_google_login=ui.Link(
        By.CSS_SELECTOR, '.list-group-item span[class*="google-logo"]'),
    link_amazon_login=ui.Link(
        By.CSS_SELECTOR, '.list-group-item span[class*="amazon-logo"]'),
    link_imdb_login=ui.Link(
        By.CSS_SELECTOR, '.list-group-item span[class*="imdb-logo"]'),
    link_create_account=ui.Link(
        By.CSS_SELECTOR, '.list-group-item.create-account'))
class PageLogin(PageBase):
    """Login IMDB page."""

    url = '/registration/signin'
