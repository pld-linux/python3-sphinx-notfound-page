#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (cannot find app fixture)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension to build a 404 page with absolute URLs
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do tworzenia strony 404 z bezwzględnymi URL-ami
Name:		python-sphinx-notfound-page
Version:	0.8
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-notfound-page/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-notfound-page/sphinx-notfound-page-%{version}.tar.gz
# Source0-md5:	2e1563e824b14391a065dae6dca39f91
URL:		https://pypi.org/project/sphinx-notfound-page/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx
BuildRequires:	python-pytest
BuildRequires:	sphinx-pdg
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
BuildRequires:	sphinx-pdg
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
# generated docs are incluced in sdist, so regeneration is disabled
%if %{with rebuild_doc}
BuildRequires:	python3-sphinx-autoapi
BuildRequires:	python3-sphinx-prompt
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	python3-sphinx_tabs
BuildRequires:	python3-sphinxemoji
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension to create a custom 404 page with absolute URLs
hardcoded.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do tworzenia własnej strony 404 z zakodowanymi
bezwzględnymi URL-ami.

%package -n python3-sphinx-notfound-page
Summary:	Sphinx extension to build a 404 page with absolute URLs
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do tworzenia strony 404 z bezwzględnymi URL-ami
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinx-notfound-page
Sphinx extension to create a custom 404 page with absolute URLs
hardcoded.

%description -n python3-sphinx-notfound-page -l pl.UTF-8
Rozszerzenie Sphinksa do tworzenia własnej strony 404 z zakodowanymi
bezwzględnymi URL-ami.

%package apidocs
Summary:	API documentation for Python sphinx-notfound-page module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinx-notfound-page
Group:		Documentation

%description apidocs
API documentation for Python sphinx-notfound-page module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinx-notfound-page.

%prep
%setup -q -n sphinx-notfound-page-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif
%endif

%if %{with rebuild_doc}
%{__make} -C docs html
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
%doc LICENSE README.rst
%{py_sitescriptdir}/notfound
%{py_sitescriptdir}/sphinx_notfound_page-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx-notfound-page
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/notfound
%{py3_sitescriptdir}/sphinx_notfound_page-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_static,autoapi,*.html,*.js}
%endif
