#
# spec file for package python-makefun
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/


%define python_version python3
Name:           python3-makefun
Version:        1.11.3
Release:        0
License:        BSD-3-Clause
Summary:        Small library to dynamically create python functions
Url:            https://github.com/smarie/python-makefun
Group:          Development/Languages/Python
# Source:         https://files.pythonhosted.org/packages/source/m/makefun/makefun-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
# BuildRequires:  %{python_module pytest-runner}
# BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-six
# SECTION test requirements
# BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python3-six
Suggests:       python-funcsigs

# %python_subpackages

%description
Small library to dynamically create python functions.

%prep
%setup -q -n %{name}-%{version}/python-makefun

%build
SETUPTOOLS_SCM_PRETEND_VERSION=1.11.3
%py3_build

%install
%py3_install
# %python_expand %fdupes %{buildroot}%{$python_sitelib}

# No tests, as tests require pytest-cases, which requires makefun
#%%check
#%%pytest

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/*

%changelog
