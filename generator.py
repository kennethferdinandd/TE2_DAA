import random

def generate_set_partition_dataset_even_sum(num_elements, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Generate a list of numbers and shuffle it
    numbers = list(range(1, 2 * num_elements + 1))
    random.shuffle(numbers)

    # Select the required number of elements
    dataset = numbers[:num_elements]

    # Ensure the sum is even
    while sum(dataset) % 2 != 0:
        random.shuffle(numbers)
        dataset = numbers[:num_elements]

    return dataset

def save_dataset_to_file(dataset, filename):
    with open(filename, 'w') as file:
        for element in dataset:
            file.write(str(element) + '\n')

# Generate datasets with even sums
dataset_10_elements = generate_set_partition_dataset_even_sum(10)
dataset_30_elements = generate_set_partition_dataset_even_sum(30)
dataset_40_elements = generate_set_partition_dataset_even_sum(40)
dataset_80_elements = generate_set_partition_dataset_even_sum(80)

save_dataset_to_file(dataset_10_elements, 'dataset_10_elements.txt')
save_dataset_to_file(dataset_30_elements, 'dataset_30_elements.txt')
save_dataset_to_file(dataset_40_elements, 'dataset_40_elements.txt')
save_dataset_to_file(dataset_80_elements, 'dataset_80_elements.txt')

print("Datasets with even sums have been successfully created.")
