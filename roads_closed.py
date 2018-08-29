from bs4 import BeautifulSoup

from get_html import get_html

url = 'http://mosday.ru/news/tags.php?roadsclosed'

def get_road_restrictions():
    """Return message about closed roads"""
    html = get_html(url)

    if html:

        bs = BeautifulSoup(html, 'html.parser')

        movement_restriction_message = ''
        for item in bs.find_all('font', style='font-size:16px', size='3')[:5]:
            text = item.text
            href = item.find('a')
            href = 'http://mosday.ru/news/' + href.get('href')
            movement_restriction_message += text + '\n' + href + '\n'
        return movement_restriction_message
    else:
        return 'Failed to get_html'
