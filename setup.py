from setuptools import setup

setup(
    name='Scryfall_TabletopSim_Project',
    version='',
    packages=['lib', 'venv.Lib.site-packages.PIL', 'venv.Lib.site-packages.rsa', 'venv.Lib.site-packages.attr',
              'venv.Lib.site-packages.idna', 'venv.Lib.site-packages.past', 'venv.Lib.site-packages.past.tests',
              'venv.Lib.site-packages.past.types', 'venv.Lib.site-packages.past.utils',
              'venv.Lib.site-packages.past.builtins', 'venv.Lib.site-packages.past.translation',
              'venv.Lib.site-packages.yarl', 'venv.Lib.site-packages.isapi', 'venv.Lib.site-packages.tests',
              'venv.Lib.site-packages.future', 'venv.Lib.site-packages.future.moves',
              'venv.Lib.site-packages.future.moves.dbm', 'venv.Lib.site-packages.future.moves.html',
              'venv.Lib.site-packages.future.moves.http', 'venv.Lib.site-packages.future.moves.test',
              'venv.Lib.site-packages.future.moves.urllib', 'venv.Lib.site-packages.future.moves.xmlrpc',
              'venv.Lib.site-packages.future.moves.tkinter', 'venv.Lib.site-packages.future.tests',
              'venv.Lib.site-packages.future.types', 'venv.Lib.site-packages.future.utils',
              'venv.Lib.site-packages.future.builtins', 'venv.Lib.site-packages.future.backports',
              'venv.Lib.site-packages.future.backports.html', 'venv.Lib.site-packages.future.backports.http',
              'venv.Lib.site-packages.future.backports.test', 'venv.Lib.site-packages.future.backports.email',
              'venv.Lib.site-packages.future.backports.email.mime', 'venv.Lib.site-packages.future.backports.urllib',
              'venv.Lib.site-packages.future.backports.xmlrpc', 'venv.Lib.site-packages.future.standard_library',
              'venv.Lib.site-packages.mtgsdk', 'venv.Lib.site-packages.pyasn1', 'venv.Lib.site-packages.pyasn1.type',
              'venv.Lib.site-packages.pyasn1.codec', 'venv.Lib.site-packages.pyasn1.codec.ber',
              'venv.Lib.site-packages.pyasn1.codec.cer', 'venv.Lib.site-packages.pyasn1.codec.der',
              'venv.Lib.site-packages.pyasn1.codec.native', 'venv.Lib.site-packages.pyasn1.compat',
              'venv.Lib.site-packages.aiohttp', 'venv.Lib.site-packages.asyncio', 'venv.Lib.site-packages.certifi',
              'venv.Lib.site-packages.chardet', 'venv.Lib.site-packages.chardet.cli', 'venv.Lib.site-packages.pyimgur',
              'venv.Lib.site-packages.urllib3', 'venv.Lib.site-packages.urllib3.util',
              'venv.Lib.site-packages.urllib3.contrib', 'venv.Lib.site-packages.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.urllib3.packages', 'venv.Lib.site-packages.urllib3.packages.backports',
              'venv.Lib.site-packages.urllib3.packages.ssl_match_hostname', 'venv.Lib.site-packages.adodbapi',
              'venv.Lib.site-packages.altgraph', 'venv.Lib.site-packages.httplib2', 'venv.Lib.site-packages.macholib',
              'venv.Lib.site-packages.requests', 'venv.Lib.site-packages.scrython',
              'venv.Lib.site-packages.scrython.sets', 'venv.Lib.site-packages.scrython.cards',
              'venv.Lib.site-packages.scrython.catalog', 'venv.Lib.site-packages.scrython.rulings',
              'venv.Lib.site-packages.scrython.symbology', 'venv.Lib.site-packages.win32com',
              'venv.Lib.site-packages.win32com.test', 'venv.Lib.site-packages.win32com.demos',
              'venv.Lib.site-packages.win32com.client', 'venv.Lib.site-packages.win32com.makegw',
              'venv.Lib.site-packages.win32com.server', 'venv.Lib.site-packages.win32com.servers',
              'venv.Lib.site-packages.apiclient', 'venv.Lib.site-packages.multidict',
              'venv.Lib.site-packages.ordlookup', 'venv.Lib.site-packages.pythonwin.pywin',
              'venv.Lib.site-packages.pythonwin.pywin.mfc', 'venv.Lib.site-packages.pythonwin.pywin.idle',
              'venv.Lib.site-packages.pythonwin.pywin.Demos.ocx', 'venv.Lib.site-packages.pythonwin.pywin.tools',
              'venv.Lib.site-packages.pythonwin.pywin.dialogs', 'venv.Lib.site-packages.pythonwin.pywin.docking',
              'venv.Lib.site-packages.pythonwin.pywin.debugger', 'venv.Lib.site-packages.pythonwin.pywin.framework',
              'venv.Lib.site-packages.pythonwin.pywin.framework.editor',
              'venv.Lib.site-packages.pythonwin.pywin.framework.editor.color',
              'venv.Lib.site-packages.pythonwin.pywin.scintilla', 'venv.Lib.site-packages.libfuturize',
              'venv.Lib.site-packages.libfuturize.fixes', 'venv.Lib.site-packages.PyInstaller',
              'venv.Lib.site-packages.PyInstaller.lib', 'venv.Lib.site-packages.PyInstaller.lib.altgraph',
              'venv.Lib.site-packages.PyInstaller.lib.modulegraph', 'venv.Lib.site-packages.PyInstaller.hooks',
              'venv.Lib.site-packages.PyInstaller.hooks.pre_find_module_path',
              'venv.Lib.site-packages.PyInstaller.hooks.pre_safe_import_module',
              'venv.Lib.site-packages.PyInstaller.utils', 'venv.Lib.site-packages.PyInstaller.utils.hooks',
              'venv.Lib.site-packages.PyInstaller.utils.hooks.subproc',
              'venv.Lib.site-packages.PyInstaller.utils.win32', 'venv.Lib.site-packages.PyInstaller.utils.cliutils',
              'venv.Lib.site-packages.PyInstaller.depend', 'venv.Lib.site-packages.PyInstaller.loader',
              'venv.Lib.site-packages.PyInstaller.loader.rthooks', 'venv.Lib.site-packages.PyInstaller.archive',
              'venv.Lib.site-packages.PyInstaller.building', 'venv.Lib.site-packages.uritemplate',
              'venv.Lib.site-packages.win32comext.adsi', 'venv.Lib.site-packages.win32comext.bits',
              'venv.Lib.site-packages.win32comext.mapi', 'venv.Lib.site-packages.win32comext.shell',
              'venv.Lib.site-packages.win32comext.axdebug', 'venv.Lib.site-packages.win32comext.ifilter',
              'venv.Lib.site-packages.win32comext.propsys', 'venv.Lib.site-packages.win32comext.axscript',
              'venv.Lib.site-packages.win32comext.axscript.client',
              'venv.Lib.site-packages.win32comext.axscript.server', 'venv.Lib.site-packages.win32comext.internet',
              'venv.Lib.site-packages.win32comext.axcontrol', 'venv.Lib.site-packages.win32comext.directsound',
              'venv.Lib.site-packages.win32comext.directsound.test', 'venv.Lib.site-packages.win32comext.authorization',
              'venv.Lib.site-packages.win32comext.taskscheduler', 'venv.Lib.site-packages.oauth2client',
              'venv.Lib.site-packages.oauth2client.contrib', 'venv.Lib.site-packages.oauth2client.contrib.django_util',
              'venv.Lib.site-packages.async_timeout', 'venv.Lib.site-packages.libpasteurize',
              'venv.Lib.site-packages.libpasteurize.fixes', 'venv.Lib.site-packages.pyasn1_modules',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip',
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
