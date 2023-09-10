from setuptools import setup, Extension
from torch.utils import cpp_extension
import platform
import torch

extra_compile_args = {
    "cxx": ["-O3"],
    "nvcc": ["-O3"],
}
if torch.version.hip:
    extra_compile_args["nvcc"].append("-U__HIP_NO_HALF_CONVERSIONS__")

setup(
    name="exllama",
    version="0.0.7",
    install_requires=[
        "torch",
    ],
    packages=["exllama"],
    py_modules=["exllama"],
    ext_modules=[
        cpp_extension.CUDAExtension(
            "exllama_ext",
            [
                "exllama_ext/exllama_ext.cpp",
                "exllama_ext/cuda_buffers.cu",
                "exllama_ext/cuda_func/q4_matrix.cu",
                "exllama_ext/cuda_func/q4_matmul.cu",
                "exllama_ext/cuda_func/column_remap.cu",
                "exllama_ext/cuda_func/rms_norm.cu",
                "exllama_ext/cuda_func/rope.cu",
                "exllama_ext/cuda_func/half_matmul.cu",
                "exllama_ext/cuda_func/q4_attn.cu",
                "exllama_ext/cuda_func/q4_mlp.cu",
                "exllama_ext/cpu_func/rep_penalty.cpp",
            ],
            extra_compile_args=extra_compile_args,
            libraries=["cublas"] if platform.system() == "Windows" else [],
        ),
    ],
    cmdclass={"build_ext": cpp_extension.BuildExtension},
)
