import os
import importlib.util
import time
import random
import numpy as np

# 알고리즘 파일 리스트 (같은 폴더에 위치)
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

# 정렬 함수 불러오기
def load_sort_functions(file_paths):
    sort_functions = {}
    for path in file_paths:
        module_name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # ✅ 래퍼 함수 우선 적용 (get_sort_function)
        if hasattr(module, "get_sort_function"):
            sort_func = module.get_sort_function()
            sort_functions[module_name] = sort_func
        elif hasattr(module, module_name):
            sort_func = getattr(module, module_name)
            if callable(sort_func):
                sort_functions[module_name] = sort_func

    return sort_functions

# 입력 데이터 생성
def generate_data(size, dtype='random'):
    if dtype == 'sorted':
        base = list(range(size))
    elif dtype == 'reversed':
        base = list(range(size, 0, -1))
    elif dtype == 'random':
        base = random.sample(range(size * 2), size)
    elif dtype == 'partially_sorted':
        half = size // 2
        base = list(range(half)) + random.sample(range(half, size * 2), size - half)
    return [(val, idx) for idx, val in enumerate(base)]

# 시간 측정만 수행
def measure(sort_func, data, repeat=10):
    times = []
    for _ in range(repeat):
        input_copy = data.copy()
        start = time.time()
        sort_func(input_copy)
        end = time.time()
        times.append(end - start)
    return np.mean(times)

# 실험 및 저장 (사이즈별)
def run_experiment_by_size(sort_functions, size, types):
    results = {}
    for name, func in sort_functions.items():
        results[name] = {}
        for dtype in types:
            key = f"{size}_{dtype}"
            data = generate_data(size, dtype)
            avg_time = measure(func, data, repeat=10)
            results[name][key] = avg_time
            print(f"{name} | {key} | Time: {avg_time:.6f}s")

    # 저장
    filename = f"results_{size}.txt"
    with open(filename, "w") as f:
        for algo, outcome in results.items():
            f.write(f"==== {algo} ====\n")
            for cond, t in outcome.items():
                f.write(f"{cond}: {t:.6f} sec\n")
            f.write("\n")
    print(f"✅ {filename} 저장 완료")

# 메인
if __name__ == "__main__":
    sort_functions = load_sort_functions(file_list)
    sizes = [1000, 10000, 100000]
    types = ['sorted', 'reversed', 'random', 'partially_sorted']
    for size in sizes:
        run_experiment_by_size(sort_functions, size, types)
