## \file src/prestashop/language.py
## \file ../src/prestashop/language.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""!   класс языка в `Prestashop` """
...
from .api import Prestashop
from src.settings import gs
from src.utils import  pprint
from .api import Prestashop
from src.logger import logger
from src.logger.exceptions import PrestaShopException

class PrestaLanguage(Prestashop):
    """! Класс, отвечающий за настройки языков магазина"""
    def __init__(self, api_credentials, *args,**kwards):
        super().__init__(api_credentials, *args,**kwards)
        
    

            

