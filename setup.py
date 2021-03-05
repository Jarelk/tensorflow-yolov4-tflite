from setuptools import setup, find_packages

REQUIRED = [
  'tensorflow-gpu==2.3.0rc0',
  'opencv-python==4.5.1.48',
  'lxml', 
  'tqdm',
  'absl-py',
  'matplodlib',
  'easydict',
  'pillow',
]

setup(
   name='tensorflow-yolov4-tflite-setup',
   version='0.0.1',
   url='https://github.com/Jarelk/tensorflow-yolov4-tflite/',
   python_requires='==3.8.0',
   description='Literally just trying to add a setup.py for easy installing',
   packages=find_packages(),
   install_requires=REQUIRED,
   license='MIT'
)
