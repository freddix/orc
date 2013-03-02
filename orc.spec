%define		apiver	0.4

Summary:	The Oil Runtime Compiler
Name:		orc
Version:	0.4.17
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://code.entropywave.com/download/orc/%{name}-%{version}.tar.gz
# Source0-md5:	af1bf3dab9e69f3c36f389285e2a12a1
Patch0:		%{name}-build.patch
URL:		http://code.entropywave.com/projects/orc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data. The "language" is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package devel
Summary:	Header files for orc library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for orc library.

%package apidocs
Summary:	ORC API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
ORC API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/orc*
%attr(755,root,root) %ghost %{_libdir}/liborc-%{apiver}.so.?
%attr(755,root,root) %ghost %{_libdir}/liborc-*-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/liborc-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/liborc-*-%{apiver}.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborc-%{apiver}.so
%attr(755,root,root) %{_libdir}/liborc-*-%{apiver}.so
%{_includedir}/orc-%{apiver}
%{_libdir}/liborc-%{apiver}.la
%{_libdir}/liborc-*-%{apiver}.la
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/orc-%{apiver}.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/orc

