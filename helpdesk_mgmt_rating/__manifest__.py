{
    "name": "Valoración de Mesa de Ayuda",
    "summary": """
        Este módulo permite al cliente valorar la asistencia recibida
        en un ticket.
        """,
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "author": "Domatix, Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/helpdesk",
    "category": "After-Sales",
    "depends": ["helpdesk_mgmt", "rating"],
    "data": [
        "data/helpdesk_data.xml",
        "views/helpdesk_ticket_menu.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_stage_views.xml",
    ],
    "installable": True,
}
