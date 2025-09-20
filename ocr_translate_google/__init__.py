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

__version__ = '0.3.0'

tsl_model_data = {
    'name': 'google_translate',
    'lang_src': [
        'af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bs', 'bg', 'co', 'he', 'hr', 'cs',
        'da', 'en', 'eo', 'et', 'ee', 'fi', 'fr', 'gl', 'ka', 'de', 'gn', 'gu', 'ha', 'he', 'hi', 'hu', 'is', 'ig',
        'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'rw', 'ko', 'ku', 'lo', 'la', 'lv', 'ln', 'lt', 'mk', 'mg', 'ms',
        'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'no', 'om', 'fa', 'pl', 'qu', 'ru', 'sm', 'sa', 'sr', 'sn', 'sd', 'sk',
        'sl', 'so', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'uk', 'ur', 'uz', 'vi',
        'cy', 'xh', 'yi', 'yo', 'zh', 'zht', 'zu'
        ],
    'lang_dst': [
        'af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bs', 'bg', 'co', 'he', 'hr', 'cs',
        'da', 'en', 'eo', 'et', 'ee', 'fi', 'fr', 'gl', 'ka', 'de', 'gn', 'gu', 'ha', 'he', 'hi', 'hu', 'is', 'ig',
        'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'rw', 'ko', 'ku', 'lo', 'la', 'lv', 'ln', 'lt', 'mk', 'mg', 'ms',
        'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'no', 'om', 'fa', 'pl', 'qu', 'ru', 'sm', 'sa', 'sr', 'sn', 'sd', 'sk',
        'sl', 'so', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'uk', 'ur', 'uz', 'vi',
        'cy', 'xh', 'yi', 'yo', 'zh', 'zht', 'zu'
        ],
    'lang_code': 'iso1',
    'entrypoint': 'google_translate.online',
    'iso1_map': {
        'zh': 'zh-cn',
        'zht': 'zh-tw',
    }
}
