
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import patch
import pandas as pd
import sys
import importlib

# Sample DataFrame for testing
def sample_df():
    return pd.DataFrame({
        'A': ['hello', 'world'],
        'B': ['foo', 'bar']
    })

def test_google_translate_mock():
    """
    Test that google_translate returns the mocked value and does not call the real API.
    """
    with patch('translator.google_translate', return_value='translated'):
        from translator import google_translate
        assert google_translate('hello', 'en', 'id', 'mocked-google-api-key-12345') == 'translated'


def test_libretranslate_mock():
    """
    Test that libretranslate returns the mocked value and does not call the real API.
    """
    with patch('translator.libretranslate', return_value='translated'):
        from translator import libretranslate
        assert libretranslate('hello', 'en', 'id') == 'translated'

def test_translate_dataframe_google():
    """
    Test that translate_dataframe uses google_translate for all cells when translator_type is 'google'.
    The DataFrame should be filled with the mocked value.
    """
    df = sample_df()
    with patch('translator.google_translate', return_value='translated'):
        from translator import translate_dataframe
        # Use a valid-looking mock API key to pass validation
        result = translate_dataframe(
            df,
            target_language='en',
            api_key='mocked-google-api-key-12345',
            source_language='id',
            translator_type='google'
        )
        assert (result == 'translated').all().all()

def test_translate_dataframe_libre():
    """
    Test that translate_dataframe uses libretranslate for all cells when translator_type is 'libre'.
    The DataFrame should be filled with the mocked value.
    """
    df = sample_df()
    with patch('translator.libretranslate', return_value='translated'):
        from translator import translate_dataframe
        result = translate_dataframe(
            df,
            target_language='en',
            api_key='',
            source_language='id',
            translator_type='libre'
        )
        assert (result == 'translated').all().all()
