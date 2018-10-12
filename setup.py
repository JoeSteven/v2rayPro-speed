from setuptools import setup, find_packages

# readme_file = 'README.md'

# try:
#     import pypandoc
#     long_description = pypandoc.convert(readme_file, to='rst')
# except ImportError:
#     logging.warning('pypandoc module not found, long_description will be the raw text instead.')
#     with open(readme_file, encoding='utf-8') as fp:
#         long_description = fp.read()

setup(
    name='v2ray-ping',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'v2ray=v2ray.v2ray_ping:main',
            'v2ray-init=v2ray.v2ray_init:main',
        ]
    },

    url='https://github.com/JoeSteven/v2rayPro-speed',
    license='Apache 2.0',
    author='Joey',
    author_email='qiaoxiaoxi621@gmail.com',
    description='a ping tool for v2ray mac client,find fast vpn server for you',
    keywords=[
        'v2ray'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: Utilities',
    ]
)
