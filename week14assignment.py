def create_staff_dict(staff_list):

    return {each_dict['emp_id']: each_dict['department'] for each_dict in staff_list}


def audit_submissions(staff_dict, submitted_ids):
    
    staffs_set = set(key for key in staff_dict)
    submitted_set = set(submitted_ids)

    missing_timesheets = staffs_set - submitted_set
    invalid_ids = submitted_set - staffs_set

    return missing_timesheets, invalid_ids


def format_reminders(staff_dict, missing_set):
    result = []
    for emp_id in missing_set:
        dept = staff_dict[emp_id]
        msg = f"REMINDER: Staff #{emp_id} ({dept})"
        result.append(msg)
    return result


staff = [
    {'emp_id': 101, 'department': "Sales"},
    {'emp_id': 102, 'department': "IT"},
    {'emp_id': 103, 'department': "HR"}
]

submitted = [101, 103, 500]

structured_staff_dict = create_staff_dict(staff)
missing_timesheets, invalid_ids = audit_submissions(structured_staff_dict, submitted)
reminders_list = format_reminders(structured_staff_dict, missing_timesheets)

print("Missing Timesheets:", missing_timesheets)
print("Invalid IDs:", invalid_ids)
print('Report:', reminders_list)