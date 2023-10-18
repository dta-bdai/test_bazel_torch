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

# load(
#     "@rules_python//python:repositories.bzl",
#     "py_repositories",
#     "python_register_toolchains",
# )
# load("@rules_python//python:pip.bzl", "pip_parse")

# py_repositories()

# python_register_toolchains(
#     name="test_torch_python",
#     python_version="3.10",
#     register_coverage_tool=True,
# )

# load("@test_torch_python//:defs.bzl", "interpreter")
# load("@rules_python//python:pip.bzl", "pip_parse")

# # Create a central repo that knows about the dependencies needed from
# # requirements.txt.
# pip_parse(
#     name="python_deps",
#     python_interpreter_target=interpreter,
#     requirements_lock="//:requirements_lock.txt",
# )

# # Load the starlark macro which will define your dependencies.
# load("@python_deps//:requirements.bzl", "install_deps")

# Call it to define repos for your requirements.
# install_deps()

# Poetry rules for managing Python dependencies

# http_archive(
#     name = "com_sonia_rules_poetry",
#     sha256 = "8a7a6a5d2ef859ba4309929f3b4d61031f2a4bfed6f450f04ab09443246a4b5c",
#     strip_prefix = "rules_poetry-ecd0d9c66b89403667304b11da3bd99764797a63",
#     urls = ["https://github.com/soniaai/rules_poetry/archive/ecd0d9c66b89403667304b11da3bd99764797a63.tar.gz"],
# )

# load("@com_sonia_rules_poetry//rules_poetry:defs.bzl", "poetry_deps")

# poetry_deps()

# load("@com_sonia_rules_poetry//rules_poetry:poetry.bzl", "poetry")

# poetry(
#     name = "poetry",
#     lockfile = "//:poetry.lock",
#     pyproject = "//:pyproject.toml",
#     # optional, if you would like to pull from pip instead of a Bazel cache
#     # tags = ["no-remote-cache"],
# )

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_conda",
    sha256 = "ee187c4902f5f8da85fcba9943064fd38b2a75f80ed0a2844b34cf9e27cb5990",
    url = "https://github.com/spietras/rules_conda/releases/download/0.2.0/rules_conda-0.2.0.zip"
)

load("@rules_conda//:defs.bzl", "conda_create", "load_conda", "register_toolchain")

load_conda(
    conda_version = "23.3.1",
    installer = "miniforge",
    install_mamba = True,
    mamba_version = "1.4.2",
    quiet = False,
    timeout = 100,
)

conda_create(
    name = "env",  # name of the environment
    environment = "@//:empty_environment.yaml",  # label pointing to environment configuration file
    use_mamba = True,  # Whether to use mamba to create the conda environment. If this is True, install_mamba must also be True
    clean = False,  # True if conda cache should be cleaned (less space taken, but slower subsequent builds), default is False
    quiet = False,  # True if conda output should be hidden True, default is True
    timeout = 100,  # how many seconds each execute action can take, default is 3600
)

register_toolchain(env = "env")
