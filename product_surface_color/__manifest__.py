# -*- coding: utf-8 -*-
{
    'name': "Surface Color Variant",

    'summary': """
        This module is display a custom images in product website  """,

    'description': """
        This module is display a custom images in product website  
    """,

    'author': "usvameria",
    'website': "https://usvameria.site",

    
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale_product_configurator', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_surface_color_variants_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
