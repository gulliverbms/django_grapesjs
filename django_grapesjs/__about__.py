import os.path
from datetime import datetime

__all__ = [
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
]


__title__ = "django_grapesjs"
__summary__ = "A django wrapper for grapes.js library."
__uri__ = ""  # @TODO: Place a uri

__version__ = "0.0.7"

__author__ = "TheLazzziest"
__email__ = ""  # @TODO: Leave an email

__license__ = "MIT"
__copyright__ = "%s %s" % (datetime.strftime(datetime.now(), "%Y"), __author__,)
