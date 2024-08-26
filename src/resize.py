import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory


"""
토큰의 수를 줄이기 위해 원본 데이터셋 이미지의 크기를 줄이는데 사용한 스크립트
"""

# 인식할 확장자
extensions = ("jpg", "jpeg", "png")

if __name__ == "__main__":
    Tk().withdraw()

    load_folder_path = askdirectory(title="불러올 폴더 선택")
    save_folder_path = askdirectory(title="저장할 폴더 선택")

    num = 1
    while True:
        load_path = ""
        save_path = save_folder_path + f"/resized{num}.jpg"

        # 확장자 별로 파일 검색
        is_file_exists = False
        for extension in extensions:
            load_path = load_folder_path + f"/image{num}.{extension}"
            if os.path.isfile(load_path):
                is_file_exists = True
                break

        if not is_file_exists:
            exit()

        img = Image.open(load_path)

        # 표 이미지 크기 조정
        img.thumbnail((512, 512))

        # 표 이미지 저장
        img.save(save_path)

        # 다음 이미지로 넘어가기
        num += 1
