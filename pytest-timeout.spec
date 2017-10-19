#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-timeout
Version  : 1.2.0
Release  : 21
URL      : https://pypi.debian.net/pytest-timeout/pytest-timeout-1.2.0.tar.gz
Source0  : https://pypi.debian.net/pytest-timeout/pytest-timeout-1.2.0.tar.gz
Summary  : py.test plugin to abort hanging tests
Group    : Development/Tools
License  : MIT
Requires: pytest-timeout-legacypython
Requires: pytest-timeout-python3
Requires: pytest-timeout-python
Requires: pytest
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
pytest-timeout
        ==============
        
        This is a plugin which will terminate tests after a certain timeout.
        When doing so it will show a stack dump of all threads running at the
        time.  This is useful when running tests under a continuous
        integration server or simply if you don't know why the test suite
        hangs.
        
        Note that while by default on POSIX systems py.test will continue to
        execute the tests after a test has timed, out this is not always
        possible.  Often the only sure way to interrupt a hanging test is by
        terminating the entire process.  As this is a hard termination
        (``os._exit()``) it will result in no teardown, JUnit XML output etc.
        But the plugin will ensure you will have the debugging output on
        stderr nevertheless, which is the most important part at this stage.
        See below for detailed information on the timeout methods and their
        side-effects.
        
        The pytest-timeout plugin has been tested on python 2.6 or higher,
        including 3.X, pypy and pypy3.
        
        
        Usage
        =====

%package legacypython
Summary: legacypython components for the pytest-timeout package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pytest-timeout package.


%package python
Summary: python components for the pytest-timeout package.
Group: Default
Requires: pytest-timeout-legacypython
Requires: pytest-timeout-python3

%description python
python components for the pytest-timeout package.


%package python3
Summary: python3 components for the pytest-timeout package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytest-timeout package.


%prep
%setup -q -n pytest-timeout-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507169996
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507169996
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
