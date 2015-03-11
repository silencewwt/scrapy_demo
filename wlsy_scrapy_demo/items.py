# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class Course(Item):
    name = Field()
    course_id = Field()
    data = Field()


class Arrangement(Item):
    name = Field()
    capacity = Field()
    classroom = Field()
    teaching_material = Field()
    remark = Field()
    selectable = Field()