# jdb-translator

---

## Version 1.0.0

Created and uploaded May 2023.

---

## Description

A simple tkinter GUI translation application.

Translates from 29 source languages into 31 target languages.

Enter source text in first text widget and select source language. Select target language, click "Translate" and the
translation appears in the second text widget.

POSTs a query to DeepL's Translator API and returns the resulting translation.

DeepL's translations are considered to be precise, reliable and consistent. The quality may vary depending on the
language pair and the complexity of the text being translated.


---

## Instructions for Installation and Use

- Copy all the project files into one folder and run JDBTranslator.exe. 
- Python does not need to be installed to run this application.
- You need at least a free DeepL API account to make use of the translation functionality in this application.
- Go to [DeepL](https://www.deepl.com/pro-checkout/account?productId=1200&yearly=false&trial=false) and sign up for their free tier.
- Create an auth key for the DeepL API and either assign that directly to the 'deepl_auth_key' variable in the file 'deepl_translation.py' or create an environmental variable and assign the key there.
- Assign that auth key to the 'auth_key' variable in 'deepl_translation.py'.
- For higher security create an 'DEEPL_AUTH_KEY' environment variable on your system and assign your DeepL API auth key to that.

I'm not affiliated in any way with DeepL. It was the easiest functioning service I could find. Future versions of this
application will include functionality for other translator APIs/services.

---

### Credits

- [Flag icon](https://commons.wikimedia.org/wiki/File:Flag_of_France.svg) from Wikimedia Commons.

---

Thank you for your attention.

Andrew

---
