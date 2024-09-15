## \file ../src/prestashop/_experiments/suppliers/hb/test_2_hb_get_site_structure.py
## \file src/prestashop/_experiments/suppliers/hb/test_2_hb_get_site_structure.py
import requests
from bs4 import BeautifulSoup
import re
import json

import header
from header import pprint,  logger

def get_links_with_text(url):


    logger.info(f"URL {url}")
    response = requests.get(url)
    logger.info(f"response: {jprint(response)}")
    
    # Проверяем успешность запроса
    if response.status_code != 200:
        return {}
    
    # Создаем объект BeautifulSoup для анализа содержимого страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим все ссылки на странице
    links = soup.find_all('a', href=True)
    

    # Создаем словарь, где ключ - это ссылка, а значение - текст ссылки
    links_with_text = {link['href']: link.text.strip() for link in links if re.match(r'^https://hbdeadsea\.co\.il/product-category', link['href'])}
    
    logger.info(f"links: {links_with_text}")
    return links_with_text


def recursive_crawl(url, depth):
    if depth == 0:
        return {}
    
    links_with_text = get_links_with_text(url)
    all_links_with_hierarchy = {}
    for link, text in links_with_text.items():
        # Рекурсивно вызываем функцию для каждой найденной ссылки на указанной глубине
        child_links = recursive_crawl(link, depth - 1)
        logger.info(f"level: {depth}")
        all_links_with_hierarchy[text] = {
            "text": text,
            "children": child_links
        }
    
    return all_links_with_hierarchy

def save_json_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def start():
    # Укажите URL, с которого начнется сбор ссылок
    starting_url = 'https://hbdeadsea.co.il'
    
    # Укажите глубину рекурсии (сколько уровней ссылок будет рекурсивно собрано)
    depth = 4
    
    # Запускаем сбор ссылок рекурсивно
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    # Сохраняем JSON-файлы для каждого верхнего узла
    for top_node_text, top_node_data in all_links_with_hierarchy.items():
        file_name = f"{top_node_text}.json"
        save_json_file(top_node_data, file_name)
        logger.warning(f"Был создан файл {file_name}")

if __name__ == '__main__':
    start()

start()
