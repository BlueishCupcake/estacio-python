import psycopg2
import customtkinter
import os
from dotenv import load_dotenv

all_available_products = [["Produto", "Preço", "Quantidade"]]

def connect_db():

    connection = None
    cursor = None

    load_dotenv()

    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        
        cursor = connection.cursor()

        cursor.execute("SELECT nome, preco, quantidade FROM produto")

        products = cursor.fetchall()
        
        return products


    except Exception as error:
        print(f"Error connecting to database: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def display_products(self):
        global all_available_products

        get_all_products = connect_db()

        all_available_products.extend(get_all_products)


        total_columns = len(all_available_products[0])
        for col in range(total_columns):
           self.grid_columnconfigure(col, weight=1)

        for row_index, row_data in enumerate(all_available_products):
            for col_index, item in enumerate(row_data):
                cell = customtkinter.CTkLabel(self, font=("Arial", 16, "bold"), text=item, padx=10, pady=5, anchor="w")
                cell.grid(row=row_index, column=col_index, padx=10, pady=5, sticky="nsew")


class RightFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        
        display_products(self)

