import os
import papermill as pm

def train_ct(dataset_name, hampel_window_len, num_sigmas):
    input = "constant-threshold.ipynb"
    output = f"out/constant-threshold-{dataset_name}.ipynb"
    pm.execute_notebook(input, output, parameters = dict(
        dataset_name = dataset_name,
        hampel_window_len = hampel_window_len,
        num_sigmas = num_sigmas
    ))

def train_all(num_datasets, hampel_window_len, num_sigmas):
    for i in range(num_datasets):
        name = f'wn-{f"00{str(i)}"[-3:]}'
        train_ct(name, hampel_window_len, num_sigmas)
        i = i + 1

dir = "./out"
if not os.path.exists(dir):
    os.mkdir(dir)

# Different training params
#train_all(10, 5, 2)
train_all(10, 5, 3)
#train_all(10, 5, 4)
