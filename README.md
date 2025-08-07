# Translate Agent

A Python tool to batch-translate Excel files using either Google Translate API or LibreTranslate API. It reads all sheets from an input Excel file, translates the content, and writes the translated sheets to a new Excel file.

## Features

- Supports both Google Translate and LibreTranslate APIs
- Translates all sheets in an Excel file
- Output file is auto-named based on input and target language
- Logging of errors and exceptions to a timestamped log file in the `log/` directory

## Requirements

- Python 3.8+
- API key for Google Translate (required for Google)
- (Optional) API key for LibreTranslate (recommended for production use)

## Setup

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure the project**:
   - Edit `config.py`:
     - Set `INPUT_FILE` to your Excel file path (e.g., `input/YourFile.xlsx`)
     - Set `TARGET_LANGUAGE` (e.g., `'en'` for English)
     - Set `SOURCE_LANGUAGE` (e.g., `'id'` for Indonesian)
     - Set `TRANSLATOR` to `'google'` or `'libre'`
     - Set `API_KEY` for the selected API (see below)

## API Keys

- **Google Translate**: Get an API key from [Google Cloud Console](https://console.cloud.google.com/). Enable the Cloud Translation API.
- **LibreTranslate**: Get a free API key from [LibreTranslate Portal](https://portal.libretranslate.com/). Some public endpoints may not require a key, but it's recommended.

## Usage

Run the main script:

```bash
python main.py
```

- The script will print the selected translator and progress.
- The translated file will be saved in the `output/` directory as `translated_<TARGET_LANGUAGE>_<INPUT_FILE>`.
- Logs are saved in the `log/` directory with a timestamped filename.

## Switching Between APIs

- In `config.py`, set `TRANSLATOR = 'google'` to use Google Translate, or `TRANSLATOR = 'libre'` to use LibreTranslate.
- Provide the correct `API_KEY` for the selected service.

## Notes

- For large files, be aware of API rate limits (especially for LibreTranslate public endpoints).
- All logs and errors are saved in the `log/` directory for troubleshooting.

## License

MIT License
