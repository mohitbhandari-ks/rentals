# Copyright (c) 2026, BWH and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle_Custom(WebsiteGenerator):
	
	def before_save(self):
		self.set_title()

	def set_title(self):
		self.title = f"{self.make} {self.model}, {self.year}"