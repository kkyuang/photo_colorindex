from PIL import Image

import matplotlib.pyplot as plt

def display_image_with_mouse_coordinates(image_path):
    try:
        # 원본 이미지 불러오기
        image = Image.open(image_path)

        # 이미지 표시
        fig, ax = plt.subplots()
        ax.imshow(image)
        plt.axis("off")
        plt.show()
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

def crop_and_save(input_image_path, output_image_path, x, y, width, height):
    try:
        # 원본 이미지 불러오기
        image = Image.open(input_image_path)

        # 확대하여 보여줄 부분 추출
        region = image.crop((x-width/2, y-width/2, x + width/2, y + height/2))

        # 추출한 부분을 원하는 크기로 변경 (선택사항, 주석 처리해도 됨)
        # resized_region = region.resize((new_width, new_height))

        # 잘라낸 부분 저장
        region.save(output_image_path)

        print("이미지가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    # 원본 이미지 경로와 저장할 이미지 경로 입력
    input_image_path = "DSC_0602.jpg"
    output_image_path = "B-O VEGA.jpg"
    
    display_image_with_mouse_coordinates(input_image_path)

    # 표시하고자 하는 직사각형의 왼쪽 상단 좌표와 크기 입력
    x = int(input("시작 x 좌표: "))
    y = int(input("시작 y 좌표: "))
    width = int(input("폭: "))
    height = int(input("높이: "))

    # 함수 호출하여 이미지 처리
    crop_and_save(input_image_path, output_image_path, x, y, width, height)
