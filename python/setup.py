from setuptools import setup, find_packages

setup(
    version="1.0",
    description="chuck-fact python bindings",
    author="Misha Tavkhelidze",
    py_modules="chuckfact",
    setup_requires=["cffi", "path.py"],
    cffi_modules=["build_chuck_fact.py:ffi_builder"],
    install_requires=["cffi"],
)
