
from typing import Literal

import customtkinter

def error_message(error_type: Literal["wrong_option", "default"]):

    if error_type == 'wrong_option':
        print('Erro! Favor selecionar uma opção válida')
    else:
        print('Ops! Algo deu errado. Contate o suporte!')

def main_options():
    user_input = input('Escolha uma opção abaixo:')

    try:
        if int(user_input) == 1:
            print("Case 1")
        elif int(user_input) == 2:
            return "Case 2"
        elif int(user_input) == 3:
            return "Case 3"
        else:
            error_message("wrong_option")
            main_options()
    except ValueError:
        error_message("wrong_option")
        main_options()

def welcome_message():
    print('\n****************************')
    print('Bem vindo. Maschka estoque!')
    print('**************************** \n')
    main_options()


def button_callback():
    welcome_message()

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)
app.mainloop()
