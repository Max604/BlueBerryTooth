from distutils.core import setup

setup(
    name='BlueBerryTooth',
    version='1.0',
    packages=['me.max604', 'me.max604.clienttooth', 'me.max604.servertooth'],
    url='https://github.com/Max604/BlueBerryTooth',
    license='GNU',
    author='Max604',
    author_email='',
    description=''
)

package_dir = {'': 'me/max604'}
packages = {'clienttooth', 'servertooth'}