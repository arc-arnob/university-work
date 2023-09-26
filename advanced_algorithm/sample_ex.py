from typing import List, Any

from mip import *


def solve():
    # N Stores, M Customers
    n_of_stores = 4
    n_of_customers = 3
    cost_matrix = [[3, 2.5, -1], [4, -1, 3], [-1, 3, 6], [2.5, 3, -1]]
    optimizer = Model()

    # Inputs
    # c_ij
    cost_of_supplying_customer_j_from_store_i = cost_matrix
    # [[optimizer.add_var(var_type=INTEGER) for j in range(n_of_customers)] # for i in range(n_of_stores)]

    # s_i
    supply_from_store_i = [1200, 500, 600, 1500] # [optimizer.add_var(var_type=INTEGER) for i in range(n_of_stores)]

    # d_j
    demand_from_customer_j = [1800, 700, 900]  # [optimizer.add_var(var_type=INTEGER) for j in range(n_of_customers)]

    # Decision Variables
    # (x_ij)
    amount_supplied_from_store_i_to_customer_j = [[optimizer.add_var(var_type=INTEGER) for j in range(n_of_customers)]
                                                  for i in range(n_of_stores)]

    # Objective Function
    optimizer.objective = minimize(xsum(cost_of_supplying_customer_j_from_store_i[i][j]
                                        * amount_supplied_from_store_i_to_customer_j[i][j]
                                        for j in range(n_of_customers)
                                        for i in range(n_of_stores)
                                        )
                                   )
    # Constraints
    for i in range(n_of_stores):
            optimizer += xsum(amount_supplied_from_store_i_to_customer_j[i][j] for j in range(n_of_customers)) <= supply_from_store_i[i]

    for i in range(n_of_stores):
        for j in range(n_of_customers):
            store_supplies_are = amount_supplied_from_store_i_to_customer_j[i]
            optimizer += xsum(store_supplies_are[j]) == demand_from_customer_j[j]

    optimizer.optimize()
    return optimizer.objective_value


if __name__ == '__main__':
    print(solve())
