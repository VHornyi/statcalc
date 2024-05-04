Statystyczny Kalkulator

Autor: [Vadym Hornyi]

Opis:
Program to prosty kalkulator statystyczny napisany w języku Python przy użyciu biblioteki Tkinter. Kalkulator umożliwia obliczenia statystyczne, takie jak średnia arytmetyczna, średnia geometryczna, mediana, moda, współczynnik korelacji, współczynnik regresji liniowej, odchylenie standardowe oraz wartości MIN i MAX dla wprowadzonych danych liczbowych.

Struktura Kodu:
- Klasa Statystyka zawiera metody do obliczeń statystycznych, takich jak średnia arytmetyczna, średnia geometryczna, moda, mediana, współczynnik korelacji, współczynnik regresji liniowej, odchylenie standardowe, MIN i MAX.
- Klasa CalculatorApp odpowiada za interfejs użytkownika przy użyciu biblioteki Tkinter. Umożliwia wprowadzanie danych i wybieranie operacji statystycznych.

Użycie:
1. Uruchomienie programu inicjalizuje interfejs użytkownika kalkulatora.
2. Wprowadź dane liczbowe do pól tekstowych.
3. Wybierz operację statystyczną, której chcesz dokonać, klikając na odpowiedni przycisk.
4. Odpowiedź lub wynik operacji zostanie wyświetlony na etykiecie wynikowej.

Uwagi:
- W przypadku błędnych danych wejściowych program zwróci odpowiedni komunikat błędu.
- Kalkulator obsługuje również przypadki, w których wprowadzone dane są liczby rzeczywiste, oddzielone spacją.

Kluczowe Funkcje:
- Średnia arytmetyczna: Oblicza średnią arytmetyczną wprowadzonych liczb.
- Średnia geometryczna: Oblicza średnią geometryczną wprowadzonych liczb, uwzględniając różne zestawy danych.
- Moda: Znajduje wartość, która występuje najczęściej w danych.
- Mediana: Oblicza medianę danych, czyli wartość środkową w posortowanym ciągu.
- Współczynnik Korelacji: Wylicza współczynnik korelacji między dwoma zestawami danych.
- Regresja Liniowa: Oblicza współczynniki regresji liniowej dla dwóch zestawów danych.
- Odchylenie Standardowe: Mierzy rozproszenie danych wokół średniej arytmetycznej.
- MIN i MAX: Znajduje najmniejszą i największą wartość w zestawie danych.

Interfejs Użytkownika:
- Pole tekstowe 1: Wprowadź dane liczbowe dla pierwszego zestawu.
- Pole tekstowe 2: Wprowadź dane liczbowe dla drugiego zestawu (jeśli wymagane).
- Przyciski cyfr: Wprowadzają cyfry do aktualnie aktywnego pola tekstowego.
- Przyciski operacji statystycznych: Wybierz operację do wykonania na danych.
- Przycisk "Space": Dodaje spację do aktualnie aktywnego pola tekstowego.
- Przycisk "Clear": Wyczyści pola wprowadzania danych.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Statistical Calculator

Author: [Vadym Hornyi]

Description:
Statistical Calculator is a simple statistical calculator program written in Python using the Tkinter library. The calculator allows for statistical calculations such as arithmetic mean, geometric mean, median, mode, correlation coefficient, linear regression coefficient, standard deviation, and MIN and MAX values for input numerical data.

Code Structure:
- The Statistics class contains methods for statistical calculations such as arithmetic mean, geometric mean, mode, median, correlation coefficient, linear regression coefficient, standard deviation, MIN, and MAX.
- The CalculatorApp class is responsible for the user interface using the Tkinter library. It allows for data input and selection of statistical operations.

Usage:
1. Running the program initializes the calculator user interface.
2. Enter numerical data into the text fields.
3. Select the statistical operation you want to perform by clicking on the corresponding button.
4. The response or result of the operation will be displayed on the result label.

Notes:
- In case of incorrect input data, the program will return an appropriate error message.
- The calculator also handles cases where the input data is real numbers separated by spaces.

Key Features:
- Arithmetic Mean: Calculates the arithmetic mean of the entered numbers.
- Geometric Mean: Calculates the geometric mean of the entered numbers, considering different data sets.
- Mode: Finds the value that occurs most frequently in the data.
- Median: Calculates the median of the data, the middle value in a sorted sequence.
- Correlation Coefficient: Computes the correlation coefficient between two sets of data.
- Linear Regression: Computes the linear regression coefficients for two sets of data.
- Standard Deviation: Measures the dispersion of data around the arithmetic mean.
- MIN and MAX: Finds the smallest and largest values in the data set.

User Interface:
- Text Field 1: Enter numerical data for the first data set.
- Text Field 2: Enter numerical data for the second data set (if required).
- Numeric Buttons: Input digits into the currently active text field.
- Statistical Operation Buttons: Select an operation to perform on the data.
- "Space" Button: Adds a space to the currently active text field.
- "Clear" Button: Clears the data input fields.
