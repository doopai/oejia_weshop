# -*- coding: utf-8 -*-

from odoo import models, fields


class Province(models.Model):

    _name = 'oe.province'
    _description = u'省份'

    name = fields.Char('名称')
    child_ids = fields.One2many('oe.city', 'pid', string='市')

    def init(self):
        from ..data.oe_province_datas import init_sql
        self.env.cr.execute(init_sql)
