
import hr
import employees
import productivity
import contacts

manager = employees.Manager(1, 'Maryam', 3000)
manager.address = contacts.Address(
    '121 Admin Rd',
    'Concord',
    'NH',
    '03301'
)
secretary = employees.Secretary(2, 'Ali', 1500)
secretary.address = contacts.Address(
    '67 Paperwork Ave.',
    'Manchester',
    'NH',
    '03101'
)
sales_guy = employees.SalesPerson(3, 'Kiran', 1000, 250)
factory_worker = employees.FactoryWorker(2, 'Noman', 40, 15)
temporary_secretary = employees.TemporarySecretary(5, 'Rabia', 40, 9)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)