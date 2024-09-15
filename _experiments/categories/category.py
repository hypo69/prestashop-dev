﻿## \file src/prestashop/_experiments/categories/category.py
"""!  Работа с категориями товара 

"""

## \file ../src/prestashop/_experiments/categories/category.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python



from pathlib import Path
import os
from typing import Union


from src.settings import gs
from src.utils import  pprint

from src.prestashop import PrestaCategory
# -----------------------------------

def get_parent_categories_list(id_category):
    return PrestaCategory.get_parent_categories_list(id_category)

class Category (PrestaCategory):
    """ Класс категорий товара. Наследует `PrestaCategory` """
    credentials: dict = None

    def get_api_credentials (self) -> dict:
        """! Функция вытаскиват из объекта глобальных настроек `gs` словарь подключений
        к базе данных, которая содержит все категории (f.e. https://e-cat.co.il/api)
        @returns словарь API параметров подключения
        """
        return next((item for item in gs.presta_credentials if bool(item['have_full_categoris_tree'])), None)

    def __init__(self, credentials:dict = None, *args, **kwards):
        """! Если я не определяю параметры подключения при инициализации функции - я подразумеваю, что 
        буду работать с базой данных, в которой гарантированно есть все категории проекта.
        На момент написания кода это база данных проекта e-cat.co.il
        """
        self.credentials = self.get_api_credentials() if not credentials else credentials

        super().__init__(self.credentials, *args, **kwards)
        ...