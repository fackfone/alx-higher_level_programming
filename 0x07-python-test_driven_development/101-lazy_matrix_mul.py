#!/usr/bin/python3
'''this module for matrices 
calculations using numpy'''


import numpy as nump


def lazy_matrix_mul(m_a, m_b):
    '''multipy 2 patrices with numpy'''
    return nump.dot(m_a, m_b)
