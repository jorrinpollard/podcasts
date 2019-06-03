from __future__ import division, absolute_import, print_function
from logging import handlers
import logging
import sys

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(
    logging.Formatter("%(asctime)s [ podcasts | %(levelname)-5.5s] %(message)s")
)

logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)
