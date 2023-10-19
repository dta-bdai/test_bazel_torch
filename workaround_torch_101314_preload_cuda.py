"""Hack to load CUDA variables shipped via PyPI. Addresses this Torch bug:
https://github.com/pytorch/pytorch/issues/101314
Copied from PyTorch's __init__.py file, with modifications:
https://github.com/pytorch/pytorch/blob/main/torch/__init__.py
Copyright notice below is from Torch.

From https://gist.github.com/qxcv/183c2d6cd81f7028b802b232d6a9dd62
"""
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of the PyTorch source tree.
import ctypes
import sys
import os
import platform
from typing import Dict

def _preload_cuda_deps(lib_folder: str, lib_name: str) -> None:
    """Preloads cuda deps if they could not be found otherwise."""
    # Should only be called on Linux if default path resolution have failed
    assert platform.system() == 'Linux', 'Should only be called on Linux'
    import glob
    lib_path = None
    for path in sys.path:
        nvidia_path = os.path.join(path, 'nvidia')
        if not os.path.exists(nvidia_path):
            continue
        # import pdb pdb.set_trace()
        candidate_lib_paths = glob.glob(os.path.join(nvidia_path, lib_folder, 'lib', lib_name))
        if candidate_lib_paths and not lib_path:
            lib_path = candidate_lib_paths[0]
        if lib_path:
            break
    if not lib_path:
        raise ValueError(f"{lib_name} not found in the system path {sys.path}")
    ctypes.CDLL(lib_path)


def preload_cuda_deps() -> None:
    cuda_libs: Dict[str, str] = {
        'cublas': 'libcublas.so.*',
        'cudnn': 'libcudnn.so.*',
        'cuda_nvrtc': 'libnvrtc.so.*',
        'cuda_runtime': 'libcudart.so.*',
        'cuda_cupti': 'libcupti.so.*',
        'cufft': 'libcufft.so.*',
        'curand': 'libcurand.so.*',
        'cusolver': 'libcusolver.so.*',
        'cusparse': 'libcusparse.so.*',
        'nccl': 'libnccl.so.*',
        'nvtx': 'libnvToolsExt.so.*',
    }
    for lib_folder, lib_name in cuda_libs.items():
        _preload_cuda_deps(lib_folder, lib_name)

preload_cuda_deps()
