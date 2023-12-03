import tracemalloc
import time

def findPartition(arr, n):
    total_sum = sum(arr)

    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    partition_table = [[True for i in range(n + 1)] for j in range(target_sum + 1)]

    for i in range(n + 1):
        partition_table[0][i] = True

    for i in range(1, target_sum + 1):
        partition_table[i][0] = False

    for i in range(1, target_sum + 1):
        for j in range(1, n + 1):
            partition_table[i][j] = partition_table[i][j - 1]
            if i >= arr[j - 1]:
                partition_table[i][j] = partition_table[i][j] or partition_table[i - arr[j - 1]][j - 1]

    return partition_table[target_sum][n]

def solve_partition_problem(arr):
    tracemalloc.start()
    start_time = time.time()

    n = len(arr)
    result = findPartition(arr, n)

    end_time = time.time()
    running_time = (end_time - start_time) * 1000

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "result": result,
        "running_time": f"Running Time: {running_time:.6f} ms",
        "peak_memory": f"Peak Memory Usage: {peak_memory:.6f} bytes"
    }

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        arr = [int(line.strip()) for line in file.readlines()]

    result = solve_partition_problem(arr)

    with open(output_file, 'w') as file:
        if result["result"]:
            file.write("Can be divided into two subsets of equal sum\n")
        else:
            file.write("Cannot be divided into two subsets of equal sum\n")

        file.write(result["running_time"] + "\n")
        file.write(result["peak_memory"] + "\n")

# Example usage
input_file = "dataset_80_elements.txt"
output_file = "output_dp_80.txt"
main(input_file, output_file)
