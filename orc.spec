%define		apiver	0.4

Summary:	The Oil Runtime Compiler
Name:		orc
Version:	0.4.19
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/orc/%{name}-%{version}.tar.gz
# Source0-md5:	2cacea6271aade6d592fe1622a136f19
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

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
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/orc-%{apiver}.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/orc

