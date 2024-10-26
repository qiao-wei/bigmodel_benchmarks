import random

def generate_random_numbers(n):
    """生成n个随机数的列表"""
    return [random.randint(1, 100) for _ in range(n)]

def calculate_average(numbers):
    """计算平均值"""
    return sum(numbers) / len(numbers)

# def generate_random_numbers(numbers):
#    """计算平均值"""
#    return sum(numbers) / len(numbers)

# def calculate_average(numbers):
#    """计算平均值"""
#    return sum(numbers) / len(numbers)

# 生成10个随机数
random_numbers = generate_random_numbers(10)
print("随机数列表:", random_numbers)

# 计算并打印平均值
average = calculate_average(random_numbers)
print("平均值:", average)
