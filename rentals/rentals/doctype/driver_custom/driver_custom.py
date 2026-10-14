# Copyright (c) 2026, BWH and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver_Custom(Document):
	def before_insert(self):
		self.full_name = f"{self.first_name} {self.last_name}"