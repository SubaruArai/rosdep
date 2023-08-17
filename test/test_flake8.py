# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import pathlib
import subprocess
import sys

import pytest


@pytest.mark.flake8
@pytest.mark.linter
def test_flake8():
    result = subprocess.run(
        ['flake8'],
        cwd=pathlib.Path(__file__).parent.parent,
        capture_output=True,
        check=False,
    )
    # pipe stdout to stdout, stderr to stderr
    print(result.stdout.decode('utf-8'), end='')
    print(result.stderr.decode('utf-8'), end='', file=sys.stderr)
    assert 0 == result.returncode, "flake8 found violations"
