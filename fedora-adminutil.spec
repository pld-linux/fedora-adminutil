Summary:	Fedora Admin Util
Summary(pl):	Fedora Admin Util
Name:		fedora-adminutil
Version:	1.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	08c514a30604e192a22d7a035a9dfccc
URL:		http://directory.fedora.redhat.com/wiki/SetupUtil
BuildRequires:	icu
BuildRequires:	libstdc++-devel
BuildRequires:	mozldap-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Setup Util is a collection of C++ APIs used to write programs that
install, configure, and uninstall Fedora Server software.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CCC="%{__cxx}" \
	MAKE=%{__make} \
	ICU_GENRB=%{_bindir}/genrb \
	ICU_INCPATH=%{_includedir}/icu \
	LDAPSDK_INCDIR=%{_includedir}/mozldap \
	NSPR_INCDIR=%{_includedir}/nspr \
	SECURITY_INCDIR=%{_includedir}/nss

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/{libadminutil,libadmsslutil},%{_libdir}}
install built/adminutil/*/include/libadminutil/* $RPM_BUILD_ROOT/%{_includedir}/libadminutil
install built/adminutil/*/include/libadmsslutil/* $RPM_BUILD_ROOT/%{_includedir}/libadmsslutil
install built/adminutil/*/lib/lib* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.a
