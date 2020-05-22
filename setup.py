from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="A Cloud Guru example from Robin Norwood",
    author_email="example_from@acloud.guru",
    description="SnapshotAlyzer 3000 is a tool for managing AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/caroline-lynagh/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points={
        "console_scripts": [
            "shotty = shotty.shotty:cli",
        ]
    }
#    entry_points= '''
#        [console_scripts]
#        shotty=shotty.shotty:cli
#    ''',
)
