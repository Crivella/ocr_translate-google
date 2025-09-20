###################################################################################
# ocr_translate-google - a google_translate plugin for ocr_translate              #
# Copyright (C) 2023-present Davide Grassano                                      #
#                                                                                 #
# This program is free software: you can redistribute it and/or modify            #
# it under the terms of the GNU General Public License as published by            #
# the Free Software Foundation, either version 3 of the License.                  #
#                                                                                 #
# This program is distributed in the hope that it will be useful,                 #
# but WITHOUT ANY WARRANTY; without even the implied warranty of                  #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                   #
# GNU General Public License for more details.                                    #
#                                                                                 #
# You should have received a copy of the GNU General Public License               #
# along with this program.  If not, see {http://www.gnu.org/licenses/}.           #
#                                                                                 #
# Home: https://github.com/Crivella/ocr_translate-google                          #
###################################################################################
"""Tests for the ocr_translate-google plugin."""

# pylint: disable=unused-argument

import pytest

from ocr_translate_google import plugin as octg_plugin


@pytest.fixture(scope='function')
def mock_translate():
    """Mock of the googletrans Translator."""
    class Result():
        """Mock the output"""
        def __init__(self):
            self.text = None

    async def mock_function(text, *args, src, dest):
        res = Result()
        res.text = text
        mock_function.called = True
        mock_function.args = (text,)
        mock_function.kwargs = {'src': src, 'dest': dest}

        return res

    return mock_function

@pytest.fixture(scope='function')
def mock_called():
    """Mock of the time.sleep function."""
    def mock_function(*args, **kwargs):
        mock_function.called = True
        mock_function.args = args
        mock_function.kwargs = kwargs

    return mock_function

@pytest.fixture(scope='function')
def mock_datetime():
    """Mock of the datetime.datetime.now function."""
    def mock_function():
        mock_function.called = True
        mock_function.args = ()
        mock_function.kwargs = {}
        mock_function.count += 1
        return mock_function.count

    mock_function.count = 0
    mock_function.now = mock_function

    return mock_function

@pytest.fixture(scope='function')
def gt_model():
    """Fixture to create a GoogleTranslateModel instance."""
    model = octg_plugin.GoogleTranslateModel()
    model.DISABLE_LOAD_EVENTS = True
    return model
