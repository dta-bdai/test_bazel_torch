import workaround_torch_101314_preload_cuda  # noqa
import torch

print(torch.__version__)

print(torch.cuda.is_available())

t = torch.rand(10, 10).cuda()
print(t.device)
