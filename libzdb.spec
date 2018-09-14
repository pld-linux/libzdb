Summary:	Small, easy to use Database Connection Pool Library
Name:		libzdb
Version:	3.0
Release:	3
License:	GPL v3+ and MIT
Group:		Libraries
Source0:	http://www.tildeslash.com/libzdb/dist/%{name}-%{version}.tar.gz
# Source0-md5:	3bb9efff10a1f3ebc5b76c1055c48635
URL:		http://www.tildeslash.com/libzdb/
BuildRequires:	flex
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel >= 8
BuildRequires:	sqlite3-devel >= 3.6.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
The Zild C Database Library implements a small, fast, and easy to use
database API with thread-safe connection pooling. The library can
connect transparently to multiple database systems, has zero
configuration and connections are specified via a standard URL scheme.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup -q

%build
%configure \
	--enable-protected \
	--enable-sqliteunlock \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libzdb.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING README
%attr(755,root,root) %{_libdir}/libzdb.so.*.*.*
%ghost %{_libdir}/libzdb.so.11

%files devel
%defattr(644,root,root,755)
%doc doc/api-docs
%{_includedir}/zdb
%{_libdir}/libzdb.so
%{_pkgconfigdir}/zdb.pc
