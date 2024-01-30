import cv2
import numpy as np
import pyautogui
from PIL import Image, ImageChops
import cv2
import numpy as np
import pyautogui

region1 = (586, 171, 368, 560)
region2 = (963, 171, 368, 560)

def capture_screenshots(region1, region2):
    """Capture screenshots of the given regions."""
    screenshot1 = pyautogui.screenshot(region=region1)
    screenshot1.save("screenshot1.png")
    screenshot2 = pyautogui.screenshot(region=region2)
    screenshot2.save("screenshot2.png")
    
    

def align_images1(image1, image2):
    # SIFT detector를 사용하여 특징점 찾기
    sift = cv2.SIFT_create()
    keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

    # 특징점을 매칭하기 위한 FLANN 매처
    matcher = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict())
    matches = matcher.knnMatch(descriptors1, descriptors2, k=2)

    # 좋은 매치 필터링
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # 호모그래피 계산
    if len(good_matches) > 4:
        src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        matrix, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        aligned_image = cv2.warpPerspective(image1, matrix, (image2.shape[1], image2.shape[0]))

        return aligned_image
    else:
        return None
    

    

# assign images 
#capture_screenshots(region1, region2)


# OpenCV로 이미지 불러오기
image1 = cv2.imread('screenshot1.png')
image2 = cv2.imread('screenshot2.png')

# 이미지 정렬
aligned_image1_cv = align_images1(image1, image2)

if aligned_image1_cv is not None:
    # 정렬된 이미지 저장
    cv2.imwrite('aligned_screenshot2.png', aligned_image1_cv)

    # PIL로 이미지 불러오기
    image2_pil = Image.open('screenshot2.png')
    aligned_image1_pil = Image.open('aligned_screenshot2.png')

    # 차이 계산
    diff = ImageChops.difference(image2_pil, aligned_image1_pil)

    # 차이 이미지 표시ds
    diff.show() 
else:
    print("이미지 정렬 실패")
