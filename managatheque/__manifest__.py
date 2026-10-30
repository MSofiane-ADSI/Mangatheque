{
    'name': "managatheque",

    'summary': "Application de gestion des mangas",

    'description': """
cette appliactio vous permet de gérer tous vos mangas.
    """,

    'author': "Information sans complexey",
    'website': "https://www.informationsanscomplex.com",

     
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/20.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',   


    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        "security/manga_security.xml",
        "security/ir.access.csv",
        "wizard/note.xml",
        "views/views.xml",
        "views/templates.xml",
        "views/manga.xml",
        'report/report_manga.xml',     # ← ajouter cette ligne


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

