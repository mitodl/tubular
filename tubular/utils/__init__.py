"""
Initialization code for the utils module.
"""
from __future__ import unicode_literals
import os
from collections import namedtuple

# Time in seconds to wait between polls of Asgard or AWS.
WAIT_SLEEP_TIME = int(os.environ.get("WAIT_SLEEP_TIME", 5))

# Time in seconds to wait between when new ASGs are enabled -and- when health checks
# are performed on those new ASGs in order to begin disabling old ASGs.
DISABLE_OLD_ASG_WAIT_TIME = int(os.environ.get("DISABLE_OLD_ASG_WAIT_TIME", 0))

EDP = namedtuple('EDP', ['environment', 'deployment', 'play'])
