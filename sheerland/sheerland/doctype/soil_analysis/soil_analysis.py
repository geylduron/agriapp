# -*- coding: utf-8 -*-
# Copyright (c) 2017, sheerland and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SoilAnalysis(Document):
	
	def on_update(self):
		field = frappe.get_doc("Field",self.field_name)
		
		field.soil_analysis_date = self.soil_analysis_date
		field.texture = self.texture
		field.moisture = self.moisture
		field.acidity = self.acidity
		field.nitrogen = self.nitrogen
		field.phosphorus = self.phosphorus
		field.potassium = self.potassium
		field.calcium = self.calcium
		field.sodium = self.sodium
		field.chlorine = self.chlorine
		field.magnesium = self.magnesium
		field.sulfur = self.sulfur
		field.iron = self.iron
		field.copper = self.copper
		field.zinc = self.zinc
		field.save()
