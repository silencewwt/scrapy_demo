# -*- coding: utf-8 -*-
import json
from items import *


class WlsyScrapyDemoPipeline(object):
    def __init__(self):
        self.course_file = open('course.json', 'w')
        self.arrangement_file = open('arrangement.json', 'w')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        print(item)
        if isinstance(item, Course):
            self.course_file.write(line)
        elif isinstance(item, Arrangement):
            self.arrangement_file.write(line)
        return item
