from admins import Admin, Privileges

eric = Admin('eric', 'matthes', 'e_mattches', 'e_mattches@example.com', 'alaska')
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]

eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
