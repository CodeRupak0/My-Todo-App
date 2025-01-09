import time


# Function to calculate pressure for each approach
def calculate_pressure(inflow, outflow):
    Pressure = inflow - outflow
    return Pressure


# Function to dynamically allocate green time based on Max pressure control principle.
def allocate_green_time(approaches, inflows, outflows, cycle_length, min_green, max_green):
    total_pressure=0
    pressures=[]
    for i in range(len(approaches)):
        pressures.append(calculate_pressure(inflows[i], outflows[i])) #defined as lists for approaches

    # Normalize pressures to allocate green time
    for p in pressures:
        total_pressure = total_pressure+int(p)

    green_times = []

    for p in pressures:
        if total_pressure == 0:
            green_time = min_green
        else:
            green_time = max(min_green, min(max_green, (p / total_pressure) * (cycle_length - len(approaches) * 3)))
        green_times.append(int(green_time))

    return green_times




approaches = ["Northbound", "Southbound", "Eastbound", "Westbound"]
cycle_length = 120      # Total cycle length in seconds
min_green = 10          # Minimum green time in seconds
max_green = 60          # Maximum green time in seconds

inflows = [500, 300, 400, 250]      # Vehicles per hour
outflows = [200, 100, 150, 100]     # Vehicles per hour

# Simulating one cycle of adaptive signal control
print("Adaptive Signal Control Simulation:")
green_times = allocate_green_time(approaches, inflows, outflows, cycle_length, min_green, max_green)

for i, approach in enumerate(approaches):
    print(f"Approach {approach}: Green Time = {green_times[i]} seconds")

# Simulate a full signal cycle
print("\nSimulated Signal Cycle:")
for i, approach in enumerate(approaches):
    print(f"Approach {approach}:")
    print(f"  Green: {green_times[i]} seconds")
    print(f"  Yellow: 3 seconds")
    print(f"  Red: {cycle_length - green_times[i] - 3 * len(approaches)} seconds\n")
    time.sleep(1)  # Simulate time for demonstration (optional)
