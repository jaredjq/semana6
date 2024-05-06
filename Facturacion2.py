# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:41:25 2024

@author: Dell
"""

import financieros

total = 1000.49
print(f"Subtotal: {financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")
