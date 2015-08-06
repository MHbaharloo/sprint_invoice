# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging


class Sprint(models.Model):
     _name = 'sprint_invoice.sprint'

     price = fields.Integer()
     project_id = fields.Many2one('sprint_invoice.project', string='Project', select=1)
     name = fields.Text()


class Project(models.Model):
    _name = 'sprint_invoice.project'

    company_id = fields.Many2one('res.company', string='Company', select=1)
    name = fields.Char()
    sprints = fields.One2many('sprint_invoice.sprint', 'project_id', "Project's sprint")
    date_invoice = fields.Date(string='Invoice Date')
    partner_id = fields.Many2one('res.partner', string='Partner', select=1)
    account_id = fields.Many2one('account.account', string='Account', select=1)
    price_unit = fields.Integer(compute='_sprint_total_price')
    axant_project = fields.Char()

    _defaults = {
        'axant_project' : "Axant Project",
    }

    @api.depends('sprints')
    def _sprint_total_price(self):
        for rec in self:
            rec.price_unit = sum([s.price for s in rec.sprints]) if rec.sprints else 0

    def make_invoices(self, cr, uid, ids, context=None):
        project_obj = self.pool.get('sprint_invoice.project')

        #for sale_order in order_obj.browse(cr, uid, context.get(('active_ids'), []), context=context):
            #logging.warning(sale_order.name)

        project = project_obj.browse(cr, uid, context.get(('active_ids'), []), context=context)

        #product = product_obj.browse(cr, uid,ids)
        #test = product_obj.search(cr, uid, [('name', '=', "dd")])
        #for prod in product:
            #logging.warning(prod.price)

        pp_id = self.pool.get('product.product')
        pr_id = pp_id.search(cr, uid, [('name', '=', "Axant Project")])

        """pr_id = self.pool.get('product.product').create(cr,uid,{
            'name' : "Axant Project",
        })
        logging.warning(pr_id)"""

        invoice_id = self.pool.get('account.invoice').create(cr,uid,{
            'partner_id' : project.partner_id.id,
            'account_id' : project.account_id.id,
            'date_invoice' : project.date_invoice,
        })

        for s in project.sprints:
            invoice_line_id = self.pool.get('account.invoice.line').create(cr,uid,{
                'name' : s.name,
                'price_unit' : s.price,
                'invoice_id' : invoice_id,
                'product_id' : pr_id[0],
            })



