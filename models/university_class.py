# -*- coding: utf-8 -*-
from odoo import models, fields

class university_class (models.Model):   
    _name = 'university.class'
    _description = 'Classe Universitaire'

    name = fields.Char(string='Nom de la classe', required=True)
    niveau = fields.Selection([
        ('l1', 'Licence 1'),
        ('l2', 'Licence 2'),
        ('l3', 'Licence 3'),
        ('m1', 'Master 1'),
        ('m2', 'Master 2'),
    ], string='Niveau', required=True)
    effectif = fields.Integer(string='Nombre d\'étudiants', default=0)

