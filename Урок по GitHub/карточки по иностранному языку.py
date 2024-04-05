import customtkinter as ctk
from tkinter import messagebox, Toplevel, Listbox
import os

ctk.set_appearance_mode("System")  # По умолчанию используется системная тема
ctk.set_default_color_theme("blue")  # 'blue' (default), 'green', 'dark-blue'

class LanguageCardsApp(ctk.CTk):
    def __init__(self, cards_file="cards.txt"):
        super().__init__()

        self.title("Карточки для изучения языка")
        self.geometry("500x500")

        self.cards_file = cards_file
        self.cards = []
        self.load_cards()

        self.setup_ui()

    def setup_ui(self):
        self.term_label = ctk.CTkLabel(self, text="Термин:")
        self.term_label.pack(pady=10)

        self.term_entry = ctk.CTkEntry(self, width=200, placeholder_text="Введите иностранное слово")
        self.term_entry.pack()

        self.definition_label = ctk.CTkLabel(self, text="Определение:")
        self.definition_label.pack(pady=10)

        self.definition_entry = ctk.CTkEntry(self, width=200, placeholder_text="Введите определение или перевод")
        self.definition_entry.pack()

        # Используем только параметры width и height для изменения размера кнопок
        self.add_button = ctk.CTkButton(self, text="Добавить карточку", command=self.add_card, fg_color="#3073FB", width=200, height=40)
        self.add_button.pack(pady=20)

        self.review_button = ctk.CTkButton(self, text="Просмотреть карточки", command=self.review_cards, fg_color="#3073FB", width=200, height=40)
        self.review_button.pack(pady=10)

        self.edit_button = ctk.CTkButton(self, text="Редактировать карточки", command=self.edit_cards, fg_color="#2B2B2B", width=200, height=40)
        self.edit_button.pack(pady=20)
        
        self.theme_button = ctk.CTkButton(self, text="Сменить тему", command=self.toggle_theme, fg_color="#2B2B2B", width=200, height=40)
        self.theme_button.pack(pady=10)

    def toggle_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    def add_card(self):
        term = self.term_entry.get()
        definition = self.definition_entry.get()

        if term and definition:
            self.cards.append([term, definition])
            self.term_entry.delete(0, 'end')
            self.definition_entry.delete(0, 'end')
            messagebox.showinfo("Успех", "Карточка добавлена успешно!")
            self.save_cards()
        else:
            messagebox.showwarning("Внимание", "Заполните оба поля для добавления карточки.")

    def load_cards(self):
        if os.path.exists(self.cards_file):
            with open(self.cards_file, "r", encoding="utf-8") as f:
                for line in f:
                    term, definition = line.strip().split(' - ')
                    self.cards.append([term, definition])

    def save_cards(self):
        with open(self.cards_file, "w", encoding="utf-8") as f:
            for term, definition in self.cards:
                f.write(f"{term} - {definition}\n")

    def review_cards(self):
        if not self.cards:
            messagebox.showinfo("Информация", "Пока нет карточек для просмотра.")
            return

        self.is_term_shown = True
        self.review_window = Toplevel(self)
        self.review_window.title("Просмотр карточек")
        self.card_index = 0
        self.show_card(self.card_index)

    def show_card(self, index):
        for widget in self.review_window.winfo_children():
            widget.destroy()

        card_text = self.cards[index][0] if self.is_term_shown else self.cards[index][1]

        card_label = ctk.CTkLabel(self.review_window, text=card_text, wraplength=400)
        card_label.pack(pady=20)

        flip_button = ctk.CTkButton(self.review_window, text="Перевернуть", command=self.flip_card, fg_color="#3073FB", width=150, height=40)
        flip_button.pack(pady=10)

        navigation_frame = ctk.CTkFrame(self.review_window)
        navigation_frame.pack(pady=20)

        prev_button = ctk.CTkButton(navigation_frame, text="<< Предыдущая", command=lambda: self.navigate_card(-1), fg_color="#3073FB", width=150, height=40)
        prev_button.pack(side='left', padx=10)

        next_button = ctk.CTkButton(navigation_frame, text="Следующая >>", command=lambda: self.navigate_card(1), fg_color="#3073FB", width=150, height=40)
        next_button.pack(side='right', padx=10)

    def flip_card(self):
        self.is_term_shown = not self.is_term_shown
        self.show_card(self.card_index)

    def navigate_card(self, direction):
        self.card_index += direction
        self.card_index = max(0, min(self.card_index, len(self.cards) - 1))
        self.is_term_shown = True
        self.show_card(self.card_index)

    def edit_cards(self):
        edit_window = Toplevel(self)
        edit_window.title("Редактировать карточки")

        listbox = Listbox(edit_window)
        listbox.pack(padx=10, pady=10, fill="both", expand=True)

        for term, definition in self.cards:
            listbox.insert("end", f"{term} - {definition}")

        def delete_card():
            selection = listbox.curselection()
            if selection:
                del self.cards[selection[0]]
                listbox.delete(selection[0])
                self.save_cards()

        delete_button = ctk.CTkButton(edit_window, text="Удалить карточку", command=delete_card, fg_color="#3073FB", width=150, height=40)
        delete_button.pack(pady=10)

if __name__ == "__main__":
    app = LanguageCardsApp()
    app.mainloop()
