# -*- coding: utf-8 -*-
from odoo import models, fields

class Teacher_class(models.Model):
    _name = 'emploi.enseignant'
    _description = 'enseignants universitaire'

    name = fields.Char(
        string="nom complet", required=True,
    )
    email = fields.Char(
        string="e-mail", required=True,
    )
    phone = fields.Char(string='Téléphone', required=True)
    department = fields.Char(string='Département', required=True)
    # subject_ids = fields.One2many('emploi.matiere', 'enseignant_id', string='Matières')