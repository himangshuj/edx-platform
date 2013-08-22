__author__ = 'vulcan'

from .sokratik import *
DEBUG = True
TEMPLATE_DEBUG = True
PIPELINE = False
DEFAULT_FILE_STORAGE = None
PIPELINE_SASS_ARGUMENTS = '--debug-info --require {proj_dir}/static/sass/bourbon/lib/bourbon.rb'.format(proj_dir=PROJECT_ROOT)
STATIC_ROOT = ENV_ROOT / "staticfiles"
PLATFORM_NAME = "sokratik-creator"
THEME_NAME = "sokratik-creator"

FAVICON_PATH = 'themes/%s/images/favicon.ico' % THEME_NAME

print FAVICON_PATH
print PLATFORM_NAME


