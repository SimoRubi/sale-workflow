# -*- coding: utf-8 -*-
# © 2016 ACSONE SA/NV <https://acsone.eu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import odoo.tests.common as common


class TestSaleOrderLineDescriptionChange(common.TransactionCase):
    def setUp(self):
        super(TestSaleOrderLineDescriptionChange, self).setUp()

        self.partner_obj = self.env['res.partner']

    def test_check_description(self):
        vals = {
            'name': 'p1@example.com',
            'groups': [
                'sale_order_line_description.'
                'group_use_product_description_per_so_line']
        }
        partner1 = self.order_line_obj.create(vals)

        vals = {
            'name': 'p2@example.com',
        }
        partner2 = self.order_line_obj.create(vals)

        body = 'this is the body'
        subject = 'this is the subject'
        recipients = partner1
        emails, recipients_nbr = \
            self.partner_obj._notify_send(body, subject, recipients)

        self.assertTrue(
            partner1.name in emails.body_html,
            'Partner name is not in the body of the mail')
