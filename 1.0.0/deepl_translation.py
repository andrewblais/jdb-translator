import os
import requests

auth_key = os.environ.get("DEEPL_AUTH_KEY")


class DeeplTranslate:

    def __init__(self, source_text, source_lang, target_lang):
        self.translation = ""
        self.source_text = source_text
        self.source_lang = source_lang
        self.target_lang = target_lang

        self.get_translation()

    def get_translation(self):
        url = "https://api-free.deepl.com/v2/translate"
        headers = {
            "Authorization": f"DeepL-Auth-Key {auth_key}",
            "User-Agent": "jdbtranslator anb2015@gmail.com",
        }
        data = {
            "text": self.source_text,
            "source_lang": self.source_lang,
            "target_lang": self.target_lang
        }
        try:
            response = requests.post(url=url, headers=headers, data=data)
            response.raise_for_status()

            deepl_data = response.json()
            self.translation = deepl_data["translations"][0].get("text")

        except requests.exceptions.HTTPError as http_error:
            print(f"An HTTP error occurred: {http_error}.")
        except requests.exceptions.RequestException as request_exception:
            print(f"A request error occurred: {request_exception}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}.")


if __name__ == "__main__":
    user_text = "Good afternoon"

    translation = DeeplTranslate(user_text, "EN", "FR").translation

    if translation:
        print(translation)
    else:
        print("Something went wrong.")
