# Copyright (c) 2023 Boston Dynamics AI Institute LLC. All rights reserved.

# This file marks a workspace root for the Bazel build system.
# See `https://bazel.build/`.

workspace(name="test_torch")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name="bazel_skylib",
    sha256="66ffd9315665bfaafc96b52278f57c7e2dd09f5ede279ea6d39b2be471e7e3aa",
    urls=[
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
    ],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")


RULES_PYTHON_VERSION = "0.23.1"

http_archive(
    name="rules_python",
    sha256="84aec9e21cc56fbc7f1335035a71c850d1b9b5cc6ff497306f84cced9a769841",
    strip_prefix="rules_python-{}".format(RULES_PYTHON_VERSION),
    url="https://github.com/bazelbuild/rules_python/releases/download/{0}/rules_python-{0}.tar.gz".format(
        RULES_PYTHON_VERSION
    ),
)

load(
    "@rules_python//python:repositories.bzl",
    "py_repositories",
    "python_register_toolchains",
)
load("@rules_python//python:pip.bzl", "pip_parse")

py_repositories()

python_register_toolchains(
    name="test_torch_python",
    python_version="3.10",
    register_coverage_tool=True,
)

load("@test_torch_python//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

# Create a central repo that knows about the dependencies needed from
# requirements.txt.
pip_parse(
    name="python_deps",
    python_interpreter_target=interpreter,
    requirements_lock="//:requirements_lock.txt",
)

# Load the starlark macro which will define your dependencies.
load("@python_deps//:requirements.bzl", "install_deps")

# Call it to define repos for your requirements.
install_deps()
