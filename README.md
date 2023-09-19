# Plugin for using googletrans with ocr_translate

This is a plugin for the [ocr_translate](https://github.com/Crivella/ocr_translate) server for implementing translations using google_translate

## Usage

- Install this by running `pip install ocr_translate-google`
- Add `ocr_translate_google` to your `INSTALLED_APPS` in `settings.py`
- Add the following to your `ocr_translate/ocr_tsl/models.json` and run the server with `AUTOCREATE_VALIDATED_MODELS` once:

    {
        "name": "google_translate",
        "lang_src": ["it", "ja", "ko", "en"],
        "lang_dst": ["it", "ja", "ko", "en"],
        "lang_code": "iso1",
        "entrypoint": "google_translate.online"
    }