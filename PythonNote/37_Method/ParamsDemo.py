# 37.3. ParamsDemo.py
# ���� ���� �Ű� ������ ���� �Լ� �����
# => sum_all() �Լ��� ���� ������ ���� ���� �������� ���� �� ����
def sum_all(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

# ���� ���� �Ű� ������ ���� �Լ� ȣ���ϱ� 
sum_all(3, 5) # 8
sum_all(3, 5, 7) # 15
sum_all(3, 5, 7, 9) # 24
