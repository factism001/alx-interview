#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.

    :param boxes:
    :return: True or False
    """
    opened_boxes = [0]

    for i in range(len(boxes)):
        for key in boxes[i]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.append(key)
    if len(opened_boxes) == len(boxes):
        return True
    else:
        return False
