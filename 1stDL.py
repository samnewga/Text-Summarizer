import tkinter as tk
from tkinter import *

from tkinter import ttk
from tkinter.scrolledtext import *
from SummerTime import SummerTime

window = tk.Tk()

window.title("Textatron")

window.geometry('700x900')

window.config(background='black')

style = ttk.Style(window)

style.configure('lefttab.TNotebook', tabposition='wn')

tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

tab_main = ttk.Frame(tab_control)

tab_control.add(tab_main, text='Mission Control')

label_summarize = Label(tab_main, text="\nHi, I am Textatrpm. Let me read and then Summarize the text. Then you may review and edit.\n", padx=5, pady=5)

label_summarize.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')

def erase_input():
    entry.delete('1.0', END)

def erase_output():
    output_display.delete('1.0', END)

def summer_time():
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    text_format = entry.get('1.0', tk.END)
    parser_config = PlaintextParser.from_string(text_format, Tokenizer('english'))
    summerTime = SummerTime()
    summer_all = summerTime.lex_rank_analysis(parser_config, 2)
    summer_all = summer_all + summerTime.luhn_analysis(parser_config, 2)
    summer_all = summer_all + summerTime.lsa_analysis(parser_config, 2)
    scrubbed = []
    for sentence in summer_all:
        concat = str(sentence) + "\n\n\n"
        concat.replace("", "{")
        concat.replace("", "}")
        scrubbed.append(concat)
    output_display.insert(tk.END, scrubbed)
    print("\nAbout to print summer all results\n")
    print(summer_all)

label_text_to_summarize = Label(tab_main, text='Enter Text to Summarize', padx=5, pady=5)
label_text_to_summarize.grid(row=1, column=0)
entry = ScrolledText(tab_main, height=30)
entry.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

button_run = Button(tab_main, text='Invoke Tex-A-Tron', command=summer_time, width=22, bg='#25d366', fg='#fff')
button_run.grid(row=4, column=0, padx=10, pady=10)

output_display = ScrolledText(tab_main)
output_display.grid(row=9, column=0, columnspan=5, padx=5, pady=5)

window.mainloop()


