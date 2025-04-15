import os
import importlib.util
import time
import random
import numpy as np

file_list = [
    "bubble_sort.py",
    "cocktail_shaker_sort.py",
    "comb_sort.py",
    "heap_sort.py",
    "insertion_sort.py",
    "intro_sort.py",
    "library_sort.py",
    "merge_sort.py",
    "quick_sort.py",
    "selection_sort.py",
    "tim_sort.py",
    "tournament_sort.py"
]


def load_sort_functions(file_paths):
    sort_functions = {}
    for path in file_paths:
        module_name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "get_sort_function"):
            sort_func = module.get_sort_function()
            sort_functions[module_name] = sort_func

        elif hasattr(module, module_name):
            sort_func = getattr(module, module_name)
            if callable(sort_func):
                sort_functions[module_name] = sort_func

    return sort_functions

def generate_data(size, dtype='random'):
    num_unique = 5 
    values = [i % num_unique for i in range(size)]
    random.shuffle(values) 

    if dtype == 'sorted':
        base = sorted([(val, idx) for idx, val in enumerate(values)], key=lambda x: x[0])
    elif dtype == 'reversed':
        base = sorted([(val, idx) for idx, val in enumerate(values)], key=lambda x: x[0], reverse=True)
    elif dtype == 'random':
        base = [(val, idx) for idx, val in enumerate(values)]
        random.shuffle(base)
    elif dtype == 'partially_sorted':
        base = [(val, idx) for idx, val in enumerate(values)]
        half = size // 2
        base[:half] = sorted(base[:half], key=lambda x: x[0])
        random.shuffle(base[half:])
    return base

def check_stability(sorted_data):
    from collections import defaultdict
    groups = defaultdict(list)
    for value, index in sorted_data:
        groups[value].append(index)
    for indices in groups.values():
        if indices != sorted(indices):
            return False
    return True

def measure(sort_func, data, repeat=10):
    times = []
    stabilities = []
    for _ in range(repeat):
        input_copy = data.copy()
        start = time.time()
        sort_func(input_copy)
        end = time.time()
        times.append(end - start)
        stable = check_stability(input_copy)
        stabilities.append(stable)
    return np.mean(times), sum(stabilities) / repeat

def run_experiment_by_size(sort_functions, size, types):
    results = {}
    for name, func in sort_functions.items():
        results[name] = {}
        for dtype in types:
            key = f"{size}_{dtype}"
            data = generate_data(size, dtype)
            avg_time, stability = measure(func, data, repeat=10)
            results[name][key] = (avg_time, stability)
            print(f"{name} | {key} | Time: {avg_time:.6f}s | Stability: {stability:.2f}")

    filename = f"results_{size}_stability.txt"
    with open(filename, "w") as f:
        for algo, outcome in results.items():
            f.write(f"==== {algo} ====\n")
            for cond, (t, s) in outcome.items():
                f.write(f"{cond}: {t:.6f} sec | Stability: {s:.2f}\n")
            f.write("\n")
    print(f"✅ {filename} 저장 완료")

if __name__ == "__main__":
    sort_functions = load_sort_functions(file_list)
    sizes = [1000]
    types = ['random']
    for size in sizes:
        run_experiment_by_size(sort_functions, size, types)
