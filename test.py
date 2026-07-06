import base64
import sys

file_path = r"C:\RPA\이미지분석및생성\Output\sample.txt"

# 1. txt 파일 읽기
with open(file_path, "r", encoding="utf-8") as f:
    b64_json = f.read().strip()

# 2. base64 → 이미지 변환
image_bytes = base64.b64decode(b64_json)

# 3. 저장
with open(fr"C:\RPA\이미지분석및생성\Output\{sys.argv[1]}.png", "wb") as f:
    f.write(image_bytes)

print("이미지 저장 완료")