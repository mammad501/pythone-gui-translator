import tkinter as tk
from googletrans import Translator

def translate_text():
    translator = Translator()
    source_text = input_text.get("1.0", tk.END).strip()
    if not source_text:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "لطفاً متن وارد کنید.")
        return

    try:
        if lang_choice.get() == 1:
            source_lang = 'fa'
            dest_lang = 'en'
        else:
            source_lang = 'en'
            dest_lang = 'fa'

        translation = translator.translate(source_text, src=source_lang, dest=dest_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translation.text)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"خطا در ترجمه: {e}")

def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


root = tk.Tk()
root.title("مترجم")
root.geometry("500x400")


lang_choice = tk.IntVar(value=1)
tk.Label(root, text="انتخاب زبان:", font=("Arial", 12)).pack(pady=5)
tk.Radiobutton(root, text="فارسی به انگلیسی", variable=lang_choice, value=1, font=("Arial", 10)).pack()
tk.Radiobutton(root, text="انگلیسی به فارسی", variable=lang_choice, value=2, font=("Arial", 10)).pack()


input_label = tk.Label(root, text="متن ورودی:", font=("Arial", 12))
input_label.pack(pady=5)
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=5)


translate_button = tk.Button(root, text="ترجمه", command=translate_text, font=("Arial", 12))
translate_button.pack(pady=10)


output_label = tk.Label(root, text="ترجمه:", font=("Arial", 12))
output_label.pack(pady=5)
output_text = tk.Text(root, height=5, width=50, state="normal")
output_text.pack(pady=5)


clear_button = tk.Button(root, text="پاک کردن", command=clear_text, font=("Arial", 12))
clear_button.pack(pady=10)


root.mainloop()
