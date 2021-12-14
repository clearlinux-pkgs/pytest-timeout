#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-timeout
Version  : 2.0.2
Release  : 65
URL      : https://files.pythonhosted.org/packages/85/62/74068d0363f9dfb585079dcf906d5186116b6f1927bb6098816c1a934ce1/pytest-timeout-2.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/62/74068d0363f9dfb585079dcf906d5186116b6f1927bb6098816c1a934ce1/pytest-timeout-2.0.2.tar.gz
Summary  : pytest plugin to abort hanging tests
Group    : Development/Tools
License  : MIT
Requires: pytest-timeout-license = %{version}-%{release}
Requires: pytest-timeout-python = %{version}-%{release}
Requires: pytest-timeout-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pexpect
BuildRequires : pypi(pytest)
BuildRequires : pytest

%description
pytest-timeout
        ==============
        
        |python| |version| |anaconda| |ci|

%package license
Summary: license components for the pytest-timeout package.
Group: Default

%description license
license components for the pytest-timeout package.


%package python
Summary: python components for the pytest-timeout package.
Group: Default
Requires: pytest-timeout-python3 = %{version}-%{release}

%description python
python components for the pytest-timeout package.


%package python3
Summary: python3 components for the pytest-timeout package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_timeout)
Requires: pypi(pytest)

%description python3
python3 components for the pytest-timeout package.


%prep
%setup -q -n pytest-timeout-2.0.2
cd %{_builddir}/pytest-timeout-2.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639502122
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-timeout
cp %{_builddir}/pytest-timeout-2.0.2/LICENSE %{buildroot}/usr/share/package-licenses/pytest-timeout/8216f3d66db8d3c8edf0e6c29f7db60c021f3490
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-timeout/8216f3d66db8d3c8edf0e6c29f7db60c021f3490

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
