## \file src/prestashop/api/____api_adaptor.py
## \file ../src/prestashop/api/____api_adaptor.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

...

from typing import List, Dict, Tuple
# from prestapyt import PrestaShopWebServiceDict
# from src.prestashop.presta_apis.presta_python_api_v1 import PrestaAPIV1 
# from src.prestashop.presta_apis.presta_python_api_v2 import PrestaAPIV2
from src.prestashop.presta_apis.core import Prestashop
from src.logger import logger
from src.settings import gs
...


class PrestaAPIV(Prestashop):
    """! Adapter for different library versions retrieved from GitHub.
    locator_description - this is a workaround, another layer is not needed. The problem is to test and check different solutions from different libraries and build your own.
    """
    connector = None
    api_credentials: str = None
    
    def __init__(self, api_credentials, *args, **kwards):
        """! 
        
        @details
        @param self `object` : description
        @returns None
        """
        self.api_credentials = api_credentials
        #self._payload(api_credentials, *args, **kwards)
        self.connector = PrestaAPIV3(api_credentials['api_domain'], api_credentials['api_key'])
        ...
        
  
    
    def get(self, resource: str = None, resource_id: int |  str = None,
            resource_ids: int | str | List[str, tuple] = None,
            search_filter: dict = None,
            display: str | list = 'full',
            sort: str = None,
            limit: str = None,
            schema: str = None,
            io_format: str = 'JSON') -> dict:
        """!
         Retrieve data from the API.
        @param resource `str` : API resource.
        @param resource_id `int|str` : Resource identifier.
        @param resource_ids `int, str, List[str], Tuple(str)` : Query filter.
        @param search_filter `dict` : Search filter.
        @param display `str|list` : Display mode.
        @returns `dict` : Query result.
        """

        if 'prestapyt' in gs.default_PrestaAPIV:
            """! resource_ids works with `delete` """
            if not search_filter:
                search_filter = {}
            if schema:
                search_filter.update({'schema': schema})
            if display:
                search_filter.update({'display': display})

            response = self.connector.get(resource=resource, resource_id=resource_id, options=search_filter)

            if resource == 'categories':
                return response.get('category') if resource_id else response.get('categories', {}).get('category')
            elif resource == 'products':
                return response.get('products', False) if response.get('products') != '' else False
            elif resource == 'languages':
                return response.get('languages', {}).get('language')
            # Add handling for other resources here
            else:
                return response
            ...
        
        elif 'V1' in gs.default_PrestaAPIV:
            return self.connector.get(resource, resource_id, search_filter)

        elif 'V2' in gs.default_PrestaAPIV:
            return self.connector.get(resource, search_filter)

        elif 'V3' in gs.default_PrestaAPIV:
            response = self.connector.get(resource=resource,
                                           resource_id=resource_id,
                                           resource_ids=resource_ids,
                                           search_filter=search_filter,
                                           display=display,
                                           sort=sort,
                                           limit=limit,
                                           schema=schema,
                                           io_format=io_format)

            if resource == 'categories':
                return response['categories'][0] if resource_id else response['categories']
            
            elif resource == 'languages':
                return response['languages'][0] if resource_id else response['languages']
            # Add handling for other resources here
            
            else:
                return response

    
    def add(self, resource: str = None, data: dict = None, resource_id: int |  str = None,
            resource_ids: int | str | List[str, tuple] = None, search_filter: dict = None,
            display: str | list = 'full', io_format: str = 'JSON') -> dict:
        """!
         Add data to the API.
        @param resource `str` : API resource.
        @param data `dict` : Data to add.
        @returns `dict` : Query result.
        """

        if 'prestapyt' in gs.default_PrestaAPIV:
            return self.connector.add(resource, data)

        elif 'V3' in gs.default_PrestaAPIV:
            return self.connector.add(resource=resource, data=data)


    def upload_image(self, resource: str, resource_id: int |  str, local_file_path: str) -> None:
        """!
         Upload an image to the API.
        @param resource `str` : API resource.
        @param resource_id `int|str` : Resource identifier.
        @param local_file_path `str` : Path to the local image file.
        @returns None
        """
        if 'prestapyt' in gs.default_PrestaAPIV:
            # Code for uploading an image using prestapyt
            pass
        elif 'V1' in gs.default_PrestaAPIV:
            # Code for uploading an image using PrestaAPIV1
            pass
        elif 'V3' in gs.default_PrestaAPIV:
            return self.connector.create_binary(resource, resource_id, local_file_path)

