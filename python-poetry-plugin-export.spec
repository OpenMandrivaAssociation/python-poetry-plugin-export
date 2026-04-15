%define module poetry-plugin-export
%define oname poetry_plugin_export

Name:		python-poetry-plugin-export
Summary:	Poetry plugin to export the dependencies to various formats
Version:	1.10.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/poetry-plugin-export/
Source0:	https://files.pythonhosted.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package is a plugin that allows the export of locked packages to
various formats.

This plugin provides the same features as the existing export command
of Poetry which it will eventually replace.

%files
%license LICENSE
%doc README.md
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
