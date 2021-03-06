"""Find all URLs in apps and load them."""
from __future__ import print_function

import importlib
from magpy.server.database import Database
from magpy.server.urls import URLS

class URLLoader(object):
    """Load URLs from apps."""

    def __init__(self):
        """Load URLs."""
        self.apps = []
        self.database = Database()

    def get_urls(self):
        """Get the urls."""
        apps = self.database.get_app_list()
        if not apps:
            return URLS

        urls = URLS
        for app in apps:
            url_path = '%s.urls' % app
            try:
                url_module = importlib.import_module(url_path)
            except:
                print("Cannot import: %s" % url_path)
                print("Skipping app: %s" % app)
            else:
                urls.extend(getattr(url_module, 'URLS', []))
        return urls
