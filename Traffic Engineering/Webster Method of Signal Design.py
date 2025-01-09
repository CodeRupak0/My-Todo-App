import math

def calculate_cycle_length(saturation_flows, vehicle_volumes, lost_time):
    """optimal cycle length using Webster's formula."""
    y = sum(vehicle_volumes[i] / saturation_flows[i] for i in range(len(vehicle_volumes)))  # Calculation of critical flow ratios
    if y >= 1:
        raise ValueError("Critical volume exceeds capacity. Adjust intersection design.")

    cycle_length = math.ceil((1.5 * lost_time + 5) / (1 - y))
    return cycle_length


def calculate_green_time(cycle_length, saturation_flows, vehicle_volumes, lost_time):
    """Allocation of green times for each phase based on traffic volumes and saturation flows."""
    y=[]
    sum_y=0
    y = [vehicle_volumes[i] / saturation_flows[i] for i in range(len(vehicle_volumes))]
    sum_y = sum(y)

    effective_green_times = [(cycle_length - lost_time) * y[i] / sum_y for i in range(len(y))]

    green_times = [math.ceil(g) for g in effective_green_times]
    return green_times



approaches = ["North-South", "East-West"]
saturation_flows = [1800, 1700]                                     # vehicles per hour
vehicle_volumes = [800, 600]                                        # vehicles per hour
num_phases = len(approaches)
All_Red_Time= 3                                                     # seconds
lost_time = 2 * num_phases + All_Red_Time                           # seconds per phase


# Calculation of cycle length
try:
    optimal_cycle_length = calculate_cycle_length(saturation_flows, vehicle_volumes, lost_time)
    print(f"Optimal Cycle Length: {optimal_cycle_length} seconds")

    # Calculate green times for each phase
    green_times = calculate_green_time(optimal_cycle_length, saturation_flows, vehicle_volumes,lost_time)
    for i, approach in enumerate(approaches):
        print(f"Green Time for {approach}: {green_times[i]} seconds")

    # Signal timing plan
    print("\nSignal Timing Plan:")
    for i, approach in enumerate(approaches):
        print(f"{approach}: Green = {green_times[i]}s, Yellow = 3s, Red = {optimal_cycle_length - green_times[i] - 3}s")

except ValueError as e:
    print(e)
