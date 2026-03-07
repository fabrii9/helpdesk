from odoo import fields, models


class HelpdeskTicketStage(models.Model):
    _inherit = "helpdesk.ticket.stage"

    rating_mail_template_id = fields.Many2one(
        comodel_name="mail.template",
        string="Plantilla de correo de valoración",
        domain=[("model", "=", "helpdesk.ticket")],
        help="Si se configura, se enviará un correo al cliente "
        "con una encuesta de valoración cuando el ticket llegue a esta etapa.",
    )
