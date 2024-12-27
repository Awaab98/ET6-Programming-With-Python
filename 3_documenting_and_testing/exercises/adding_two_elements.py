#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for performing simple addition on two elements.

Module contents:
    - adding_two_elements: Adds two elements and returns the sum

Created on 2024-12-20
Author: Awaab98
"""
def adding_two_elements(first_element: int,second_element:int) -> int:
    """ returns a value that represents the sum of the two elements

    Parameters:
        first_element (int): the first value to be added
        second_element (int): the second value to be added

    Returns:
        int: the sum of the two elements
        
    Raises:
        if one of the two inputs is not an integer
        
    Examples:
        >>> adding_two_elements(0,1)
        1
        >>> adding_two_elements(2,5)
        7
        >>> adding_two_elements(9,1)
        10
        >>> adding_two_elements("hello", 5)
        Traceback (most recent call last):
        ...
        AssertionError: Cannot add string and integer
        
    """
    # Ensuring that the two elements has the same data type
    assert not (isinstance(first_element, str) and isinstance(second_element, int) or \
        isinstance(first_element, int) and isinstance(second_element, str)), "Cannot add string and integer"
    
    return first_element + second_element
