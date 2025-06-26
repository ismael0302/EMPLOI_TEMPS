# -*- coding: utf-8 -*-
{
    'name': 'Gestion Emploi du Temps',
    'version': '1.0',
    'sequence': '1',
    'category': 'Education',
    'summary': "Module de gestion d\'emploi du temps",
    'author': 'Ismael',
    'depends': ['base'],
    'data': [
        'security\ir.model.access.csv',
        # 'views/emploi_temps_views.xml',
        'views/university_class_views.xml',
        'views/teacher_views.xml',

    ],
    'installable': True,
    'application': True,
}
