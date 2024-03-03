from Assignment import Assignment
from DateFormat import date_value

def sort_assignment(all_assignment: list[Assignment]) -> list[Assignment]:
    """
    This function sorts all assignment lists by due date order.
    """
    # Iterate through each list index
    for i, current in enumerate(all_assignment):
        j = i - 1
        # Go back through the list to find next smallest
        while j >= 0 and date_value(all_assignment[j].due_date) > date_value(current.due_date):
            # Swap element backwards
            all_assignment[j+1] = all_assignment[j]
            j -= 1
        # Swap that element into the target index
        all_assignment[j+1] = current
    return all_assignment