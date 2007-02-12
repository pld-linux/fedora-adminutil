Summary:	Fedora Admin Util - API to install and configure Fedora Server software
Summary(pl.UTF-8):	Fedora Admin Util - API do instalacji i konfiguracji oprogramowania Fedora Server
Name:		fedora-adminutil
Version:	1.0.4
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	8bafc54cdc08e3886b6a68d0ac9367a0
Patch0:		%{name}-link.patch
URL:		http://directory.fedora.redhat.com/wiki/AdminUtil
BuildRequires:	icu
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mozldap-devel >= 6.0
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
Requires:	mozldap-devel >= 6.0
Requires:	nspr-devel

%description devel
Header files for Fedora Admin Util libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Fedora Admin Util.

%prep
%setup -q
%patch0 -p1

%build
%{__make} buildAdminUtil \
	ARCH_DEBUG="%{rpmcflags}" \
	ARCH_OPT="%{rpmcflags}" \
	BUILD_DEBUG=%{?debug:full}%{!?debug:optimize} \
	CC="%{__cc}" \
	CCC="%{__cxx}" \
	MAKE="%{__make}" \
	NSOS_TEST=PLD \
	ICU_GENRB=%{_bindir}/genrb \
	ICU_INCPATH=%{_includedir}/icu \
	LDAPSDK_INCDIR=%{_includedir}/mozldap \
	NSPR_INCDIR=%{_includedir}/nspr \
	SECURITY_INCDIR=%{_includedir}/nss

%{__make} -f pkgadminutil.mk pkguxAdminUtil \
	BUILD_DEBUG=%{?debug:full}%{!?debug:optimize} \
	INSTDIR=. \
	PKGINSTDIR=. \
	NSOS_TEST=PLD

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

cp -r built/adminutil/*/include/* $RPM_BUILD_ROOT%{_includedir}
cp -r built/adminutil/*/lib/* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/adminutil-properties

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/adminutil-1.0
