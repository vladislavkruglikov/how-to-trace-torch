import torch


assert torch.__version__ == "2.3.0a0+6ddf5cf85e.nv24.04"

with torch.profiler.profile(
    activities=[torch.profiler.ProfilerActivity.CUDA], 
    record_shapes=True,
    profile_memory=True
) as profiler:
    with torch.profiler.record_function("allocate_16_bytes"):
        vector = torch.FloatTensor([4.5, 3.9, 8.1, 7.0])
        vector = vector.cuda()

report = profiler.key_averages().table(sort_by="cpu_time_total")

print(report)

profiler.export_chrome_trace(path="trace_allocate_16_bytes_gpu.json")
