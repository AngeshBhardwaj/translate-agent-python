
import requests
import logging
import os
import datetime
from config import SOURCE_LANGUAGE, TARGET_LANGUAGE, API_KEY

# Configure logging to a new file for each run in the log directory
log_dir = os.path.join(os.path.dirname(__file__), 'log')
os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(log_dir, f"translate_agent_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def google_translate(text, target_language=TARGET_LANGUAGE, source_language=SOURCE_LANGUAGE, api_key=API_KEY):
    url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}"
    payload = {
        "q": text,
        "source": source_language,
        "target": target_language,
        "format": "text"
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["translations"][0]["translatedText"]
        else:
            logging.error(f"Google Translate API error: status={response.status_code}, text={response.text}")
            return text
    except Exception as e:
        logging.exception(f"Exception in google_translate for text: {text}")
        return text

def libretranslate(text, target_language=TARGET_LANGUAGE, source_language=SOURCE_LANGUAGE):
    url = "https://libretranslate.com/translate"
    payload = {
        "q": text,
        "source": source_language,
        "target": target_language,
        "format": "text"
    }
    # Optionally add API key if present in config and not empty
    from config import API_KEY
    if API_KEY and API_KEY != 'YOUR_API_KEY':
        payload["api_key"] = API_KEY
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            try:
                data = response.json()
                return data.get("translatedText", text)
            except Exception as e:
                logging.exception(f"LibreTranslate JSON decode error for text: {text} | Raw response: {response.text}")
                return text
        else:
            logging.error(f"LibreTranslate API error: status={response.status_code}, text={response.text}")
            return text
    except Exception as e:
        logging.exception(f"Exception in libretranslate for text: {text}")
        return text

def translate_dataframe(df, target_language=TARGET_LANGUAGE, api_key=API_KEY, source_language=SOURCE_LANGUAGE, translator_type=None):
    if translator_type is None:
        from config import TRANSLATOR
        translator_type = TRANSLATOR
    translated_df = df.copy()
    if translator_type.lower() == 'libre':
        for col in translated_df.columns:
            translated_df[col] = translated_df[col].astype(str).apply(
                lambda x: libretranslate(x, target_language, source_language=source_language) if x.strip() else x
            )
    else:
        # Validate API key
        if not api_key or api_key == 'YOUR_API_KEY' or not isinstance(api_key, str) or len(api_key.strip()) < 10:
            raise ValueError("A valid Google API key must be provided in config.py to use the Google translator.")
        for col in translated_df.columns:
            translated_df[col] = translated_df[col].astype(str).apply(
                lambda x: google_translate(x, target_language, source_language=source_language, api_key=api_key) if x.strip() else x
            )
    return translated_df
