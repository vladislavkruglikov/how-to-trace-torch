import torch


assert torch.__version__ == "2.3.0a0+6ddf5cf85e.nv24.04"

with torch.profiler.profile(
    activities=[torch.profiler.ProfilerActivity.CUDA], 
    record_shapes=True,
    profile_memory=True
) as profiler:
    with torch.profiler.record_function("allocate_16_bytes"):
        matrix = torch.rand(size=(1024, 1024))
        matrix = matrix.cuda()
        other_matrix = torch.rand(size=(1024, 1024))
        other_matrix = other_matrix.cuda()
        output = matrix @ other_matrix
        output = output.cpu()

report = profiler.key_averages().table(sort_by="cpu_time_total")

print(report)

profiler.export_chrome_trace(path="trace_matrix_multiplication_gpu.json")
