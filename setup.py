import facenet
from setuptools import setup, find_packages
packages = find_packages()
setup(
    name='facenet',
    version=facenet.__version__,
    author='David Sandberg',
    author_email='no_email_here...@gmail.com',
    packages=packages,
    package_data={'align': ['*.npy', 'facenet/align/*.npy']},
    entry_points={'console_scripts': ['align_dataset_mtcnn = facenet.align.align_dataset_mtcnn:main']},  # noqa E501
    url='https://github.com/davidsandberg/facenet',
    license='MIT License',
    description='Face recognition using Tensorflow',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    platforms=['any'],
    install_requires=[
        "future >= 0.16.0",
        "h5py",
        "imageio >= 2.4.0",
        "matplotlib",
        "numpy >= 1.14.0",
        "opencv-python >= 3.4.2",
        "Pillow",
        "psutil",
        "requests",
        "scikit-learn",
        "scipy >= 1.0.0",
        "setuptools >= 38.6.0",
        "tensorflow == 1.15"
        ]
)
