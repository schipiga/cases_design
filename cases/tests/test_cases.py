"""
--------------------------
Autotests for top 250 imdb
--------------------------
"""

import pytest


@pytest.mark.usefixtures('top_page')
class TestTop250Imdb(object):
    """Tests for top 250 IMDB movies page."""

    def test_share_with_social(self):
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
