import pyautogui

# 座標の設定
left = 410
top = 350
right = 700
bottom = 570
# 幅と高さを計算
width = right - left
height = bottom - top

# スクリーンショットの取得と保存
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save("screenshot_capture.png")

print("スクリーンショットを保存しました: screenshot_capture.png")

# 3x3の領域に分割
button_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
button_centers = {}

button_width = width // 3
button_height = height // 3

for i in range(3):
    for j in range(3):
        button_name = button_names[i * 3 + j]
        center_x = left + j * button_width + button_width // 2
        center_y = top + i * button_height + button_height // 2
        button_centers[button_name] = (center_x, center_y)


# ボタンの中心座標を表示
print("ボタンの中心座標:")
for name, center in button_centers.items():
    print(f"{name}: {center}")

# ボタンをクリックする関数
def number_click(button_name):
    if button_name in button_centers:
        center = button_centers[button_name]
        pyautogui.click(center)
        print(f"Clicked on {button_name} at {center}")
    else:
        print(f"Button {button_name} does not exist")
