## \file src/prestashop/warehouse.py
## \file ../src/prestashop/warehouse.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Класс склада (warwehouse) `Prestashop`"""


import os,sys
from attr import attr, attrs
from pathlib import Path

from src.settings import gs
from src.utils import  pprint
from .api import Prestashop
from src.logger import logger


class PrestaWarehouse(Prestashop): 
    ...