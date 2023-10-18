# test_bazel_torch

Small repo to reproduce errors with torch.

Try running:
```bash
bazel run //:test
```

Error message:
```
INFO: Analyzed target //:test (0 packages loaded, 0 targets configured).
INFO: Found 1 target...
Target //:test up-to-date:
  bazel-bin/test
INFO: Elapsed time: 0.120s, Critical Path: 0.00s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Running command line: bazel-bin/test
Traceback (most recent call last):
  File "/home/dta/.cache/bazel/_bazel_dta/2884c22a612f21a527cba82d4ecab394/execroot/test_torch/bazel-out/k8-fastbuild/bin/test.runfiles/python_deps_torch/site-packages/torch/__init__.py", line 174, in _load_global_deps
    ctypes.CDLL(lib_path, mode=ctypes.RTLD_GLOBAL)
  File "/home/dta/.cache/bazel/_bazel_dta/2884c22a612f21a527cba82d4ecab394/external/test_torch_python_x86_64-unknown-linux-gnu/lib/python3.10/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libcufft.so.11: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/dta/.cache/bazel/_bazel_dta/2884c22a612f21a527cba82d4ecab394/execroot/test_torch/bazel-out/k8-fastbuild/bin/test.runfiles/test_torch/test.py", line 1, in <module>
    import torch
  File "/home/dta/.cache/bazel/_bazel_dta/2884c22a612f21a527cba82d4ecab394/execroot/test_torch/bazel-out/k8-fastbuild/bin/test.runfiles/python_deps_torch/site-packages/torch/__init__.py", line 234, in <module>
    _load_global_deps()
  File "/home/dta/.cache/bazel/_bazel_dta/2884c22a612f21a527cba82d4ecab394/execroot/test_torch/bazel-out/k8-fastbuild/bin/test.runfiles/python_deps_torch/site-packages/torch/__init__.py", line 195, in _load_global_deps
    _preload_cuda_deps(lib_folder, lib_name)
  File "/home/dta/.cache/bazel/_bazel_dta/2884c22a612f21a527cba82d4ecab394/execroot/test_torch/bazel-out/k8-fastbuild/bin/test.runfiles/python_deps_torch/site-packages/torch/__init__.py", line 161, in _preload_cuda_deps
    ctypes.CDLL(lib_path)
  File "/home/dta/.cache/bazel/_bazel_dta/2884c22a612f21a527cba82d4ecab394/external/test_torch_python_x86_64-unknown-linux-gnu/lib/python3.10/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libnvJitLink.so.12: cannot open shared object file: No such file or directory
```
