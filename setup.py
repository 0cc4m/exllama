from setuptools import setup, Extension
from torch.utils import cpp_extension
import platform

setup(
    name="exllama",
    version="0.0.1",
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
                "exllama_ext/cuda_func/q4_mlp.cu",
                "exllama_ext/cpu_func/rep_penalty.cpp",
            ],
            extra_compile_args={"nvcc": ["-O3"]},
            libraries=["cublas"] if platform.system() == "Windows" else [],
        ),
    ],
    cmdclass={"build_ext": cpp_extension.BuildExtension},
)
