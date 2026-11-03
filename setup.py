import setuptools

setuptools.setup(
    name="My_Snake_lib",
    version="0.0.2",
    author="pia",
    author_email="pia.koch@student.uva.nl",
    python_requires=">=3.6",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=["pillow"],
    package_data={"My_Snake_lib": ["*.gif", "python_images/*"]},
    entry_points={"console_scripts": ["play = My_Snake_lib.game:main"]},
)
