from PIL import Image

def get_total_brightness(image_path):
    try:
        # 이미지 열기
        img = Image.open(image_path)

        # 이미지 크기 구하기
        width, height = img.size

        # 모든 픽셀의 밝기 값을 더하는 변수 초기화
        total_brightness = 0
        Bgpixel = img.getpixel((0, 0))
        BgBrightness = (sum(Bgpixel) // len(Bgpixel))

        # 각 픽셀의 밝기 값 추출
        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))

                # 픽셀의 밝기 값 구하기 (RGB 이미지라면 R, G, B 성분을 모두 더한 후 평균값을 사용합니다)
                brightness = (sum(pixel) // len(pixel))

                # 픽셀의 밝기 값 더하기
                total_brightness += brightness

        return total_brightness

    except Exception as e:
        print("오류 발생:", str(e))
        return None

# 이미지 파일 경로 력
image_pathB = "B-O 5.jpg"  # 본인의 이미지 파일 경로로 바꿔주세요
image_pathV = "V-O 5.jpg"  # 본인의 이미지 파일 경로로 바꿔주세요

# 모든 픽셀의 밝기 값 더하기
total_brightnessB = get_total_brightness(image_pathB)
total_brightnessV = get_total_brightness(image_pathV)

# 결과 출력
if total_brightnessB is not None:
    print("B필터:", total_brightnessB)
    print("V필터:", total_brightnessV)
    print("V-B:", total_brightnessV-total_brightnessB)
    print("V/B:", total_brightnessV/total_brightnessB)