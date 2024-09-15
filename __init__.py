"""! Модуль обработки запросов к базам данных Prestashop.
Адаптер для API
"""
...
## \file ../src/prestashop/__init__.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
...
from packaging.version import Version
from .version import __version__, __name__, __doc__, __details__, __annotations__,  __author__  

from .api import Prestashop
from .product import PrestaProduct
from .supplier import PrestaSupplier
from .category import PrestaCategory
from .warehouse import PrestaWarehouse
from .language import PrestaLanguage
from .shop import PrestaShop
from .pricelist import PriceListRequester
from .customer import PrestaCustomer
