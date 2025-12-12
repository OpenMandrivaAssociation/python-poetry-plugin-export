Summary:	Poetry plugin to export the dependencies to various formats
Name:		python-poetry-plugin-export
Version:	1.9.0
Release:	2
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/poetry-plugin-export/
Source0:	https://files.pythonhosted.org/packages/source/p/poetry_plugin_export/poetry_plugin_export-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildArch:	noarch

%description
This package is a plugin that allows the export of locked packages to
various formats.

This plugin provides the same features as the existing export command
of Poetry which it will eventually replace.

%prep
%autosetup -p1 -n poetry_plugin_export-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.md
%{py_sitedir}/poetry_plugin_export
%{py_sitedir}/poetry_plugin_export-*.*-info
