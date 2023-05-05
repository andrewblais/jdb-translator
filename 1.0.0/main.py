from tkinter import *
from tkinter import ttk, messagebox
from deepl_info import *
from deepl_translation import DeeplTranslate


def translate_text():
    try:
        for key, value in source_lang_dict.items():
            if value == source_combo.get():
                source_lang_key = key

        for key, value in target_lang_dict.items():
            if value == target_combo.get():
                target_lang_key = key

        # Turn source_text text into DeeplTranslate object
        to_translate = DeeplTranslate((source_text.get(1.0, END)), source_lang_key, target_lang_key)

        # Translate text
        translated_text = to_translate.translation

        # Output text
        target_text.delete(1.0, END)
        target_text.insert(1.0, translated_text)

    except Exception as e:
        messagebox.showerror("Translation Error", e)


def clear():
    """Clear the source and target language text boxes"""
    source_text.delete(1.0, END)
    target_text.delete(1.0, END)


def copy_translation(text_widget):
    # Clear the clipboard
    text_widget.clipboard_clear()

    # Get text from widget
    copied_text = text_widget.get(1.0, END)

    # Post to clipboard
    text_widget.clipboard_append(copied_text)


def display_context_menu(event):
    global current_text_widget
    current_text_widget = event.widget
    context_menu_text.tk_popup(event.x_root, event.y_root)


def cut(text_widget, event=None):
    text_widget.event_generate("<<Cut>>")
    return "break"


def copy(text_widget, event=None):
    text_widget.event_generate("<<Copy>>")
    return "break"


def paste(text_widget, event=None):
    text_widget.event_generate("<<Paste>>")
    return "break"


def select_all(text_widget, event=None):
    text_widget.tag_all(SEL, "1.0", "end-1c")
    text_widget.mark_set(INSERT, "1.0")
    text_widget.see(INSERT)
    return "break"


def delete_selected(text_widget, event=None):
    text_widget.delete(SEL_FIRST, SEL_LAST)


def about_popup():
    info = "JDBTranslator v.1.0.0\n©2023, MIT License\nAndrew Blais\nhttps://github.com/andrewblais"
    messagebox.showinfo("About JDBTranslator", info)


# MAIN WINDOW
window = Tk()
window.title("JDBTranslator")
window.iconbitmap("france.ico")
window.geometry("560x680")
window.maxsize(560, 680)
window.minsize(560, 680)
window.config(padx=20, pady=15)

# SOURCE LABEL
source_info = "Input text to be translated:"
source_label = Label(window, text=source_info)
source_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")

# SOURCE TEXT BOX (ROW 1 - COLUMN 0)
source_text = Text(window, height=12, width=62, wrap="word")
source_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# SOURCE LANGUAGE MENU (ROW 1 - COLUMN 0)
source_combo = ttk.Combobox(window, width=19, values=source_lang_names)
source_combo.current(5)
source_combo.grid(row=2, column=0, padx=12, pady=0, sticky="w")

# TRANSLATE BUTTON (ROW 1 - COLUMN 0)
translate_button = Button(window, text=" Translate ", font=("Helvetica", 10), command=translate_text)
translate_button.grid(row=3, column=1, padx=0, pady=10)

# RESET BUTTON (ROW 1 - COLUMN 0)
reset_button = Button(window, text="   Reset   ", font=("Helvetica", 10), command=clear)
reset_button.grid(row=4, column=1, padx=0, pady=10)

# TARGET LABEL
target_info = "View translation:"
target_label = Label(window, text=target_info)
target_label.grid(row=5, column=0, padx=10, pady=0, sticky="w")

# DESTINATION LANGUAGE MENU (ROW 1 - COLUMN 0)
target_combo = ttk.Combobox(window, width=19, values=target_lang_names)
target_combo.current(9)
target_combo.grid(row=5, column=2, padx=12, pady=0, sticky="e")

# DESTINATION TEXT BOX (ROW 1 - COLUMN 0)
target_text = Text(window, height=12, width=62)
target_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# COPY BUTTON
translate_button = Button(window, text=" Copy Translation ", font=("Helvetica", 10), command=lambda: copy_translation(target_text))
translate_button.grid(row=7, column=1, padx=0, pady=10)

# ABOUT BUTTON
about_button = Button(window, text=" About ", font=("Helvetica", 10), command=about_popup)
about_button.grid(row=7, column=2,  padx=12, pady=10, sticky="e")

# CREATE CONTEXT MENU
context_menu_text = Menu(window, tearoff=0)
context_menu_text.add_command(label="Cut", command=lambda: cut(current_text_widget))
context_menu_text.add_command(label="Copy", command=lambda: copy(current_text_widget))
context_menu_text.add_command(label="Paste", command=lambda: paste(current_text_widget))
context_menu_text.add_separator()
context_menu_text.add_command(label="Delete", command=lambda: delete_selected(current_text_widget))
context_menu_text.add_separator()
context_menu_text.add_command(label="Select All", command=lambda: select_all(current_text_widget))

# BIND RIGHT-CLICK TO display_context_menu()
source_text.bind("<Button-3>", display_context_menu)
target_text.bind("<Button-3>", display_context_menu)

print(window.bind_class("Listbox"))

window.mainloop()
