"""
--------------------------
Autotests for top 250 imdb
--------------------------

Please, note that autotests may have different steps and case, according to
the convenience of automation (And usually it happens).
"""

import pytest


@pytest.mark.usefixtures('top_page')
class TestTop250Imdb(object):
    """Tests for top 250 IMDB movies page.

    **Preconditions:**

    #. User is not authenticated.
    """

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
