## \file ../src/prestashop/_experiments/suppliers/hb/____experiments_6_lxml_get_unique_links_DFS_algoryphm.py
## \file src/prestashop/_experiments/suppliers/hb/____experiments_6_lxml_get_unique_links_DFS_algoryphm.py
""" FROM openAI:
Если вам необходимо углубиться до глубины depth = 5, то вам понадобится оптимизировать рекурсивный алгоритм,
чтобы избежать переполнения стека вызовов и ускорить процесс сбора ссылок.

Вместо рекурсивного подхода можно использовать итеративный (нерекурсивный) алгоритм для обхода и сбора ссылок. 
Одним из наиболее распространенных алгоритмов обхода в глубину (DFS) является алгоритм с использованием стека.


В этом коде мы используем стек для хранения URL'ов, которые нужно обработать, и обходим сайт 
с использованием итеративного подхода вместо рекурсивного. При этом глубина обхода ограничивается заданным значением depth.

Теперь вы можете углубиться до глубины depth = 5 без опасения переполнения стека вызовов.
"""


"   ЭТОТ ТЕСТ  НЕ РАБОТАЕТ  "                                                                                                                                                          

from math import log
import header
from header import pprint,  logger
import requests
import json
from lxml import etree
from urllib.parse import urlparse

def get_path_from_root(url:str):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    root_path = '/'.join(path_parts[:3])  # Assuming that the root path is always the first 3 parts of the URL
    return root_path

def get_links(response, visited_links: set, xpath: str) -> (set):
    url = response.url
    if url in visited_links:
        return set(), None

    logger.debug(f"depth: {depth}")

    # Отмечаем URL как просмотренный
    visited_links.add(url)

    # Создаем объект lxml для анализа содержимого страницы
    lxml_tree = etree.HTML(response.text)

    # Выполняю поиск ссылок на странице, исключая адрес "https://hbdeadsea.co.il/product-category/allproducts/" и ссылки с классом "swiper-slide-inner"

    
    links = lxml_tree.xpath(f'{xpath}')

    return links


    if not 'unique_links' in locals():
        unique_links = set()

    link_text = None

    for link in links:
        href = link.attrib['href']
        try:
            link_text = link.attrib['title'].strip()
        except KeyError:
            link_text = link.text
            if not link_text or link_text == '\n':
                continue
        except Exception as ex:
            print(f"Error: {ex}\nLink: {link}")
            continue

        if href not in visited_links:  # Check if the URL has already been visited
            unique_links.add((href, link_text))
            visited_links.add(href)

    for link in links_main_menu_with_subs:
        href = link.attrib['href']
        children = get_unique_links(requests.get(href),visited_links)
        unique_links.add((href, children))


    return unique_links, link_text

def recursive_crawl(url: str, depth:int, visited_links:set) -> dict:
    if depth == 0:
        return {}

    response = requests.get(url)
    unique_links, link_text = get_links(response, visited_links)

    current_node_data = {}
    for href, name in unique_links:
        link_hierarchy = href.replace(url, "").rstrip("/").split("/")
        current_dict = current_node_data
        for part in link_hierarchy:
            current_dict = current_dict.setdefault(part, {})
        current_dict["URL"] = href
        if name is not None:
            current_dict["name"] = name
        current_dict["children"] = recursive_crawl(href, depth - 1, visited_links)

    return current_node_data

def save_json_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def is_root_category(url):
    # Check if the URL has only one subfolder after 'https://hbdeadsea.co.il/product-category/'
    path = url.replace('https://hbdeadsea.co.il/product-category/', '').rstrip('/')
    return len(path.split('/')) == 1

def process_top_level_categories(root_url:str , depth:int):
    visited_links = set()
    response = requests.get(root_url)

    xpath_link_subs = "//a[@href and starts-with(@href, '{url}') and not(contains(@href, 'allproducts/')) and not(contains(@class, 'swiper-slide-inner'))]"
    xpath_link_main_menu_with_subs = "//a[@class='dropdown-toggle menu-link' and not(contains(@href, 'allproducts/'))]/following-sibling::ul[@class='dropdown-menu']//a[starts-with(@href, '{url}') and not(contains(@href, 'allproducts/'))]"
    xpath_link_main_menu_wo_subs = "//a[@class='menu-link']"


    unique_links, link_text = get_unique_links(response, visited_links, xpath_link_main_menu_wo_subs)

    for url, link_text in unique_links:
        if is_root_category(url):
            visited_links.remove(url)
            children_data = recursive_crawl(url, depth, visited_links)
            root_path = get_path_from_root(root_url)
            save_json_file(children_data, f"{url('/')[-1]}_depth{depth}.json")

if __name__ == '__main__':
    # Укажите URL, с которого начнется сбор ссылок
    root_url = 'https://hbdeadsea.co.il/product-category'

    # Укажите глубину рекурсии (сколько уровней ссылок будет рекурсивно собрано)
    depth = 2

    # Обработка корневой категории, если ее URL имеет вид 'https://hbdeadsea.co.il/product-category/{sub_category}/'
    process_top_level_categories(root_url, depth)

