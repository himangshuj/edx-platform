__author__ = 'vulcan'
from dev import *

THEME_NAME = "stanford"
if not THEME_NAME is None:
    enable_theme(THEME_NAME)
    FAVICON_PATH = 'themes/%s/images/favicon.ico' % THEME_NAME
