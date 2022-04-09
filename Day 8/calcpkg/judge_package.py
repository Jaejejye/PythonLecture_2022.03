from calcpkg import operation, geometry
r = int(input())
print(operation.squareroot(r))
print(geometry.circle_area(r))

# --> 해당 ... 패키지가 자꾸 오류나서 실행이 안댐... 일단 코딩도장 답으로는 테스트 통과 함...
"""
calcpkg 패키지는 __init__.py 파일이 비어 있고, operation 모듈과 geometry 모듈만 들어있습니다. 따라서 패키지를 사용할 때는 import 패키지.모듈 형식으로 가져온 뒤 패키지.모듈.함수() 형식으로 사용해야 합니다.

일단 정수가 입력된다고 했으므로 int(input())과 같이 입력 값을 정수로 변환한 뒤 변수에 저장합니다(이하 변수는 n).

그다음에 제곱은은 calcpkg.operation.squareroot에 n을 넣은 뒤 print로 반환값을 출력하고, 원의 넓이는 calcpkg.geometry.circle_area에 n을 넣은 뒤 print로 반환값을 출력하면 됩니다.
"""