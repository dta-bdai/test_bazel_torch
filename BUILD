load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//python:defs.bzl", "py_binary")
load("@python_deps//:requirements.bzl", "requirement")

compile_pip_requirements(
    name="requirements",
    extra_args=["--allow-unsafe"],
    requirements_in="requirements.in",
    requirements_txt="requirements_lock.txt",
)

py_binary(
    name="test",
    srcs=["test.py"],
    deps=[
        requirement("torch"),
    ],
)
