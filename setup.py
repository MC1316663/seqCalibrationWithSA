from setuptools import setup

setup(
    name = 'sequntial_calibrationWithSA',
    version = '0.0.2',
    description = "algorithm for sequential calibration with variance based SA",
    url = 'https://github.com/MC1316663/seqCalibrationWithSA.git',
    author = 'Moongi Choi',
    author_email = 'u1316663@utah.edu',
    packages = ['sequntial_calibrationWithSA'],
    install_requires = ['numpy']
)


'''note: How to make library
- cmd -> cd repository (C:\Users\MoongiChoi\Desktop\MG\양식, 코드 등\Python\Sequential_Calibration_with_SA\seqCalibrationWithSA)
- python setup.py bdist_wheel
- cd dist
- twine upload xxx.whl
- 업데이트시에는 setup.py -> 0.02로 하고 다시 위 과정 반복
- https://pypi.org/project/sequntial-calibrationWithSA/ 에서 확인

참고:https://lsjsj92.tistory.com/592
https://developer-theo.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-GitHub-Repository-%EC%83%9D%EC%84%B1%EB%B6%80%ED%84%B0-PyPI-Package-%EB%B0%B0%ED%8F%AC%EA%B9%8C%EC%A7%80

'''