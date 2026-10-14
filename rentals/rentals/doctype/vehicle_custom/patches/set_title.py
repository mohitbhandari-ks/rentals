import frappe


def execute():
	for doc in frappe.get_all("Vehicle_Custom"):
		vehicle = frappe.get_doc("Vehicle_Custom", doc.name)
		vehicle.set_title();
		vehicle.title = f"{vehicle.make} {vehicle.model}, {vehicle.year}"
		vehicle.save()
	frappe.db.commit()