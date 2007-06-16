Summary:	Fedora Admin Util - API to install and configure Fedora Server software
Summary(pl.UTF-8):	Fedora Admin Util - API do instalacji i konfiguracji oprogramowania Fedora Server
Name:		fedora-adminutil
Version:	1.1.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://directory.fedoraproject.org/sources/adminutil-%{version}.tar.bz2
# Source0-md5:	d320b5dcde3193e2a72b35220f728fd5
Patch0:		%{name}-link.patch
URL:		http://directory.fedoraproject.org/wiki/AdminUtil
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	icu >= 3.4
BuildRequires:	libicu-devel >= 3.4
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	mozldap-devel >= 6.0
BuildRequires:	nspr-devel >= 1:4.6
BuildRequires:	nss-devel >= 1:3.11
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AdminUtil is a set of utility functions written in C, which are
divided into 2 groups: libadminutil and libadmsslutil. They are mainly
used in the Admin Server / CGI services to communicate with the
configuration Directory Server. It covers, e.g., login to Admin Server
using the authentication with the Directory Server. AdminUtil is
needed to build the Admin Server as well as the Directory Server's
admin components.

%description -l pl.UTF-8
AdminUtil to zestaw funkcji narzędziowych napisanych w C, podzielonych
na dwie grupy: libadminutil i libadmsslutil. Są używane głównie przez
Admin Server / usługi CGI do komunikowania się z konfiguracyjnym
Directory Serverem. Pokrywają m.in. logowanie do Admin Servera przy
użyciu uwierzytelnienia względem Directory Servera. AdminUtil jest
potrzebny do zbudowania Admin Servera oraz komponentów
administracyjnych Directory Servera.

%package devel
Summary:	Header files for Fedora Admin Util libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Fedora Admin Util
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libicu-devel >= 3.4
Requires:	mozldap-devel >= 6.0
Requires:	nspr-devel >= 1:4.6
# for admsslutil
Requires:	nss-devel >= 1:3.11

%description devel
Header files for Fedora Admin Util libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Fedora Admin Util.

%package static
Summary:	Static Fedora Admin Util libraries
Summary(pl.UTF-8):	Statyczne biblioteki Fedora Admin Util
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Fedora Admin Util libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Fedora Admin Util.

%prep
%setup -q -n adminutil-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libadminutil.so.*.*.*
%attr(755,root,root) %{_libdir}/libadmsslutil.so.*.*.*
%{_datadir}/adminutil

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libadminutil.so
%attr(755,root,root) %{_libdir}/libadmsslutil.so
%{_libdir}/libadminutil.la
%{_libdir}/libadmsslutil.la
%{_includedir}/libadminutil
%{_includedir}/libadmsslutil
%{_pkgconfigdir}/adminutil.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libadminutil.a
%{_libdir}/libadmsslutil.a
