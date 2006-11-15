# TODO: -devel/-static separation
Summary:	Fedora Admin Util - API to install and configure Fedora Server software
Summary(pl):	Fedora Admin Util - API do instalacji i konfiguracji oprogramowania Fedora Server
Name:		fedora-adminutil
Version:	1.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	08c514a30604e192a22d7a035a9dfccc
URL:		http://directory.fedora.redhat.com/wiki/AdminUtil
BuildRequires:	icu
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mozldap-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AdminUtil is a set of utility functions written in C, which are
divided into 2 groups: libadminutil and libadmsslutil. They are mainly
used in the Admin Server / CGI services to communicate with the
configuration Directory Server. It covers, e.g., login to Admin Server
using the authentication with the Directory Server. AdminUtil is
needed to build the Admin Server as well as the Directory Server's
admin components.

%description -l pl
AdminUtil to zestaw funkcji narzêdziowych napisanych w C, podzielonych
na dwie grupy: libadminutil i libadmsslutil. S± u¿ywane g³ównie przez
Admin Server / us³ugi CGI do komunikowania siê z konfiguracyjnym
Directory Serverem. Pokrywaj± m.in. logowanie do Admin Servera przy
u¿yciu uwierzytelnienia wzglêdem Directory Servera. AdminUtil jest
potrzebny do zbudowania Admin Servera oraz komponentów
administracyjnych Directory Servera.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CCC="%{__cxx}" \
	MAKE="%{__make}" \
	ICU_GENRB=%{_bindir}/genrb \
	ICU_INCPATH=%{_includedir}/icu \
	LDAPSDK_INCDIR=%{_includedir}/mozldap \
	NSPR_INCDIR=%{_includedir}/nspr \
	SECURITY_INCDIR=%{_includedir}/nss

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/{libadminutil,libadmsslutil},%{_libdir}}
install built/adminutil/*/include/libadminutil/* $RPM_BUILD_ROOT%{_includedir}/libadminutil
install built/adminutil/*/include/libadmsslutil/* $RPM_BUILD_ROOT%{_includedir}/libadmsslutil
install built/adminutil/*/lib/lib* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_includedir}/*
