# load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//python:defs.bzl", "py_binary")
# load("@python_deps//:requirements.bzl", "requirement")
# load("@poetry//:dependencies.bzl", "dependency")


# compile_pip_requirements(
#     name="requirements",
#     extra_args=["--allow-unsafe"],
#     requirements_in="requirements.in",
#     requirements_txt="requirements_lock.txt",
# )

py_binary(
    name="test",
    srcs=["test.py"],
    # data=["@python_deps_nvidia_cufft_cu12//:site-packages/nvidia/cufft/lib/libcufft.so.11"],
    # deps=[
    #     requirement("torch"),
    #     requirement("ipdb"),
    # ],
)
