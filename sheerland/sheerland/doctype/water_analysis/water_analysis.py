# -*- coding: utf-8 -*-
# Copyright (c) 2017, sheerland and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class WaterAnalysis(Document):
	def on_update(self):
		field = frappe.get_doc("Field",self.field_name)
		
		field.collection_datetime = self.collection_datetime
		field.laboratory_testing_datetime = self.laboratory_testing_datetime
		field.result_datetime = self.result_datetime
		field.type_of_sample = self.type_of_sample
		field.container = self.container
		field.origin = self.origin
		field.collection_temperature = self.collection_temperature
		field.storage_temperature = self.storage_temperature
		field.appearance = self.appearance
		field.person_responsible = self.person_responsible
		field.save()
