"""
------
Config
------
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

CHROMEDRIVER_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'third_party', 'chromedriver'))

XVFB_LOCK = '/tmp/cases_xvfb.lock'
