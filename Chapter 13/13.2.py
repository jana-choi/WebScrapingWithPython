from PIL import Image
import pytesseract

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    
    print("### before")
    print(pytesseract.image_to_string(image))

    # 임계점을 설정하고 이미지를 저장합니다.
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)
    return image


image = cleanFile("./textBad.png", "./textCleaned.png")

# 테서랙트를 호출해 새로 생성된 이미지를 인식합니다.
print("### after")
print(pytesseract.image_to_string(image))