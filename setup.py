from setuptools import setup

setup (name='igit',
       version = '1.0',
       packages = ['igit'],
       entry_points = {
           'console_scripts': [
                'igit = igit.cli:main'
           ]   
        

})