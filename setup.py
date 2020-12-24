from setuptools import find_packages, setup

setup(
    name='DingTalkMessageBot',
    version='0.1.0',
    description='A Simple DingTalk Message Bot',
    url='https://github.com/jicewarwick/DingTalkMessageBot',
    author='Ce Ji',
    author_email='Mr.Ce.Ji@outlook.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='DingTalk, Bot',
    packages=find_packages(),
    python_requires='>=3.5, <4',
    install_requires=['requests']
)
