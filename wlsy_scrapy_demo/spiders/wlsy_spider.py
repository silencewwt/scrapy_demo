# -*- coding: utf-8 -*-
from scrapy import FormRequest, Request
from scrapy.spider import Spider
from ..items import *


class WlsySpider(Spider):
    name = 'wlsy'
    course_url = "http://wlsy.xidian.edu.cn/PhyEws/student/course.aspx"
    login_url = "http://wlsy.xidian.edu.cn/PhyEws/default.aspx?ReturnUrl=%2fphyEws%2fstudent%2fselect.aspx"
    login_form = {
        'login1$StuLoginID': '14130130295', 'login1$StuPassword': '14130130295', 'login1$UserRole': 'Student',
        'login1$btnLogin.x': '18', 'login1$btnLogin.y': '8', '__VIEWSTATE': '/wEPDwUKMTEzNzM0MjM0OWQYAQUeX19Db250cm9sc1'
        'JlcXVpcmVQb3N0QmFja0tleV9fFgEFD2xvZ2luMSRidG5Mb2dpbtOya8lT1fzi71oyQgc7Hv73+yvb',
        '__EVENTVALIDATION': '/wEWBwLprev4CQKckJOGDgKD8YXRCQLJ5dDDBAKVx8n1CQKytMi0AQKcg465CqY+2XXD/g4v/g6yTYN6r/N0zBZo'
    }

    def start_requests(self):
        return [FormRequest(self.login_url, formdata=self.login_form, callback=self.yield_course_page)]

    def yield_course_page(self, response):
        yield Request(self.course_url, callback=self.parse_course_page)

    def parse_course_page(self, response):
        course_id_list = response.xpath("//option/@value").extract()
        form_data_list = response.xpath("//input[@type='hidden']")
        form_data = {}
        for data in form_data_list:
            form_data[data.xpath('@name').extract()[0]] = data.xpath('@value').extract()[0]
        form_data['__EVENTTARGET'] = 'plan1$ExpeList'
        for course_id in course_id_list:
            form_data['plan1$ExpeList'] = course_id
            yield FormRequest(self.course_url, callback=self.parse_course, formdata=form_data)

    def parse_course(self, response):
        tr_list = response.xpath("//table[@id='plan1_PlanGrid']/tr")
        course = Course()
        print course.items()
        course['name'] = response.xpath("//option[@selected='selected']/text()").extract()[0]
        course['course_id'] = response.xpath("//option[@selected='selected']/@value").extract()[0]
        course['data'] = []
        for tr in tr_list[1:]:
            row_text_list = tr.xpath("td/span/text()").extract()
            course['data'].append(row_text_list)
        return course