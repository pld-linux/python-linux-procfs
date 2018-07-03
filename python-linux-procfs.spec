#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Linux /proc abstraction classes for Python 2
Summary(pl.UTF-8):	Klasy abstrakcji linuksowego /proc dla Pythona 2
Name:		python-linux-procfs
Version:	0.4.10
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	https://www.kernel.org/pub/software/libs/python/python-linux-procfs/%{name}-%{version}.tar.xz
# Source0-md5:	561a3177990a8e530a1402b7fe177423
URL:		https://rt.wiki.kernel.org/index.php/Tuna
BuildRequires:	python-modules >= 2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 abstractions to extract information from the Linux kernel
/proc files.

%description -l pl.UTF-8
Abstrakcje Pythona 2 do wydobywania informacji z plików /proc jądra
Linuksa.

%package -n python3-linux-procfs
Summary:	Linux /proc abstraction classes for Python 3
Summary(pl.UTF-8):	Klasy abstrakcji linuksowego /proc dla Pythona 3
Group:		Libraries/Python

%description -n python3-linux-procfs
Python 3 abstractions to extract information from the Linux kernel
/proc files.

%description -n python3-linux-procfs -l pl.UTF-8
Abstrakcje Pythona 3 do wydobywania informacji z plików /proc jądra
Linuksa.

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/procfs
%if "%{py_ver}" > "2.4"
#%{py_sitescriptdir}/python_linux_procfs-%{version}-py*.egg-info
%{py_sitescriptdir}/python_linux_procfs-0.4.9-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-linux-procfs
%defattr(644,root,root,755)
%{py3_sitescriptdir}/procfs
#%{py3_sitescriptdir}/python_linux_procfs-%{version}-py*.egg-info
%{py3_sitescriptdir}/python_linux_procfs-0.4.9-py*.egg-info
%endif
