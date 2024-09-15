﻿## \file src/prestashop/supplier.py
## \file ../src/prestashop/supplier.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! @namespace src.pestashop 
Класс поставщика в `Prestashop`"""
...
from types import SimpleNamespace
from src.settings import gs
from src.logger import logger
from src.utils import j_loads as j_loads
from .api import Prestashop


class PrestaSupplier (Prestashop):
    """! """
    def __init__(self, api_credentials: dict | SimpleNamespace, *args,**kwards):
        super().__init__(
            api_credentials['api_domain'], 
            api_credentials['api_key'], *args,**kwards)

