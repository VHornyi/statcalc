import tkinter as tk
from tkinter import ttk
# Ta klasa zawiera statyczne metody do obliczania różnych wskaźników statystycznych
class Statystyka:
    # Oblicza średnią arytmetyczną z listy liczb przedstawionych jako ciąg znaków.
    def calculate_ar_average(numbers_str):
        try:
            numbers_list = [float(num) for num in numbers_str.split()]
            if numbers_list:
                average = sum(numbers_list) / len(numbers_list)
                return f"średnia arytmetyczna: {average:.2f}"
            else:
                return "Błąd, wpisz coś."
        except ValueError:
            return "Błąd!!!"

    # Oblicza średnią geometryczną z dwóch list liczb przedstawionych jako ciągi znaków.
    def calculate_geom_average(numbers_str1, numbers_str2):
        try:
            numbers_list1 = [float(num) for num in numbers_str1.split()]
            numbers_list2 = [float(num) for num in numbers_str2.split()]
            numbers_list1.extend(numbers_list2)

            if numbers_list1:
                geometric_mean = 1
                for num in numbers_list1:
                    geometric_mean *= num

                if geometric_mean <= 0:
                    return "Nie można obliczyć dla ujemnych lub zerowych wartości."
                else:
                    geometric_mean = geometric_mean ** (1 / len(numbers_list1))
                    return f"średnia geometryczna: {geometric_mean:.2f}"
            else:
                return "Błąd, wpisz coś."
        except ValueError:
            return "Błąd!!!"

    # Oblicza modę z listy liczb przedstawionej jako ciąg znaków.
    def calculate_moda(numbers_str):
        try:
            numbers_list = [float(num) for num in numbers_str.split()]
            if numbers_list:
                mode_result = Statystyka.find_mode(numbers_list)
                return f"moda: {mode_result}"
            else:
                return "Wpisz coś."
        except ValueError:
            return "Błąd"

    # Metoda pomocnicza do znajdowania mody na liście liczb.
    def find_mode(numbers_list):
        frequency_dict = {}
        for num in numbers_list:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        mode_result = max(frequency_dict, key=frequency_dict.get)
        return mode_result

    # Oblicza medianę z listy liczb przedstawionej jako ciąg znaków.
    def calculate_mediana(numbers_str):
        try:
            numbers_list = [float(num) for num in numbers_str.split()]
            if numbers_list:
                numbers_list.sort()
                n = len(numbers_list)

                if n % 2 == 0:
                    median_result = (numbers_list[n // 2 - 1] + numbers_list[n // 2]) / 2
                else:
                    median_result = numbers_list[n // 2]

                return f"mediana: {median_result}"
            else:
                return "Wpisz coś"
        except ValueError:
            return "Błąd!!!"

    # Oblicza współczynnik korelacji między dwoma listami liczb przedstawionymi jako ciągi znaków.
    def calculate_correlation(numbers_str1, numbers_str2):
        try:
            numbers_list1 = [float(num) for num in numbers_str1.split()]
            numbers_list2 = [float(num) for num in numbers_str2.split()]

            if numbers_list1 and numbers_list2 and len(numbers_list1) == len(numbers_list2):
                correlation_result = Statystyka.calculate_correlation_coefficient(numbers_list1, numbers_list2)
                return f"współczynnik korelacji: {correlation_result:.2f}"
            else:
                return "Wpisz tę samą liczbę wartości"
        except ValueError:
            return "Błąd!!!"

    # Metoda pomocnicza do obliczania współczynnika korelacji.
    def calculate_correlation_coefficient(list1, list2):
        n = len(list1)
        mean_list1 = sum(list1) / n
        mean_list2 = sum(list2) / n

        numerator = sum((x - mean_list1) * (y - mean_list2) for x, y in zip(list1, list2))
        denominator1 = sum((x - mean_list1) ** 2 for x in list1)
        denominator2 = sum((y - mean_list2) ** 2 for y in list2)

        if denominator1 != 0 and denominator2 != 0:
            correlation_coefficient = numerator / (denominator1 ** 0.5 * denominator2 ** 0.5)
            return correlation_coefficient
        else:
            return 0

    # Oblicza parametry regresji liniowej dla dwóch list liczb `x_values` i `y_values`.
    def calculate_linear_regression(x_values, y_values):
        try:
            if len(x_values) == 0 or len(y_values) == 0:
                return "Błąd, brak wartości x lub y."
            elif len(x_values) != len(y_values):
                return "Błąd, różna liczba wartości x i y."

            n = len(x_values)
            sum_x = sum(x_values)
            sum_y = sum(y_values)
            sum_xy = sum(x * y for x, y in zip(x_values, y_values))
            sum_x_squared = sum(x**2 for x in x_values)

            a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
            b = (sum_y - a * sum_x) / n

            return f"a = {a:.2f}, b = {b:.2f}"
        except ValueError:
            return "Błąd!!!"

    # Oblicza odchylenie standardowe z listy liczb przedstawionej jako ciąg znaków.
    def calculate_standard_deviation(numbers_str):
        try:
            numbers_list = [float(num) for num in numbers_str.split()]
            if numbers_list:
                mean_value = sum(numbers_list) / len(numbers_list)
                variance = sum((x - mean_value) ** 2 for x in numbers_list) / len(numbers_list)
                std_deviation = variance ** 0.5
                return f"Odchylenie standardowe: {std_deviation:.2f}"
            else:
                return "Błąd, wpisz coś."
        except ValueError:
            return "Błąd!!!"
    # Oblicza wartości minimalną i maksymalną z listy liczb przedstawionej jako ciąg znaków.
    def calculate_min_max(numbers_str):
        try:
            numbers_list = [float(num) for num in numbers_str]
            if numbers_list:
                min_value = min(numbers_list)
                max_value = max(numbers_list)
                return f"MIN: {min_value}, MAX: {max_value}"
            else:
                return "Błąd, wpisz coś."
        except ValueError:
            return "Błąd!!!"

# Ta klasa reprezentuje główną aplikację kalkulatora. Zawiera metody do tworzenia interfejsu użytkownika, obsługi zdarzeń oraz wywoływania metod klasy `Statystyka` do wykonania obliczeń.
class CalculatorApp:
    
    # Konstruktor klasy, tworzy interfejs użytkownika.
    def __init__(self, master):
        self.master = master
        master.geometry("900x500+100+50")
        master['bg'] = '#f2f2f2'
        master.title("Statystyczny kalkulator")
        master.minsize(900, 500)

        photo = tk.PhotoImage(file='stat.png')
        master.iconphoto(False, photo)

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 13))
        self.style.configure('TEntry', font=('Arial', 30))
        self.style.configure('TLabel', font=('Arial', 18))

        self.calc_entry = ttk.Entry(master, justify=tk.RIGHT, font=('Arial', 30), style='TEntry')
        self.calc_entry.insert(0, '0')
        self.calc_entry.grid(row=0, column=0, columnspan=5, sticky='we', pady=10)

        self.calc2_entry = ttk.Entry(master, justify=tk.RIGHT, font=('Arial', 30), style='TEntry')
        self.calc2_entry.insert(0, '0')
        self.calc2_entry.grid(row=1, column=0, columnspan=5, sticky='we', pady=10)

        self.result_label = ttk.Label(master, text="Odpowiedź: ", justify=tk.RIGHT, style='TLabel')
        self.result_label.grid(row=6, column=1, sticky='we', columnspan=4, pady=10)
        self.create_buttons()
        self.configure_grid()

    # Tworzy przyciski w interfejsie użytkownika.
    def create_buttons(self):
        button_positions = [
            ('1', 2, 0),
            ('2', 2, 1), 
            ('3', 2, 2),
            ('4', 3, 0), 
            ('5', 3, 1), 
            ('6', 3, 2),
            ('7', 4, 0), 
            ('8', 4, 1), 
            ('9', 4, 2),
            ('0', 5, 1),
            (' ', 5, 2),
            ('CLEAR', 5, 0),
            ('średnia arytmetyczna', 2, 3),
            ('średnia geometryczna', 3, 3),
            ('mediana', 4, 3),
            ('moda', 2, 4),
            ('współczynnik korelacji', 3, 4),
            ('współczynnik regresji liniowej', 4, 4),
            ('odchylenie standardowe', 5, 4),
            ('MIN MAX', 5,3),
        ]

        for button_text, row, col in button_positions:
            if 'arytmetyczna' in button_text:
                button = self.make_srednia_ar_operation_button(button_text)
            elif 'geometryczna' in button_text:
                button = self.make_srednia_geom_operation_button(button_text)
            elif 'moda' in button_text:
                button = self.make_moda_operation_button(button_text)
            elif 'mediana' in button_text:
                button = self.make_mediana_operation_button(button_text)
            elif 'korelacji' in button_text:
                button = self.make_korelacja_operation_button(button_text)
            elif 'liniowej' in button_text:
                button = self.make_regresja_liniowa_operation_button(button_text)
            elif 'standardowe' in button_text:
                button = self.make_std_deviation_operation_button(button_text)
            elif 'MIN MAX' in button_text:
                button = self.make_min_max_operation_button(button_text)
            elif 'CLEAR' in button_text:
                button = self.make_clear_button(button_text)
            elif ' ' in button_text:
                button = self.make_space_button()
            else:
                button = self.make_digit_button(button_text)

            button.grid(row=row, column=col, sticky='wens', padx=2, pady=2)
    
    # Tworzy przycisk "CLEAR" do czyszczenia pól wprowadzania.
    def make_clear_button(self, text):
        return ttk.Button(text=text, style='TButton', command=self.clear_entries)
    
    # Tworzy przycisk do dodawania spacji
    def make_space_button(self):
        return ttk.Button(text='Space', style='TButton', command=lambda: self.add_space())

    # Tworzy przycisk do wprowadzania cyfry.
    def make_digit_button(self, digit):
        button = ttk.Button(text=digit, style='TButton', command=lambda: self.add_digit(digit))
        button.configure(style='TButton')
        return button

    # Tworzy przycisk do wykonania średniej arytmetycznej.
    def make_srednia_ar_operation_button(self, operation):
        return ttk.Button(text=operation, style='TButton', command=self.calculate_ar_average)

    # Tworzy przycisk do wykonania średniej geometrycznej.
    def make_srednia_geom_operation_button(self, operation):
        operation = operation.strip()
        return ttk.Button(text=operation, style='TButton', command=self.calculate_geom_average)

    # Tworzy przycisk do wykonania obliczenia mody.
    def make_moda_operation_button(self, operation):
        return ttk.Button(text=operation, style='TButton', command=self.calculate_moda)

    # Tworzy przycisk do wykonania obliczenia mediany.
    def make_mediana_operation_button(self, operation):
        return ttk.Button(text=operation, style='TButton', command=self.calculate_mediana)

    # Tworzy przycisk do wykonania obliczenia korelacji.
    def make_korelacja_operation_button(self, operation):
        return ttk.Button(text=operation, style='TButton', command=self.calculate_correlation)

    # Tworzy przycisk do wykonania regresji liniowej.
    def make_regresja_liniowa_operation_button(self, operation):
        return ttk.Button(text=operation, style='TButton', command=self.calculate_linear_regression)

    # Tworzy przycisk do wykonania obliczenia odchylenia standardowego.
    def make_std_deviation_operation_button(self, operation):
        return ttk.Button(text=operation, style='TButton', command=self.calculate_standard_deviation)
    
    # Tworzy przycisk do wykonania obliczenia minimum i maksimum.
    def make_min_max_operation_button(self, operation):
        return ttk.Button(text=operation, style='TButton', command=self.calculate_min_max)

    # Dodaje spację do aktywnego pola wprowadzania. (Niestety cyfry i spacje z add_space i add_digit dodawane są tylko do calc_entry, dla calc2_entry to nie działa)
    def add_space(self):
        active_entry = self.master.focus_get()

        if active_entry == self.calc_entry:
            entry = self.calc_entry
        elif active_entry == self.calc2_entry:
            entry = self.calc2_entry
        else:
            entry = self.calc_entry

        value = entry.get() + ' '
        entry.delete(0, tk.END)
        entry.insert(0, value)

    # Konfiguruje siatkę interfejsu.
    def configure_grid(self):
        for col in range(6):
            self.master.grid_columnconfigure(col, minsize=120, weight=1)
        for row in range(7):
            self.master.grid_rowconfigure(row, minsize=70, weight=1)

    # Dodaje cyfrę do aktywnego pola wprowadzania. 
    def add_digit(self, digit):
        active_entry = self.master.focus_get()

        if active_entry == self.calc_entry:
            entry = self.calc_entry
        elif active_entry == self.calc2_entry:
            entry = self.calc2_entry
        else:
            entry = self.calc_entry

        value = entry.get() + str(digit)
        if value[0] == '0':
            value = value[1:]
        entry.delete(0, tk.END)
        entry.insert(0, value)

    # Dodaje operację do aktywnego pola wprowadzania.
    def add_operation(self, operation):
        active_entry = self.master.focus_get()

        if active_entry == self.calc_entry:
            entry = self.calc_entry
        elif active_entry == self.calc2_entry:
            entry = self.calc2_entry
        else:
            entry = self.calc_entry

        value = entry.get()
        last_word = value.split()[-1].strip()

        if last_word in ('średnia', 'geometryczna', 'mediana', 'moda', 'korelacji', 'regresji'):
            value = ' '.join(value.split()[:-1])

        entry.delete(0, tk.END)
        entry.insert(0, value + ' ' + operation)
    
    # Czyści pola wprowadzania i ustawia ich wartości domyślne na zero.
    def clear_entries(self):
        self.calc_entry.delete(0, tk.END)
        self.calc2_entry.delete(0, tk.END)
        self.calc_entry.insert(0, '0')
        self.calc2_entry.insert(0, '0')

    # Wywołuje metodę obliczania średniej arytmetycznej.
    def calculate_ar_average(self):
        result = Statystyka.calculate_ar_average(self.calc_entry.get() + ' ' + self.calc2_entry.get())
        self.result_label.config(text=result)
    
    # Wywołuje metodę obliczania średniej geometrycznej.
    def calculate_geom_average(self):
        result = Statystyka.calculate_geom_average(self.calc_entry.get(), self.calc2_entry.get())
        self.result_label.config(text=result)

    # Wywołuje metodę obliczania mody.
    def calculate_moda(self):
        result = Statystyka.calculate_moda(self.calc_entry.get())
        self.result_label.config(text=result)

    # Wywołuje metodę obliczania mediany.
    def calculate_mediana(self):
        result = Statystyka.calculate_mediana(self.calc_entry.get())
        self.result_label.config(text=result)

    # Wywołuje metodę obliczania korelacji.
    def calculate_correlation(self):
        result = Statystyka.calculate_correlation(self.calc_entry.get(), self.calc2_entry.get())
        self.result_label.config(text=result)

    # Wywołuje metodę obliczania regresji liniowej.
    def calculate_linear_regression(self):
        x_values = [float(num) for num in self.calc_entry.get().split()]
        y_values = [float(num) for num in self.calc2_entry.get().split()]
        result = Statystyka.calculate_linear_regression(x_values, y_values)
        self.result_label.config(text=result)

    # Wywołuje metodę obliczania odchylenia standardowego.
    def calculate_standard_deviation(self):
        result = Statystyka.calculate_standard_deviation(self.calc_entry.get() + ' ' + self.calc2_entry.get())
        self.result_label.config(text=result)

    # Wywołuje metodę obliczania minimum i maksimum.
    def calculate_min_max(self):
        result = Statystyka.calculate_min_max(self.calc_entry.get().split())
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
