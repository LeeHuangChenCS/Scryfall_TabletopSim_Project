from setuptools import setup

setup(
    name='Scryfall_TabletopSim_Project',
    version='1.0',
    packages=['venv.Lib.site-packages.PIL', 'venv.Lib.site-packages.rsa', 'venv.Lib.site-packages.attr',
              'venv.Lib.site-packages.idna', 'venv.Lib.site-packages.yarl', 'venv.Lib.site-packages.tests',
              'venv.Lib.site-packages.mtgsdk', 'venv.Lib.site-packages.pyasn1', 'venv.Lib.site-packages.pyasn1.type',
              'venv.Lib.site-packages.pyasn1.codec', 'venv.Lib.site-packages.pyasn1.codec.ber',
              'venv.Lib.site-packages.pyasn1.codec.cer', 'venv.Lib.site-packages.pyasn1.codec.der',
              'venv.Lib.site-packages.pyasn1.codec.native', 'venv.Lib.site-packages.pyasn1.compat',
              'venv.Lib.site-packages.aiohttp', 'venv.Lib.site-packages.asyncio', 'venv.Lib.site-packages.certifi',
              'venv.Lib.site-packages.chardet', 'venv.Lib.site-packages.chardet.cli', 'venv.Lib.site-packages.pyimgur',
              'venv.Lib.site-packages.urllib3', 'venv.Lib.site-packages.urllib3.util',
              'venv.Lib.site-packages.urllib3.contrib', 'venv.Lib.site-packages.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.urllib3.packages', 'venv.Lib.site-packages.urllib3.packages.backports',
              'venv.Lib.site-packages.urllib3.packages.ssl_match_hostname', 'venv.Lib.site-packages.httplib2',
              'venv.Lib.site-packages.requests', 'venv.Lib.site-packages.scrython',
              'venv.Lib.site-packages.scrython.sets', 'venv.Lib.site-packages.scrython.cards',
              'venv.Lib.site-packages.scrython.catalog', 'venv.Lib.site-packages.scrython.rulings',
              'venv.Lib.site-packages.scrython.symbology', 'venv.Lib.site-packages.apiclient',
              'venv.Lib.site-packages.multidict', 'venv.Lib.site-packages.uritemplate',
              'venv.Lib.site-packages.oauth2client', 'venv.Lib.site-packages.oauth2client.contrib',
              'venv.Lib.site-packages.oauth2client.contrib.django_util', 'venv.Lib.site-packages.async_timeout',
              'venv.Lib.site-packages.pyasn1_modules', 'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.idna',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pytoml',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.certifi',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.msgpack',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.util',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.colorama',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.progress',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.requests',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.packaging',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.webencodings',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.req',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.vcs',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.utils',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.models',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.commands',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.operations'],
    url='',
    license='',
    author='Lee',
    author_email='',
    description=''
)
