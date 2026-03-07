from odoo import fields, models


class HelpdeskTicketTag(models.Model):
    _name = "helpdesk.ticket.tag"
    _description = "Etiqueta de Ticket de Mesa de Ayuda"
    _order = "sequence,id"

    sequence = fields.Integer(default=10)
    name = fields.Char(translate=True)
    color = fields.Integer(string="Índice de color")
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Compañía",
        default=lambda self: self.env.company,
    )
