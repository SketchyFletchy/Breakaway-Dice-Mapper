from setuptools import setup, find_packages


with open('requirements.txt', 'r') as rf:
    requirements = rf.readlines()
    requirements = [x.replace('\n', '').replace('\r', '')
                    for x in requirements]

setup(
    name='breakawayDiceMapper',
    version='0.1',
    python_requires='>=3.5',
    packages=find_packages(),
    install_requires=[requirements],
    entry_points={
        'console_scripts': [
            'bdm = breakawayDiceMapper.__main__:main',
            'bdm-clean = breakawayDiceMapper.cleanDir:main',
            'bdm-plot = breakawayDiceMapper.plotter:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
