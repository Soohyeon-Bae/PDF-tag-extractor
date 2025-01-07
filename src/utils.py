# src/utils.py

from tqdm import tqdm
import re


def display_progress(iterable, desc='', total=None, unit='item'):
    """Display a progress bar for the given iterable"""
    if total is None:
        total = len(iterable)
    return tqdm(iterable, desc=desc, total=total, unit=unit)
