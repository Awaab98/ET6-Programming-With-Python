#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting the words in a string.
This is part of the debugging exercise series focusing on buggy implementations.

Module contents:
    - count_words: Counts the number of words in a string

Created on 2024-12-06
Author: Claude AI
"""

def count_words(text: str) -> int:
    """Counts the number of words in a string.
    Words are separated by spaces.

    Parameters:
        text: str, the input string

    Returns -> int: number of words in the text

    Examples:
        >>> count_words("hello world")
        2
        >>> count_words("one")
        1
        >>> count_words("")
        0
    """
    assert isinstance(text, str), "input must be a string"
    
    splitted_text = text.split(" ")
    
    words_counter = 0
    for word in splitted_text:
        if word != '':
            words_counter += 1
    
    return words_counter
