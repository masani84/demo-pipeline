from setuptools import setup, find_packages

setup(name='census-income', 
      version="0.0.1",
      authod_email = 'sivakrishnam@gmail.com',
      packages=find_packages(),
      install_requires = ["pandas", "numpy", "flask", "scipy"]
      )