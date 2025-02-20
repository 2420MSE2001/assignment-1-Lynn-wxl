# main.py

def calculate_sum(n):
    # 在此编写代码
    if n==1 or n==0:
        return n
    elif n>1:
        return calculate_sum(n-1)+n


if __name__ == "__main__":
    result = calculate_sum(50)
    print(f"1+2+...+50的和是：{result}")
