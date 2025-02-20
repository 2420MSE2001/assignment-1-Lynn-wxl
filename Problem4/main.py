# main.py

def left_side(x, num_terms):
    """
    计算方程左侧前 num_terms 项的和。
    """
    result = 0
    for n in range(num_terms):
        result += (2**(n)*x**(2**(n)-1)-(2**(n+1))*(x**((2**(n+1))-1)))/(1-x**(2**(n))+x**(2**(n+1)))
        print(result)
    return result

def right_side(x):
    """
    计算方程右侧的固定值。
    """
    result = (1+2*x)/(1+x+x**2)
    print("right",result)
    return result

def find_num_terms(x, tolerance=1e-6):
    """
    寻找满足左侧与右侧差异小于容差的最小项数。
    """
    num_term = 0
    while num_term<50:
        num_term +=1
        if abs(left_side(x, num_term)-right_side(x)) < tolerance:
            break
    return num_term

if __name__ == "__main__":
    x = 0.25  # 题目给定的 x 值
    num_terms = find_num_terms(x)
    print(f"所需最小项数: {num_terms}")
