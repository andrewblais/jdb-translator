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

You may run this application in two ways:

1. Ignore JDBTranslator.exe and the 'venv' directory. Simply include the files:
    - deepl_info.py
    - deepl_translation.py
    - france.ico
    - main.py
    - (README.md)
      in a directory called 'JDBTranslator' (or whatever) and place that directory wherever you find most advantageous.
      You will need to run this application through Python, either with an IDE or by assigning a default IDE such as
      IDLE to automatically open and run the GUI interface. Just double-click on 'main.py' and you're off and away.


2. Create a directory called 'JDBTranslator' (or something germane), extract/paste all of the files from Step 1 there,
   and additionally include:
    - the 'venv' directory
    - 'JDBTranslator.exe'
    - Now you can run the application on a machine without Python installed.


3. You need at least a free DeepL API account to make use of the translation functionality in this
   application.
    - Go to [DeepL](https://www.deepl.com/pro-checkout/account?productId=1200&yearly=false&trial=false) and
      sign up for their free tier.
    - Create an auth key for the DeepL API and either assign that directly to the 'deepl_auth_key' variable in the
      file 'deepl_translation.py' or create an environmental variable and assign the key there.

I'm not affiliated in any way with DeepL. It was the easiest functioning service I could find. Future versions of this
application will include functionality for other translator APIs/services.

---

### Credits

- [Flag icon](https://commons.wikimedia.org/wiki/File:Flag_of_France.svg) from Wikimedia Commons.

---

Thank you for your attention.

Andrew

---
