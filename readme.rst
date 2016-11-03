---------------
Task to resolve
---------------

For the page http://www.imdb.com/chart/top?ref_=nv_mv_250_6, please do the following:

#. List all the test cases you consider necessary ordered by priority starting from the must have ones (at least 10)
#. What tests you would add to the compulsory pre-release test suite?
#. Describe test cases #4 and #8 in details taking into consideration that these tests will be performed by junior testers.
#. Cover at least 2 cases (#4, #8, maybe some others) with automated tests. Make sure that instructions provided with your code allow it to be run in Linux environment.

--------
Solution
--------

First of all let's define the type of testing. We see a web page, and seems it would be nice to verify its functionality. Nice toolkit for that is selenium. And should keep in mind, that selenium is exactly for functional testing only, not for load testing, not for markup testing. Btw some recommendations about other testing types:

- load testing - `yandex.tank <https://tech.yandex.ru/tank/>`_
- markup testing - `yandex.gemini <https://github.com/gemini-testing/gemini>`_
- integration and unit testing - commonly depends on backend language and framework.

Then let's create test plan according to test design patterns and page functionality. And separate testcases according to severity (not priority! priority of bugs fixing is set by project manager(s)).

**Test suite preconditions:**

#. User is not authenticated at IMDB site.

**Critical:**

#. Page should looks fine and all active UI elements should be clickable in popular browser. (List of top browsers: http://www.w3schools.com/browsers/. Special attention should be paid to IE. It is not functional testcase but very critical).
#. Clicking to movie title link leads to movie details page.
#. Clicking to movie star "your rating" leads to login page.
#. Clicking to movie button "add to watchlist" leads to login page.
#. Share button is clickable.
#. In dropdown menu social buttons lead to social pages.

**Major:**

#. Clicking to movie icon leads to movie details page.
#. Sort type "Ranking" is correct.
#. Sort type "IMDb Rating" is correct.
#. Sort type "Release Date" is correct.
#. Sort type "Number of Ratings" is correct.
#. Sort type "Your Rating" is correct.
#. In dropdown menu email item has correct link.
#. Top list includes exactly 250 items.

**Minor:**

#. Reverse sort order link works correct.
#. Top list numeration has correct order by default.
#. Copy site address to clipboard in dropdown menu.

Let's describe some testcases, as they should be presented at test plan management tool (would like to recommend http://www.gurock.com/testrail/).

Scenario: **Clicking to movie title link leads to movie details page**

**Setup:**

#. Page http://www.imdb.com/chart/top?ref_=nv_mv_250_6 is opened in browser.

**Steps:**

#. Click title movie of first item in movies list
    - Page with detailed info about exactly that movie is opened.

------------------------------------

Scenario: **Share button is clickable**

**Setup:**

#. Page http://www.imdb.com/chart/top?ref_=nv_mv_250_6 is opened in browser.

**Steps:**

#. Click button "Share".
    - Dropdown menu with social buttons to share are present (*QA engineer should be familiar with project and understand what it's meant under "social buttons to share" and other concepts. It should not be described in every step in details.*)

----------------------------------------

Scenario: **In dropdown menu social buttons lead to social pages**

**Setup:**

#. Page http://www.imdb.com/chart/top?ref_=nv_mv_250_6 is opened in browser.

**Steps:**

#. Click button "Share".
    - Dropdown menu with social buttons to share are present.
#. Click button "Facebook"
    - Dropdown menu is closed.
    - Facebook page to share IMDB page is opened.
#. Click button "Twitter"
    - Dropdown menu is closed.
    - Twitter page to tweet IMDB page is opened.

----------------------------------------------

Scenario: **Copy site address to clipboard in dropdown menu**

**Setup:**

#. Page http://www.imdb.com/chart/top?ref_=nv_mv_250_6 is opened in browser.

**Steps:**

#. Click button "Share".
    - Dropdown menu with social buttons to share are present.
#. Click item "Copy"
    - Dropdown menu is closed.
#. Open text editor and push Ctrl+V
    - link "http://www.imdb.com/chart/top" is pasted.
