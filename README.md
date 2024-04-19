넷마블의 틀린그림 찾기 게임에서 매직아이 기능을 자체 제작하였습니다.

기본 아이디어
![image](https://github.com/100-heon/Find_Diff_two_imgs/assets/158144807/921be3e1-c651-4d9f-afac-456f86237602)

첫번째 시도 
![image](https://github.com/100-heon/Find_Diff_two_imgs/assets/158144807/34f18375-8671-4d3e-ad0f-d8ec291c11e0)



첫 결과
![image](https://github.com/100-heon/Find_Diff_two_imgs/assets/158144807/f283d295-f5a4-4536-88b8-38b27db25e34)



원인 분석
![image](https://github.com/100-heon/Find_Diff_two_imgs/assets/158144807/f825ab97-1440-4f23-92b3-6860b2863df0)


해결 방안
두 이미지를 하나의 이미지로 정렬한 뒤 crop 하기

SIFT +  FLANMatcher, Homography
![image](https://github.com/100-heon/Find_Diff_two_imgs/assets/158144807/5daef09d-251e-48c8-bfa9-c6ff78675f10)


실제 매치 이미지
![image](https://github.com/100-heon/Find_Diff_two_imgs/assets/158144807/a7adcb2a-3707-41f9-bbe9-28e74cca2541)

이렇게 출려된 매치들 중 distance가 짧은 상위 몇개의 매치를 리스트에 저장.
distacne가 작을 수록 좋은 매치.


매치를 활용하여 호모그래피를 계산하여 두 이미지간의 변환관계를 구한다.
![image](https://github.com/100-heon/Find_Diff_two_imgs/assets/158144807/2a596614-f914-4c3d-99d7-abef63797f03)


input images
![image](https://github.com/100-heon/Find_Diff_two_imgs/assets/158144807/087889de-e11f-410e-9aea-3577994003db)

output images
![image](https://github.com/100-heon/Find_Diff_two_imgs/assets/158144807/7f8b9ae0-fac5-4acc-8e46-b0439db16aa1)
