from odoo import fields, models


class HelpdeskTicketSubject(models.Model):
    _name = "helpdesk.ticket.subject"
    _description = "Asunto de Ticket de Mesa de Ayuda"
    _order = "name"

    name = fields.Char(string="Nombre", required=True, translate=False)
    active = fields.Boolean(default=True)

    _name_uniq = models.Constraint(
        "UNIQUE(name)",
        "El asunto ya existe.",
    )
