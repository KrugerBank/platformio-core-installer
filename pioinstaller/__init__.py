# Copyright (c) 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging.config

VERSION = (1, 1, 3)
__version__ = ".".join([str(s) for s in VERSION])

__title__ = "platformio-installer"
__description__ = "An installer for PlatformIO Core"

__url__ = "https://platformio.org"

__author__ = "PlatformIO Labs"
__email__ = "contact@piolabs.com"


__license__ = "Apache-2.0"
__copyright__ = "Copyright 2014-present PlatformIO"


logging.basicConfig(format="%(levelname)s: %(message)s")
logging.config.dictConfig(
    {"version": 1, "loggers": {"pioinstaller": {"level": "INFO"}}}
)
