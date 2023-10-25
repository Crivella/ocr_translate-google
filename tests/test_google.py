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

# pylint: disable=missing-function-docstring,missing-class-docstring,protected-access

from importlib.metadata import entry_points

import googletrans
import pytest

import ocr_translate_google as octg
import ocr_translate_google.plugin as octg_plugin


def test_entrypoint():
    """The entrypoint defined in the model should not be changed."""
    # Updating the pluging with a change in entrypoint would break the app unless model entries are regenerated.
    # This restriction might be released in the future.
    assert octg.tsl_model_data['entrypoint'] == 'google_translate.online'

def test_entrypoint_pyproj():
    """The entrypoint defined for the model data should match the one exported in pyproject.toml."""
    ept_group = 'ocr_translate.tsl_models'
    ept_name = octg.tsl_model_data['entrypoint']
    for ept in entry_points(group=ept_group, name=ept_name):
        cls = ept.load()

    assert cls is octg_plugin.GoogleTranslateModel

def test_load():
    """Test that the model is loaded correctly."""
    obj = octg_plugin.GoogleTranslateModel()

    assert obj.translator is None
    obj.load()
    assert isinstance(obj.translator, googletrans.Translator)

def test_unload():
    """Test that the model is unloaded correctly."""
    obj = octg_plugin.GoogleTranslateModel()
    obj.load()
    assert isinstance(obj.translator, googletrans.Translator)
    obj.unload()
    assert obj.translator is None

def test_translate_nonbatch(monkeypatch, mock_translate):
    """Test that translate calls the translator correctly."""
    obj = octg_plugin.GoogleTranslateModel()
    obj.load()
    monkeypatch.setattr(obj.translator, 'translate', mock_translate)

    tokens = ['tok1', 'tok2']
    expected = 'tok1 tok2'

    res = obj._translate(tokens, 'ja', 'en')

    assert mock_translate.called
    assert mock_translate.args == (expected,)
    assert mock_translate.kwargs == {'src': 'ja', 'dest': 'en'}

    assert res == expected

def test_translate_batch(monkeypatch, mock_translate):
    """Test that translate calls the translator correctly."""
    obj = octg_plugin.GoogleTranslateModel()
    obj.load()
    monkeypatch.setattr(obj.translator, 'translate', mock_translate)

    tokens = [['tok1', 'tok2'], ['tok3', 'tok4']]
    expected = 'tok1 tok2\n\ntok3 tok4'

    res = obj._translate(tokens, 'ja', 'en')

    assert mock_translate.called
    assert mock_translate.args == (expected,)
    assert mock_translate.kwargs == {'src': 'ja', 'dest': 'en'}

    assert res == expected.split('\n\n')

def test_translate_exception(monkeypatch):
    """Test that translate returns an empty string if an exception is raised."""
    obj = octg_plugin.GoogleTranslateModel()
    obj.load()

    def mock_raise(*args, **kwargs):
        raise TypeError
    monkeypatch.setattr(obj.translator, 'translate', mock_raise)

    res = obj._translate(['tok1', 'tok2'], 'ja', 'en')

    assert res == ' '


def test_throttling(monkeypatch, mock_translate, mock_called, mock_datetime):
    """Test that consecutive calls to translate are throttled."""
    monkeypatch.setattr(octg_plugin.time, 'sleep', mock_called)
    # Needed to make sure test result does not depend on PC speed or has to run for 2+ seconds
    monkeypatch.setattr(octg_plugin.datetime, 'datetime', mock_datetime)
    monkeypatch.setattr(octg_plugin.datetime, 'timedelta', lambda seconds: seconds)
    obj = octg_plugin.GoogleTranslateModel()
    obj.load()
    monkeypatch.setattr(obj.translator, 'translate', mock_translate)

    tokens = ['tok1', 'tok2']

    obj._translate(tokens, 'ja', 'en')
    obj._translate(tokens, 'ja', 'en', options={'delta_thr': 2})

    assert hasattr(mock_called, 'called')

def test_no_token_input():
    """Test that an empty string is returned if no tokens are passed."""
    obj = octg_plugin.GoogleTranslateModel()
    obj.load()

    res = obj._translate([''], 'ja', 'en')

    assert res == [' ']