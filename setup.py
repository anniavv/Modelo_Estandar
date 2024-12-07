from setuptools import setup, find_packages

setup(
    name="Modelo_Estandar",
    version="0.1.0",
    description="Un paquete sobre partículas del modelo estándar con interfaz gráfica usando PyQt5.",
    author="Annia Verdín",
    author_email="annia_verdin@ciencias.unam.mx",
    url="https://github.com/anniavv/Modelo_Estandar.git",
    packages=find_packages(),
    install_requires=["PyQt5"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
