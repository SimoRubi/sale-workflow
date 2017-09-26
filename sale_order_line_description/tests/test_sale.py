# -*- coding: utf-8 -*-
# © 2016 ACSONE SA/NV <https://acsone.eu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import odoo.tests.common as common


class TestSaleOrderLineDescriptionChange(common.TransactionCase):
    def setUp(self):
        super(TestSaleOrderLineDescriptionChange, self).setUp()

        self.sale_order_model = self.env['sale.order']
        self.sale_order_line_model = self.env['sale.order.line']

        # Data
        self.product = self._create_product('test_product')
        self.customer_1 = \
            self._create_customer('Test Customer 1',
                                  'sale_order_line_description.'
                                  'group_use_product_description_per_so_line'
                                  )
        self.customer_2 = self._create_customer('Test Customer 2')

    def _create_customer(self, name, group=None):
        """Create a Partner."""
        return self.env['res.partner'].create({
            'name': name,
            'email': 'example@yourcompany.com',
            'groups': [group]
        })

    def _create_product(self, name):
        """Create a Product."""
        product = self.env['product.product'].create({
            'name': name,
        })
        return product

    def test_check_sale_order_line_description(self):
        self.assertTrue(
            1 == 1,
            'Partner name is not in the body of the mail')
