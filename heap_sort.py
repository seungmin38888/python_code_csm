# [Do it! 실습 6-16] 힙 정렬 알고리즘 구현하기

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """힙 정렬"""

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 힙으로 만들기"""
        temp = a[left]      # 루트

        parent = left
        while parent < (right + 1) // 2:   # 왜  while기준이 이거야?
            cl = parent * 2 + 1     # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl  # 큰 값을 선택합니다. 이유: 밑에 자식과 부모의 값 비교에서 부모가 자식보다 더 커야하므로 비교군을 자식중에 가장 큰 자식으로 골라야함
            if temp >= a[child]:
                break
            # a[left] 가 a[child] 보다 더 작을 경우 a[left]를 내리고 부모 자리에 a[child]를 올리는 작업을 한다.
            a[parent] = a[child]  
            parent = child # parent 원소값까지 child의 값으로 바꿔줌으로써 위의 while문을 반복안하게 됨
            # 부모 자리에 부모값보다 더큰 자식값을 넣기 완료
        a[parent] = temp # 바뀐 parent는 결국 방금 부모 노드로 올라간 값의 원래 자식이었을때의 자리이며 자식보다 작은 부모의 값이 대신 들어간다. 

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):   # a[i] ~ a[n-1]을 힙으로 만들기
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]     # 최댓값인 a[0]과 마지막 원소 a[i]를 교환
        down_heap(a, 0, i - 1)      # a[0] ~ a[i-1]을 힙으로 만들기

if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')