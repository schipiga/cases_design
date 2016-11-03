
__all__ = [
    'slugify',
]


def slugify(string):
    """Slugify test names to put test results in folder with test name."""
    return ''.join(s if s.isalnum() else '_' for s in string).strip('_')
