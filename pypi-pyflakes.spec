#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-pyflakes
Version  : 3.1.0
Release  : 102
URL      : https://files.pythonhosted.org/packages/8b/fb/7251eaec19a055ec6aafb3d1395db7622348130d1b9b763f78567b2aab32/pyflakes-3.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8b/fb/7251eaec19a055ec6aafb3d1395db7622348130d1b9b763f78567b2aab32/pyflakes-3.1.0.tar.gz
Summary  : passive checker of Python programs
Group    : Development/Tools
License  : MIT
Requires: pypi-pyflakes-bin = %{version}-%{release}
Requires: pypi-pyflakes-license = %{version}-%{release}
Requires: pypi-pyflakes-python = %{version}-%{release}
Requires: pypi-pyflakes-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
========
Pyflakes
========
A simple program which checks Python source files for errors.

%package bin
Summary: bin components for the pypi-pyflakes package.
Group: Binaries
Requires: pypi-pyflakes-license = %{version}-%{release}

%description bin
bin components for the pypi-pyflakes package.


%package license
Summary: license components for the pypi-pyflakes package.
Group: Default

%description license
license components for the pypi-pyflakes package.


%package python
Summary: python components for the pypi-pyflakes package.
Group: Default
Requires: pypi-pyflakes-python3 = %{version}-%{release}

%description python
python components for the pypi-pyflakes package.


%package python3
Summary: python3 components for the pypi-pyflakes package.
Group: Default
Requires: python3-core
Provides: pypi(pyflakes)

%description python3
python3 components for the pypi-pyflakes package.


%prep
%setup -q -n pyflakes-3.1.0
cd %{_builddir}/pyflakes-3.1.0
pushd ..
cp -a pyflakes-3.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690817817
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyflakes
cp %{_builddir}/pyflakes-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyflakes/200da923b63ba8767fe085a65a35f9c01b5eb867 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyflakes

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyflakes/200da923b63ba8767fe085a65a35f9c01b5eb867

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
