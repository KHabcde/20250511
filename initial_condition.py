import pyautogui
import pytesseract
from PIL import Image
import pytesseract
from collections import Counter
import numpy as np
import pandas as pd

# 座標の設定
left = 82
top = 242
right = 404
bottom = 567
# 幅と高さを計算
width = right - left
height = bottom - top

# スクリーンショットの取得と保存
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")

print("スクリーンショットを保存しました: screenshot_capture.png")

# Tesseract OCRのパスを設定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 領域を9x9のマスに分割
cell_width = width // 9
cell_height = height // 9

# 各マスのスクリーンショットを撮影し、OCRで数字を読み取る
numbers_1 = []
for row in range(9):
    row_numbers_1 = []
    for col in range(9):
        # 各マスの座標を計算
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_right = cell_left + cell_width
        cell_bottom = cell_top + cell_height

        # スクリーンショットを撮影
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)

        # OCRで数字を読み取る
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        # 数字をリストに追加
        row_numbers_1.append(cell_number if cell_number.isdigit() else None)
    numbers_1.append(row_numbers_1)

# 結果を表示
for row in numbers_1:
    print(row)


# 座標の設定
left = 82
top = 242-1
right = 404
bottom = 567-1
# 幅と高さを計算
width = right - left
height = bottom - top

# スクリーンショットの取得と保存
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")

print("スクリーンショットを保存しました: screenshot_capture.png")

# Tesseract OCRのパスを設定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 領域を9x9のマスに分割
cell_width = width // 9
cell_height = height // 9

# 各マスのスクリーンショットを撮影し、OCRで数字を読み取る
numbers_2 = []
for row in range(9):
    row_numbers_2 = []
    for col in range(9):
        # 各マスの座標を計算
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_right = cell_left + cell_width
        cell_bottom = cell_top + cell_height

        # スクリーンショットを撮影
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)

        # OCRで数字を読み取る
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        # 数字をリストに追加
        row_numbers_2.append(cell_number if cell_number.isdigit() else None)
    numbers_2.append(row_numbers_2)

# 結果を表示
for row in numbers_2:
    print(row)
    
    
# 座標の設定
left = 82-1
top = 242-1
right = 404-1
bottom = 567-1
# 幅と高さを計算
width = right - left
height = bottom - top

# スクリーンショットの取得と保存
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")

print("スクリーンショットを保存しました: screenshot_capture.png")

# Tesseract OCRのパスを設定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 領域を9x9のマスに分割
cell_width = width // 9
cell_height = height // 9

# 各マスのスクリーンショットを撮影し、OCRで数字を読み取る
numbers_3 = []
for row in range(9):
    row_numbers_3 = []
    for col in range(9):
        # 各マスの座標を計算
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_right = cell_left + cell_width
        cell_bottom = cell_top + cell_height

        # スクリーンショットを撮影
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)

        # OCRで数字を読み取る
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        # 数字をリストに追加
        row_numbers_3.append(cell_number if cell_number.isdigit() else None)
    numbers_3.append(row_numbers_3)

# 結果を表示
for row in numbers_3:
    print(row)

# 4回目の処理
left = 82
top = 242+1
right = 404
bottom = 567+1
width = right - left
height = bottom - top
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")
print("スクリーンショットを保存しました: screenshot_capture.png")
cell_width = width // 9
cell_height = height // 9
numbers_4 = []
for row in range(9):
    row_numbers_4 = []
    for col in range(9):
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        row_numbers_4.append(cell_number if cell_number.isdigit() else None)
    numbers_4.append(row_numbers_4)
for row in numbers_4:
    print(row)

# 5回目の処理
left = 82+1
top = 242
right = 404+1
bottom = 567
width = right - left
height = bottom - top
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")
print("スクリーンショットを保存しました: screenshot_capture.png")
cell_width = width // 9
cell_height = height // 9
numbers_5 = []
for row in range(9):
    row_numbers_5 = []
    for col in range(9):
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        row_numbers_5.append(cell_number if cell_number.isdigit() else None)
    numbers_5.append(row_numbers_5)
for row in numbers_5:
    print(row)

# 6回目の処理
left = 82+1
top = 242+1
right = 404+1
bottom = 567+1
width = right - left
height = bottom - top
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")
print("スクリーンショットを保存しました: screenshot_capture.png")
cell_width = width // 9
cell_height = height // 9
numbers_6 = []
for row in range(9):
    row_numbers_6 = []
    for col in range(9):
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        row_numbers_6.append(cell_number if cell_number.isdigit() else None)
    numbers_6.append(row_numbers_6)
for row in numbers_6:
    print(row)

# 7回目の処理
left = 82-1
top = 242+1
right = 404-1
bottom = 567+1
width = right - left
height = bottom - top
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")
print("スクリーンショットを保存しました: screenshot_capture.png")
cell_width = width // 9
cell_height = height // 9
numbers_7 = []
for row in range(9):
    row_numbers_7 = []
    for col in range(9):
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        row_numbers_7.append(cell_number if cell_number.isdigit() else None)
    numbers_7.append(row_numbers_7)
for row in numbers_7:
    print(row)

# 8回目の処理
left = 82+1
top = 242-1
right = 404+1
bottom = 567-1
width = right - left
height = bottom - top
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")
print("スクリーンショットを保存しました: screenshot_capture.png")
cell_width = width // 9
cell_height = height // 9
numbers_8 = []
for row in range(9):
    row_numbers_8 = []
    for col in range(9):
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        row_numbers_8.append(cell_number if cell_number.isdigit() else None)
    numbers_8.append(row_numbers_8)
for row in numbers_8:
    print(row)

# 9回目の処理
left = 82-1
top = 242-1
right = 404+1
bottom = 567+1
width = right - left
height = bottom - top
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")
print("スクリーンショットを保存しました: screenshot_capture.png")
cell_width = width // 9
cell_height = height // 9
numbers_9 = []
for row in range(9):
    row_numbers_9 = []
    for col in range(9):
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        row_numbers_9.append(cell_number if cell_number.isdigit() else None)
    numbers_9.append(row_numbers_9)
for row in numbers_9:
    print(row)

# 10回目の処理
left = 82+1
top = 242+1
right = 404-1
bottom = 567-1
width = right - left
height = bottom - top
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")
print("スクリーンショットを保存しました: screenshot_capture.png")
cell_width = width // 9
cell_height = height // 9
numbers_10 = []
for row in range(9):
    row_numbers_10 = []
    for col in range(9):
        cell_left = left + col * cell_width
        cell_top = top + row * cell_height
        cell_screenshot = pyautogui.screenshot(region=(cell_left, cell_top, cell_width, cell_height))
        cell_image_path = f"cell_{row}_{col}.png"
        cell_screenshot.save(cell_image_path)
        cell_image = Image.open(cell_image_path)
        cell_text = pytesseract.image_to_string(cell_image, config='--psm 10 digits')
        cell_number = cell_text.strip()

        # 数値が10以上の場合は1の位を採用
        if cell_number.isdigit() and int(cell_number) >= 10:
            cell_number = str(int(cell_number) % 10)

        row_numbers_10.append(cell_number if cell_number.isdigit() else None)
    numbers_10.append(row_numbers_10)
for row in numbers_10:
    print(row)

# 各回の読み取り結果をリストにまとめる
all_numbers = [numbers_1, numbers_2, numbers_3, numbers_4, numbers_5, numbers_6, numbers_7, numbers_8, numbers_9, numbers_10]

# 各マスの最頻値を計算する
final_numbers = []
uncertain_cells = []  # 最頻値が決定しにくいセルを記録
for row in range(9):
    final_row = []
    for col in range(9):
        # 各回の同じマスの値を収集
        cell_values = [numbers[row][col] for numbers in all_numbers]

        # 空欄を含む妥当な値（None, 1-9）をフィルタリング
        valid_values = [int(value) if value and value.isdigit() and 1 <= int(value) <= 9 else None for value in cell_values]

        # 最頻値を計算
        most_common = Counter(valid_values).most_common()
        if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
            # 出現頻度が拮抗している場合
            final_row.append("?")  # 印として"?"を追加
            uncertain_cells.append((row, col))
        elif most_common:
            final_row.append(most_common[0][0])  # 最頻値を追加
        else:
            final_row.append(None)  # 空欄を妥当な結果として扱う
    final_numbers.append(final_row)

# 最終結果を表示
print("最終的な読み取り結果:")
for row in final_numbers:
    print(row)

# 不確定なセルを表示
if uncertain_cells:
    print("最頻値が決定しにくいセル:")
    for cell in uncertain_cells:
        print(f"行: {cell[0]}, 列: {cell[1]}")

# 最終結果をテキストファイルに保存
with open("final_numbers.txt", "w", encoding="utf-8") as f:
    f.write("最終的な読み取り結果:\n")
    for row in final_numbers:
        f.write(" ".join(str(cell) if cell is not None else "None" for cell in row) + "\n")

# 不確定なセルをテキストファイルに保存
if uncertain_cells:
    with open("uncertain_cells.txt", "w", encoding="utf-8") as f:
        f.write("最頻値が決定しにくいセル:\n")
        for cell in uncertain_cells:
            f.write(f"行: {cell[0]}, 列: {cell[1]}\n")

def read_final_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]  # Skip the first line
        array = []
        for line in lines:
            row = [int(x) if x.isdigit() else None for x in line.strip().split()]
            array.append(row)
        return np.array(array)

def update_uncertain_cell(array, row, col):
    print(f"Current value at Row {row}, Column {col}: {array[row][col]}")
    new_value = input("Enter a new value for this cell: ")
    array[row][col] = int(new_value) if new_value.isdigit() else None
    return array

def save_to_excel(array, output_path):
    df = pd.DataFrame(array)
    df.to_excel(output_path, index=False, header=False)

if __name__ == "__main__":
    final_numbers_path = "final_numbers.txt"
    uncertain_cells_path = "uncertain_cells.txt"
    output_excel_path = "updated_final_numbers.xlsx"

    # Read the 2D array from final_numbers.txt
    final_numbers = read_final_numbers(final_numbers_path)

    # Update uncertain cells
    with open(uncertain_cells_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]  # Skip the first line
        for line in lines:
            try:
                row, col = map(int, line.strip().split(': ')[1].split(', '))
                final_numbers = update_uncertain_cell(final_numbers, row, col)
            except (ValueError, IndexError) as e:
                print(f"Skipping invalid line in uncertain_cells.txt: {line.strip()} ({e})")

    # Save updated array to Excel
    save_to_excel(final_numbers, output_excel_path)
    print(f"Updated 2D array saved to {output_excel_path}")


