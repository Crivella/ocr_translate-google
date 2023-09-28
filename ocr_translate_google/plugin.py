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
"""Plugin to implement google translation for ocr_translate."""

import datetime
import time

import googletrans
from ocr_translate import models as m


class GoogleTranslateModel(m.TSLModel):
    """OCRtranslate plugin to allow usage of google_translate as translator."""

    class Meta: # pylint: disable=missing-class-docstring
        proxy = True

    def __init__(self, *args, **kwargs):
        """Initialize the model."""
        super().__init__(*args, **kwargs)
        self.last = None
        self.translator = None

    def load(self):
        """Load the model into memory."""
        self.last = None
        self.translator = googletrans.Translator()

    def unload(self) -> None:
        """Unload the model from memory."""
        del self.translator

    def _translate(self, tokens: list, src_lang: str, dst_lang: str, options: dict = None) -> str | list[str]:
        """Translate a text using a the loaded model.

        Args:
            tokens (list): list or list[list] of string tokens to be translated.
            lang_src (str): Source language.
            lang_dst (str): Destination language.
            options (dict, optional): Options for the translation. Defaults to {}.

        Raises:
            TypeError: If text is not a string or a list of strings.

        Returns:
            Union[str,list[str]]: Translated text. If text is a list, returns a list of translated strings.
        """
        batch = False
        if isinstance(tokens[0], list):
            batch = True
            tokens = [' '.join(t) for t in tokens]
            tokens = '\n\n'.join(tokens)
        elif isinstance(tokens, str):
            tokens = ' '.join(tokens)
        while not self.last is None and datetime.datetime.now() - self.last < datetime.timedelta(seconds=2):
            time.sleep(0.2)
        self.last = datetime.datetime.now()
        res = self.translator.translate(tokens, src=src_lang, dest=dst_lang).text
        if batch:
            res = res.split('\n\n')
        return res
