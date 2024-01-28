import heapq


def min_cable_costs(cable_lengths):
    heapq.heapify(cable_lengths)
    total_cost = 0

    while len(cable_lengths) > 1:
        cable_A = heapq.heappop(cable_lengths)
        cable_B = heapq.heappop(cable_lengths)

        connection_cost = cable_A + cable_B
        total_cost += connection_cost

        heapq.heappush(cable_lengths, connection_cost)

    return total_cost


cable_lengths = [10, 2, 4, 1]
result = min_cable_costs(cable_lengths)
print(f"Мінімальні витрати: {result}")
