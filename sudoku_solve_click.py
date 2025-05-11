import openpyxl
import pyautogui

def read_sudoku_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    sudoku = []
    for row in sheet.iter_rows(min_row=1, max_row=9, min_col=1, max_col=9):
        sudoku.append([cell.value if cell.value is not None else 0 for cell in row])

    return sudoku

def is_valid_move(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False

    return True

def solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(sudoku, row, col, num):
                        sudoku[row][col] = num
                        print(f"Set sudoku[{row}][{col}] = {num}")

                        if solve_sudoku(sudoku):
                            return True

                        sudoku[row][col] = 0
                        print(f"Backtrack: Reset sudoku[{row}][{col}] to 0")

                return False

    return True

def click_cell(row, col):
    # Calculate the cell's center coordinates
    cell_width = width_sudoku // 9
    cell_height = height_sudoku // 9
    center_x = left_sudoku + col * cell_width + cell_width // 2
    center_y = top_sudoku + row * cell_height + cell_height // 2

    pyautogui.click(center_x, center_y)
    print(f"Clicked on cell ({row}, {col}) at ({center_x}, {center_y})")

# 数字から英語の単語へのマッピング
number_to_name = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

def number_click(button_name):
    # 数字を英語の単語に変換
    button_name = number_to_name.get(button_name, button_name)
    
    if button_name in button_centers:
        center = button_centers[button_name]
        pyautogui.click(center)
        print(f"Clicked on {button_name} at {center}")
    else:
        print(f"Button {button_name} does not exist")

def click_all_cells_and_buttons(sudoku):
    for row in range(9):
        for col in range(9):
            num = sudoku[row][col]
            if num != 0:
                # Click the corresponding cell
                click_cell(row, col)

                # Click the corresponding button
                number_click(str(num))

def main():
    file_path = "updated_final_numbers.xlsx"
    sudoku = read_sudoku_from_excel(file_path)

    print("Initial Sudoku:")
    for row in sudoku:
        print(row)

    if solve_sudoku(sudoku):
        print("\nSolved Sudoku:")
        for row in sudoku:
            print(row)

        # Click all cells and buttons after solving the Sudoku
        click_all_cells_and_buttons(sudoku)
    else:
        print("No solution exists for the given Sudoku.")

# Sudoku grid coordinates
left_sudoku = 82
top_sudoku = 242
right_sudoku = 404
bottom_sudoku = 567
width_sudoku = right_sudoku - left_sudoku
height_sudoku = bottom_sudoku - top_sudoku

# Button grid coordinates
left_button = 410
top_button = 350
right_button = 700
bottom_button = 570
width_button = right_button - left_button
height_button = bottom_button - top_button

button_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
button_centers = {}

button_width = width_button // 3
button_height = height_button // 3

for i in range(3):
    for j in range(3):
        button_name = button_names[i * 3 + j]
        center_x = left_button + j * button_width + button_width // 2
        center_y = top_button + i * button_height + button_height // 2
        button_centers[button_name] = (center_x, center_y)

# ボタンの中心座標を表示
print("ボタンの中心座標:")
for name, center in button_centers.items():
    print(f"{name}: {center}")

if __name__ == "__main__":
    main()

