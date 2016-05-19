Name:           python-rencode
Version:        1.0.3
Release:        1
Summary:        Web safe object pickling/unpickling
License:        GPLv3+ and BSD
URL:            https://github.com/aresch/rencode

Group:          Development/Python

Source0:        https://github.com/aresch/rencode/archive/v%{version}.tar.gz
      
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
%{__python} setup.py install -O2 --skip-build --root=%{buildroot} --prefix=%{_prefix}
%{_bindir}/find %{buildroot} -name \*.egg-info | %{_bindir}/xargs %{__rm}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc LICENSE README examples
%{python_sitearch}/yaml
%{python_sitearch}/*.so


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




##########################################################################################




%build
CFLAGS="%{optflags}" %{__python} setup.py build

pushd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py build
popd

%install
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

#fix permissions on shared objects
chmod 0755 \
    %{buildroot}%{python_sitearch}/rencode/_rencode.so \
    %{buildroot}%{python3_sitearch}/rencode/_rencode.cpython-*.so

%check
pushd tests
ln -sf %{buildroot}%{python_sitearch}/rencode rencode
%{__python} test_rencode.py
%{__python} timetest.py
popd

pushd %{py3dir}/tests
ln -sf %{buildroot}%{python3_sitearch}/rencode rencode
%{__python3} test_rencode.py
%{__python3} timetest.py
popd

%files
%{python_sitearch}/rencode
%{python_sitearch}/rencode*.egg-info
%doc COPYING README.md

%files -n python3-rencode
%{python3_sitearch}/rencode
%{python3_sitearch}/rencode*.egg-info
%doc COPYING README.md




