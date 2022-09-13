import requests
import ssl
from lxml import etree

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://dict.deepl.com/chinese-english/search?ajax=1&source=chinese&onlyDictEntries=1&translator=dnsof7h3k2lgh3gda&kind=full&eventkind=change&forleftside=true&il=en'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

looking_for = input('请输入您想查询的文字：')

form_data = {
    'query': f'{looking_for}'
}

response = requests.post(url, params=form_data, headers=headers)
tree = etree.HTML(response.content)
words_class = tree.xpath('//span[@class="tag_wordtype"]//text()')
words = tree.xpath('//h3[@class="translation_desc"]/span/a[1]/text()')


def get_result(result_dict: dict):
    for i in range(len(words_class)):
        result_dict[str(words_class[i])] = str(words[i])

    if len(words) - len(words_class) > 0:
        result_dict['词组'] = list(map(str, words[len(words_class):]))
    return result_dict


print('翻译结果为：\n', get_result({}))
