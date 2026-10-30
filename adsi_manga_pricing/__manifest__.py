{
    "name": "ADSI Manga Pricing",
    "summary": "Manga purchase costs, sale prices and margin analysis",
    "description": """
Manage manga purchase costs, sale prices and calculated margins.
Enforce pricing rules and provide a pivot analysis of manga margins.
    """,
    "author": "ADSI-Tech",
    "version": "20.0.1.0.0",
    "category": "Services",
    "license": "LGPL-3",
    "depends": [
        "base",
        "managatheque",
    ],
    "data": [
        "views/manga_pricing_views.xml",
        "views/manga_pricing_menus.xml",
    ],
    "application": False,
    "installable": True,
}