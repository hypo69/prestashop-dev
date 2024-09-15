## \file src/prestashop/product.py
## \file ../src/prestashop/product.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Класс товара `Prestashop`"""
...

import os,sys
from attr import attr, attrs
from pathlib import Path
from typing import Dict, List
# ----------------------------------
from src.settings import gs
from src.utils import  pprint
from .api import Prestashop
from src.logger import logger
from src.logger.exceptions import PrestaShopException


class PrestaProduct(Prestashop):
    """ Класс товара из модуля prestashop
   Непосредственно выполняет все операции через API
   ------------------------------------
   Methods:
    check(product_reference: str): Проверка наличия товара в бд
        по product_reference (SKU, MKT)
        Вернет словарь товара, если товар есть, иначе False
    search(filter: str, value: str): Расширенный поиск в БД по фильтрам
    get(id_product): Возвращает информацию о товаре по ID
    """

    
    def __init__(self, api_credentials, *args,**kwards):
        super().__init__(
            api_credentials['api_domain'], 
            api_credentials['api_key'], *args,**kwards)
     