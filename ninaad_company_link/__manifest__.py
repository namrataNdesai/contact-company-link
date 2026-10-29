{
    'name': 'Contact Company Link',
    'version': '18.0.1.0.0',
    'summary': 'Create a new Odoo Company from an existing Contact in one click',
    'description': """
        Create Company from Contact
        ===========================
        Businesses often start with a single company and expand over time. When a new
        company has to be set up for an organisation that already exists as a contact,
        standard Odoo requires creating the company separately and linking it by hand.

        This module adds a **Create Company** action to Contacts, so an existing company
        contact can be turned into an Odoo company in one click.
    """,
    'author': 'Ninaad Global Pvt Ltd.',
    'website': 'https://www.ninaadglobal.com',
    'support': 'support@ninaadglobal.com',
    'depends': ['base', 'contacts'],
    'data': ['data/server_action.xml'],
    'images': ['static/description/screen_image.png'],
    'application': True,
    'installable': True,
    'auto_install': False,
    "license": "Other proprietary",
}
