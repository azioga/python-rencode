Name:           python-rencode
Version:        1.0.3
Release:        1
Summary:        Web safe object pickling/unpickling
License:        GPLv3+ and BSD
URL:            https://github.com/aresch/rencode
Group:          Development/Python
Source0:        https://github.com/aresch/rencode/archive/v%{version}.tar.gz#/rencode-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-cython
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.

%prep
%setup -q -n rencode-%{version}

%build
export CFLAGS="%{optflags}"
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
%{_bindir}/find %{buildroot} -name \*.egg-info | %{_bindir}/xargs %{__rm}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%{python_sitearch}/rencode
%{python_sitearch}/*.so
%{python_sitearch}/rencode*.egg-info
%doc COPYING README.md

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.3-1
- Update to version 1.0.3
- Update upstream location (now on github)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.2-4.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-2.20121209svn33
- use macros consistently
- fix permissions on shared objects
- drop useless setuptools copypasta
- fix License tag

* Thu Apr 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-1.20121209svn33
- initial package

