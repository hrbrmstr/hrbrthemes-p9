import setuptools

setuptools.setup(
    name='hrbrthjemes',
    author='boB Rudis',
    author_email='bob@rud.is',
    description='Opinionated Themes For plotine',
    keywords='plotnine, ggplot2, themes',
    url='https://gitlab.com/hrbrmstr/hrbrthemes-p9',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    python_requires='>=3.6',
    install_requires=['plotnine'],
    extras_require={
        'dev': ['check-manifest'],
    },
)
