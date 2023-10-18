import sys

print(sys.path)
with open("/home/dta/tmp/path_with_debug.txt", "w") as f:
	f.writelines("\n".join(sys.path))

import torch

print(torch.__version__)
print(torch.cuda.is_available())

t = torch.rand(10, 10).cuda()
print(t.device)
