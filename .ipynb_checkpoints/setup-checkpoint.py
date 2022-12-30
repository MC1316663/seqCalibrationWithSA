from setuptools import setup

setup(
    name = 'seqCalibrationWithSA',
    version = 0.0.1,
    description = "algorithm for sequential calibration with variance based SA",
    url = 'https://github.com/MC1316663/seqCalibrationWithSA.git',
    author = 'Moongi Choi',
    author_email = 'u1316663@utah.edu',
    packages = ['seqCalibrationWithSA'],
    install_packages = []
)


'''note: How to make library
- cmd -> cd repository
- python setup.py bdist_wheel
- cd dist
- twine upload xxx.whl

'''