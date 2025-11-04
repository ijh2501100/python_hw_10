# python_hw_10
# Python GitHub 과제

## 1. 과제 개요
- VS Code에서 Python 프로젝트를 생성하고 Git/GitHub을 활용하여 버전 관리 및 저장소 연동을 실습한다.  
---

## 2. 수행 과정
1. **#25.py 작성 및 첫 commit**
   - commit 메시지: `add #25.py`  
   - 기능: 표준 입력으로 키와 해당 값들을 각각 입력 받은 후, dictionary로 만들고 출력
    keys = input('alpha bravo charlie delta echo foxtrot golf를 입력하세요: ').split()
    values = list(map(int, input('30 40 50 60 70 80 90를 입력하세요: ').split()))
    a = dict(zip(keys, values))

    del a['alpha']
    del a['delta']

    print(a)

2. **두 번째 commit**
   - commit 메시지: `add #26.py` 
   - 기능: park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}의 dictionary을 선언하고, english 점수와 science 점수를 출력
     park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
     print('english 점수: ', park['english'])
     print('science 점수: ', park['science'])
   

3. **세 번째 commit**
   - commit 메시지:`add #27,py`
   - 기능: kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}의 dictionary을 선언하고, 모든 과목을 100점으로 수정 후 출력
   kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
   kim = dict.fromkeys(kim.keys(), 100)
   print(kim)


4. **네 번째 commit**
   - commit 메시지:`add #28,py`
   - 기능: lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}의 dictionary을 선언하고, english의 key가 있는지 체크하고 있으면, 해당 key-value을 삭제 후 출력
   lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
   if 'english' in lee:
    del lee ['english']
   print(lee)


5. **다섯 번째 commit**
   - commit 메시지:`add #29,py`
   - 기능: lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}의 dictionary을 선언하고, key와 value를 모두 출력
    lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
    for key, value in lim.items():
        print(key, value)


6. **여섯 번째 commit**
   - commit 메시지:`add #30,py`
   - 기능: choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}의 dictionary을 선언하고, 90점 이상인 과목들의 key만 출력
    choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
    for subject, score in choi.items():
        if score >= 90:
            print(subject)


6. **일곱 번째 commit**
   - commit 메시지:`add #31,py`
   - 기능: yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}의 dictionary을 선언하고, 4과목의 평균을 출력
    yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
    average = sum(yoo.values()) / len(yoo)
    print("평균 점수: ", average) 
---

## 5. GitHub Repository URL
- URL: [https://github.com/ijh2501100/python_hw_10.git]  
