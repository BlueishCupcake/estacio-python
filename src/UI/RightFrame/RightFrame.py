import customtkinter

mocked_table_data = [
    ["ID", "Name", "Age"],
    [1, "Alice", 24],
    [2, "Bob", 30],
    [3, "Charlie", 22],
    [4, "Charlie", 22],
    [5, "Charlie", 22],
]

class RightFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        
        total_columns = len(mocked_table_data[0])
        for col in range(total_columns):
            self.grid_columnconfigure(col, weight=1)

        for row_index, row_data in enumerate(mocked_table_data):
            for col_index, item in enumerate(row_data):
                cell = customtkinter.CTkLabel(self, font=("Arial", 16, "bold"), text=item, padx=10, pady=5, anchor="center")
                cell.grid(row=row_index, column=col_index, padx=10, pady=5, sticky="nsew")
