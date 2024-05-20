import torch


assert torch.__version__ == "2.3.0a0+6ddf5cf85e.nv24.04"

with torch.profiler.profile(
    activities=[torch.profiler.ProfilerActivity.CPU], 
    record_shapes=True,
    profile_memory=True
) as profiler:
    with torch.profiler.record_function("allocate_16_bytes"):
        vector = torch.FloatTensor([4.5, 3.9, 8.1, 7.0])

report = profiler.key_averages().table(sort_by="cpu_time_total")

# This will print report inside terminal
# make sure it says that 16 bytes were allocated
# since each float is 4 bytes and we have tensor with 4 numbers
print(report)

# In the names of functions that were called are some aten which
# is name of the tensor library that is used unde the hood of torch

# To visualize trace use chrome://tracing inside chrome browser
profiler.export_chrome_trace(path="trace_allocate_16_bytes_cpu.json")
