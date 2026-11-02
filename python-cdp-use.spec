Name:		python-cdp-use
Version:	1.4.5
Release:	1
Summary:	Type-safe Chrome DevTools Protocol client
License:	MIT
Group:		Development/Python
URL:		https://github.com/browser-use/cdp-use
Source0:	https://files.pythonhosted.org/packages/source/c/cdp-use/cdp_use-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)

%description
cdp-use is a typed Python client for the Chrome DevTools Protocol.
browser-harness uses it to drive a local browser.

%files
%doc README.md
%license LICENSE
%{python_sitelib}/cdp_use
%{python_sitelib}/cdp_use-%{version}.dist-info
