import json
import os.path

import scrapy
from scrapy import Request


class KsSpider(scrapy.Spider):
    name = 'ks'
    allowed_domains = ['wangxiao.cn']
    start_urls = ['http://ks.wangxiao.cn/']

    def parse(self, response, **kwargs):
        lis = response.xpath('//ul[@class="first-title"]/li')
        for li in lis:
            category = li.xpath('./p/span/text()').extract_first()
            hrefs = li.xpath('./div/a')
            for href in hrefs:
                major_name = href.xpath('./text()').extract_first()
                _major_href = href.xpath('./@href').extract_first()
                major_href = response.urljoin(_major_href).replace('TestPaper', 'exampoint')
                # print(category, '--->', major_name, '--->', major_href)
                yield Request(url=major_href, callback=self.parse_second, meta={
                    '类别': category,
                    '专业名': major_name
                })
                # return None  # 仅做测试

    def parse_second(self, response, **kwargs):
        category = response.meta['类别']
        major_name = response.meta['专业名']

        subject_hrefs = response.xpath('//div[@class="filter-item"]/a')
        for _subject_href in subject_hrefs:
            subject_href = response.urljoin(_subject_href.xpath('./@href').extract_first())
            subject_name = _subject_href.xpath('./text()').extract_first()
            # print(category, major_name, subject_href, subject_name)
            yield Request(url=subject_href, callback=self.parse_third, meta={
                '类别': category,
                '专业名': major_name,
                '科目': subject_name
            })
            # return None  # 仅做测试

    def parse_third(self, response, **kwargs):
        category = response.meta['类别']
        major_name = response.meta['专业名']
        subject_name = response.meta['科目']

        point_items = response.xpath('//ul[@class="section-point-item"]')
        if point_items:
            for item in point_items:
                sec_or_chaps = item.xpath('./ancestor::ul[@class="section-item" or @class="chapter-item"]')
                sec_or_chap_list = []
                for sec_or_chap in sec_or_chaps:
                    dirs = ''.join(sec_or_chap.xpath('./li[1]//text()').extract()).strip().replace(' ', '')
                    sec_or_chap_list.append(dirs)
                # print(sec_or_chap_list)
                file_path = os.path.join(category, major_name, subject_name, *sec_or_chap_list)
                file_name = ''.join(item.xpath('./li[1]//text()').extract()).strip().replace(' ', '')
                print('if内', file_path, file_name)

                questions_href = 'http://ks.wangxiao.cn/practice/listQuestions'
                top = item.xpath('./li[2]/text()').extract_first().strip().replace(' ', '').split('/')[1]
                data_sign = item.xpath('./li[3]/span/@data_sign').extract_first()
                data_subsign = item.xpath('./li[3]/span/@data_subsign').extract_first()
                data = {
                    'examPointType': '',
                    'practiceType': '2',
                    'questionType': '',
                    'sign': data_sign,
                    'subsign': data_subsign,
                    'top': top
                }
                yield Request(
                    url=questions_href,
                    method='POST',
                    body=json.dumps(data),
                    headers={
                        'Content-Type': 'application/json; charset=UTF-8'
                    },
                    meta={
                        '文件名': file_name,
                        '文件路径': file_path
                    },
                    callback=self.parse_forth
                )
                # return None  # 仅做测试
        else:
            chapter_items = response.xpath('//ul[@class="chapter-item"]')
            if chapter_items:
                for chapter_item in chapter_items:
                    file_name = ''.join(chapter_item.xpath('./li[1]//text()').extract()).strip().replace(
                        ' ', '')
                    file_path = os.path.join(category, major_name, subject_name)
                    print('else内', file_path, file_name)
                    questions_href = 'http://ks.wangxiao.cn/practice/listQuestions'
                    top = chapter_item.xpath('./li[2]/text()').extract_first().strip().replace(' ', '').split('/')[1]
                    data_sign = chapter_item.xpath('./li[3]/span/@data_sign').extract_first()
                    data_subsign = chapter_item.xpath('./li[3]/span/@data_subsign').extract_first()
                    data = {
                        'examPointType': '',
                        'practiceType': '2',
                        'questionType': '',
                        'sign': data_sign,
                        'subsign': data_subsign,
                        'top': top
                    }
                    yield Request(
                        url=questions_href,
                        method='POST',
                        body=json.dumps(data),
                        headers={
                            'Content-Type': 'application/json; charset=UTF-8'
                        },
                        meta={
                            '文件名': file_name,
                            '文件路径': file_path
                        },
                        callback=self.parse_forth
                    )
                    # return None  # 仅做测试

    def parse_forth(self, response, **kwargs):
        total_data = response.json()
        if not total_data:
            print('没有获取到json数据')
        file_name = response.meta['文件名']
        file_path = response.meta['文件路径']

        data = total_data['Data']  # data是一个list
        for question_type in data:  # question_type代表一类题型，如单选题、多选题、材料题等，是字典
            if not question_type['materials']:  # 如果没有材料题
                print('当前试卷没有材料题', file_path, file_name)
                questions = question_type['questions']  # questions是一个列表，包含了具体的题目
                for question in questions:  # question是具体的一个题目，是字典
                    question_content = question['content']  # question_content是题干，是字符串
                    question_analysis = question['textAnalysis']  # question_analysis是答案解析，是字符串
                    options = question['options']  # options是许多选项，是列表
                    if options:  # options不能是一个空列表
                        print('选项是:', options)
                        option_list, answer_list = self.parse_option(options)

                        # 开始组装一道题
                        question_info = question_content + '\n' + '\n'.join(
                            option_list) + '\n' + '正确答案: ' + ''.join(
                            answer_list) + '\n' + '答案解析: ' + question_analysis + '\n\n\n\n'
                        yield {
                            '文件名': file_name,
                            '文件路径': file_path,
                            '文件内容': question_info
                        }
                    else:
                        # 开始组装一道题
                        question_info = question_content + '\n' + '答案解析: ' + question_analysis + '\n\n\n\n'
                        yield {
                            '文件名': file_name,
                            '文件路径': file_path,
                            '文件内容': question_info
                        }
            else:
                print('当前试卷有材料题', file_path, file_name)
                material_questions = question_type['materials']  # material_questions是列表，代表许多材料题
                for material_question in material_questions:  # material_question是具体的一道材料题，是字典
                    material = material_question['material']['content']  # material是材料，是字符串
                    questions = material_question['questions']  # questions是材料题下的许多题目，是列表
                    question_content_list = []
                    for question in questions:  # question是本材料题下的一道题，是字典
                        question_content = question['content']  # question_content是题干，是str
                        question_analysis = question['textAnalysis']  # question_analysis是解析，是str
                        question_options = question['options']  # question_option是选项，是list
                        if question_options:  # question_options不能是一个空列表
                            option_list, answer_list = self.parse_option(question_options)
                            complete_question = question_content + '\n' + '\n'.join(
                                option_list) + '\n' + '正确答案: ' + ''.join(
                                answer_list) + '\n' + '答案解析: ' + question_analysis
                            question_content_list.append(complete_question)
                        else:  # question_options是一个空列表
                            complete_question = question_content + '\n' + '答案解析: ' + question_analysis
                            question_content_list.append(complete_question)

                    # 开始组装一道题
                    question_info = material + '\n\n' + '\n'.join(question_content_list) + '\n\n\n\n'
                    yield {
                        '文件名': file_name,
                        '文件路径': file_path,
                        '文件内容': question_info
                    }

    def parse_option(self, options: list):
        option_list = []
        answer_list = []
        if options:  # options不能是一个空列表
            for option in options:  # option是具体的一个选项，是字典
                option_content = option['content']  # option_content是选项内容，是字符串
                option_is_right = option['isRight']  # option_is_right是选项答案，是字符串
                option_name = option['name']  # option_name是选项名，是字符串

                option_list.append(option_name + '. ' + option_content)
                if option_is_right == 1:
                    answer_list.append(option_name)
            return option_list, answer_list
