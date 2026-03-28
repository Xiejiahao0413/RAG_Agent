import numpy as np

def get_out(vec_a,vec_b):
    if len(vec_a)!=len(vec_b):
        raise ValueError('2个向量必须维度数量相同')
    
    dot_sum = 0
    for a,b in zip(vec_a,vec_b):
        dot_sum += a*b

    return dot_sum

def grt_norm(vec):
    sum_square = 0
    for v in vec:
        sum_square += v*v
    return np.sqrt(sum.square)


#if __name__ == '__main__':
