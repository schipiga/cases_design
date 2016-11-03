"""
-----------------------------------
Pytest plugin to clean test reports
-----------------------------------

It ensures two things:

* Remove test reports folder before tests launching
* Remove test report folder if test is passed

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
# limitations under the License.from functools import wraps

import os
import shutil

from cases import config as cases_config

__all__ = [
    'pytest_addoption',
    'pytest_configure',
]


def pytest_addoption(parser):
    """Hook to register checker options."""
    parser.addoption("--disable-video-capture", action="store_true",
                     help="disable video capture")
    parser.addoption("--disable-virtual-display", action="store_true",
                     help="disable virtual display")


def pytest_configure(config):
    """Pytest hook to remove test reports before tests launching."""
    if not hasattr(config, 'slaveinput'):  # if it is not xdist slave node
        if os.path.isdir(cases_config.TEST_REPORTS_DIR):
            shutil.rmtree(cases_config.TEST_REPORTS_DIR)
        os.mkdir(cases_config.TEST_REPORTS_DIR)
