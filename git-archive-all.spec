Summary:		Python script wrapper for git-archive
Name:		git-archive-all
Version:		1.23.1
Release:		1
License:		MIT
Group:		Development/Tools
Url:		https://github.com/Kentzo/git-archive-all
Source0:	https://github.com/Kentzo/git-archive-all/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:		noarch

%description
This is a python script wrapper for git-archive, allowing to process also the
submodules. It Supports for any level of submodules tree. It creates an
archive from the current tree state by using:
"git ls-files --cached --full-name --no-empty-directory".
Files from submodules are extracted using the same command.

%files
%doc README.rst
%{_bindir}/%{name}

#-----------------------------------------------------------------------------

%prep
%setup -q
#sed -i 's@^#! /usr/bin/env python$@#! /usr/bin/env python3@' git_archive_all.py


%build
# Nothing to do


%install
%make_install prefix=%{buildroot}%{_prefix}
