import os

import pytest
import xvfbwrapper

from cases import config
from cases.third_party import video_recorder
from cases.third_party import process_mutex
from cases.third_party import utils

__all__ = [
    'report_dir',
    'virtual_display',
    'video_capture',
]


@pytest.fixture
def report_dir(request):
    """Create report directory to put test logs."""
    _report_dir = os.path.join(config.TEST_REPORTS_DIR,
                               utils.slugify(request.node.name))
    if not os.path.isdir(_report_dir):
        os.makedirs(_report_dir)
    return _report_dir


@pytest.fixture(scope='session')
def virtual_display(request):
    """Run test in virtual X server if env var is defined."""
    if request.config.option.disable_virtual_display:
        return

    _virtual_display = xvfbwrapper.Xvfb(width=1920, height=1080)
    # workaround for memory leak in Xvfb taken from:
    # http://blog.jeffterrace.com/2012/07/xvfb-memory-leak-workaround.html
    # and disables X access control
    args = ["-noreset", "-ac"]

    _virtual_display.extra_xvfb_args.extend(args)

    with process_mutex.Lock(config.XVFB_LOCK):
        _virtual_display.start()

    request.addfinalizer(_virtual_display.stop)


@pytest.yield_fixture(autouse=True)
def video_capture(request, virtual_display, report_dir):
    """Capture video of test."""
    if request.config.option.disable_video_capture:
        return

    recorder = video_recorder.VideoRecorder(
        os.path.join(report_dir, 'video.mp4'))
    recorder.start()

    request.addfinalizer(recorder.stop)
