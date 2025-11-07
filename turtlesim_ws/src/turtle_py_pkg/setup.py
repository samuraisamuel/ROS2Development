from setuptools import find_packages, setup

package_name = 'turtle_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='142815081+samuraisamuel@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "move_forward = turtle_py_pkg.move_forward:main",
            "move_right = turtle_py_pkg.move_right:main",
            "command_converter = turtle_py_pkg.command_converter:main",
        ],
    },
)
