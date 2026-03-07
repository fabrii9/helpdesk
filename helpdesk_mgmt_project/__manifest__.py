# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Proyecto de Mesa de Ayuda",
    "summary": "Agregar la opción de seleccionar proyecto en los tickets.",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "category": "After-Sales",
    "author": "PuntSistemes S.L.U., " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/helpdesk",
    "depends": ["helpdesk_mgmt", "project"],
    "data": [
        "views/helpdesk_ticket_view.xml",
        "views/helpdesk_ticket_team_view.xml",
        "views/project_view.xml",
        "views/project_task_view.xml",
        "views/project_milestone.xml",
    ],
    "development_status": "Production/Stable",
    "auto_install": True,
}
