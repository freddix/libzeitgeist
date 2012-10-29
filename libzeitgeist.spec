Summary:	Zeitgeist client library
Name:		libzeitgeist
Version:	0.3.18
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://launchpad.net/libzeitgeist/0.3/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	d63a37295d01a58086d0d4ae26e604c2
URL:		http://zeitgeist-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a client library for applications that want to
interact with the Zeitgeist daemon.

%package devel
Summary:	Header files for zeitgeist library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for zeitgeist library.

%package apidocs
Summary:	zeitgeist library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for zeitgeist library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libzeitgeist

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libzeitgeist-1.0.so.?
%attr(755,root,root) %{_libdir}/libzeitgeist-1.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzeitgeist-1.0.so
%{_includedir}/zeitgeist-1.0
%{_pkgconfigdir}/zeitgeist-1.0.pc
%{_datadir}/vala/vapi/zeitgeist-1.0.deps
%{_datadir}/vala/vapi/zeitgeist-1.0.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/zeitgeist-1.0

