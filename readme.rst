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

First of all let's define the type of testing. We see web pages, and seems it would be nice to verify its functionality. Nice toolkit for that is selenium. And should keep in mind, that selenium is exactly for functional testing only, not for load testing, not for markup testing. Btw some recommendations about other testing types:

- load testing - `yandex.tank <https://tech.yandex.ru/tank/>`_
- markup testing - `yandex.gemini <https://github.com/gemini-testing/gemini>`_
- integration and unit testing - commonly depends on backend language and framework.

Then let's to create test plan according to test design patterns and page functionality. And separate testcases according to severity (not priority! priority of bugs fixing is set by project manager(s)).

Critical:

- share button is clickable
- social buttons lead to social pages

Major:

- email has correct link

Minor:

- copy site address to clipboard

(to be continued...)
