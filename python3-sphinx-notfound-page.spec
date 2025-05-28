#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Sphinx extension to build a 404 page with absolute URLs
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do tworzenia strony 404 z bezwzględnymi URL-ami
Name:		python3-sphinx-notfound-page
Version:	1.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-notfound-page/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_notfound_page/sphinx_notfound_page-%{version}.tar.gz
# Source0-md5:	88c8413b3daf4ca387d4782c3360222a
URL:		https://pypi.org/project/sphinx-notfound-page/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
%if %{with tests}
BuildRequires:	python3-Sphinx >= 5
BuildRequires:	python3-pytest
BuildRequires:	sphinx-pdg >= 5
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension to create a custom 404 page with absolute URLs
hardcoded.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do tworzenia własnej strony 404 z zakodowanymi
bezwzględnymi URL-ami.

%prep
%setup -q -n sphinx_notfound_page-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/notfound
%{py3_sitescriptdir}/sphinx_notfound_page-%{version}.dist-info
