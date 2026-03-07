from odoo import api, fields, models


class HelpdeskTicketStage(models.Model):
    _name = "helpdesk.ticket.stage"
    _description = "Etapa de Ticket de Mesa de Ayuda"
    _order = "sequence, id"

    name = fields.Char(string="Nombre de etapa", required=True, translate=True)
    description = fields.Html(translate=True, sanitize_style=True)
    sequence = fields.Integer(default=1)
    active = fields.Boolean(default=True)
    unattended = fields.Boolean()
    closed = fields.Boolean()
    close_from_portal = fields.Boolean(
        help="Mostrar botón en el formulario del portal para permitir cerrar el ticket "
        "con esta etapa como destino."
    )
    mail_template_id = fields.Many2one(
        comodel_name="mail.template",
        string="Plantilla de correo",
        domain=[("model", "=", "helpdesk.ticket")],
        help="Si se configura, se enviará un correo electrónico al "
        "cliente cuando el ticket "
        "llegue a esta etapa.",
    )
    fold = fields.Boolean(
        string="Plegado en Kanban",
        help="Esta etapa se pliega en la vista kanban "
        "cuando no hay registros en esa etapa "
        "para mostrar.",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Compañía",
        default=lambda self: self.env.company,
    )
    team_ids = fields.Many2many(
        comodel_name="helpdesk.ticket.team",
        string="Equipos de mesa de ayuda",
        help="Equipo específico que usa esta etapa. Si está vacío, todos los equipos podrán usarla",
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )

    @api.onchange("closed")
    def _onchange_closed(self):
        if not self.closed:
            self.close_from_portal = False
