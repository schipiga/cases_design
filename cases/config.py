import os

UI_TIMEOUT = 5
ACTION_TIMEOUT = 30
IDBM_URL = 'http://www.imdb.com/'
RESOLUTION = 1920, 1080


SORT_RANKING = 'Ranking'
SORT_IMDB_RATING = 'IMDb Rating'
SORT_RELEASE_DATE = 'Release Date'
SORT_NUBMER_RATINGS = 'Number of Ratings'
SORT_YOUR_RATING = 'Your Rating'

TEST_REPORTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                'test_reports'))

XVFB_LOCK = '/tmp/cases_xvfb.lock'
