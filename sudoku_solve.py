import openpyxl

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
    else:
        print("No solution exists for the given Sudoku.")

if __name__ == "__main__":
    main()