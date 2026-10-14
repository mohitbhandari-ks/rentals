import frappe

@frappe.whitelist()
def get_emoji():
    return "😀"

def send_payemt_reminder():
    pass

def get_query_conditions_for_vehicle_custom(user):

    return "name = 2"