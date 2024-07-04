import os

def check_folders():
    assets_path = './assets'
    data_path = './data'
    users_path = data_path + '/users'
    incomes_path = data_path + '/incomes'
    expenses_path = data_path + '/expenses'
    fixed_cost_path = data_path + '/fixed_cost'
    budgets_path = data_path + '/budgets'

    if not os.path.exists(assets_path):
        os.makedirs(assets_path)
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    if not os.path.exists(users_path):
        os.makedirs(users_path)
    if not os.path.exists(incomes_path):
        os.makedirs(incomes_path)
    if not os.path.exists(expenses_path):
        os.makedirs(expenses_path)
    if not os.path.exists(fixed_cost_path):
        os.makedirs(fixed_cost_path)
    if not os.path.exists(budgets_path):
        os.makedirs(budgets_path)

if __name__ == '__main__':
    check_folders()