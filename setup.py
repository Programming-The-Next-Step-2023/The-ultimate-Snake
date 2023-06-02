import setuptools

setuptools.setup(
    name = "The-ultimate-Snake",
    version = "0.0.1",
    author = "pia",
    author_email = "pia.koch@student.uva.nl",
    python_requires = ">=3.6",
    packages = ['My_Snake_lib'],
    entry_points={"console_scripts": ["play= The-ultimate-Snake.My_Snake_lib.game:main"]}
)
