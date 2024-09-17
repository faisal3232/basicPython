# Creating a nested dictionary
family = {
    'parent1': {
        'name': 'John',
        'age': 45,
        'children': {
            'child1': {'name': 'Chris', 'age': 20},
            'child2': {'name': 'Alex', 'age': 18}
        }
    },
    'parent2': {
        'name': 'Jane',
        'age': 42,
        'children': {
            'child1': {'name': 'Sam', 'age': 16}
        }
    }
}

# Accessing values
print(family['parent1']['name'])  # Output: John
print(family['parent1']['children']['child1']['name'])  # Output: Chris

# Modifying values
family['parent2']['children']['child1']['age'] = 17

# Adding a new entry
family['parent1']['children']['child3'] = {'name': 'Taylor', 'age': 14}

# Iterating through nested dictionaries
for parent, details in family.items():
    print(f"Parent: {details['name']}, Age: {details['age']}")
    for child, child_details in details['children'].items():
        print(f"  Child: {child_details['name']}, Age: {child_details['age']}")

# Output:
# Parent: John, Age: 45
#   Child: Chris, Age: 20
#   Child: Alex, Age: 18
#   Child: Taylor, Age: 14
# Parent: Jane, Age: 42
#   Child: Sam, Age: 17
