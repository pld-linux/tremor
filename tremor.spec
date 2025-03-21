Summary:	Tremor - integer Ogg Vorbis library
Summary(pl.UTF-8):	Tremor - biblioteka Ogg Vorbis operująca na liczbach całkowitych
Name:		tremor
Version:	1.2.1
%define	gitref	9b78f57f4335f7158dbb82df00645d2ba57e0d33
%define	snap	20240715
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	BSD
Group:		Libraries
# git clone https://git.xiph.org/tremor.git
Source0:	https://gitlab.xiph.org/xiph/tremor/-/archive/%{gitref}/%{name}-%{snap}.tar.bz2
# Source0-md5:	0b89bc44a645040d40741c29cb3e909d
Patch0:		%{name}-am.patch
URL:		https://xiph.org/vorbis/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libogg-devel >= 1:1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libogg >= 1:1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tremor Vorbis I stream and file decoder provides an embeddable,
integer-only library (libvorbisidec) intended for decoding all current
and future Vorbis I compliant streams. The Tremor libvorbisidec
library exposes an API intended to be as similar as possible to the
familiar 'vorbisfile' library included with the open source Vorbis
reference libraries distributed for free by Xiph.org.

%description -l pl.UTF-8
Tremor - dekoder strumieni i plików Vorbis I - dostarcza dającą się
osadzać, operującą tylko na liczbach całkowitych bibliotekę
(libvorbisidec) przeznaczoną do dekodowania wszystkich obecnych i
przyszłych strumieni zgodnych ze specyfikacją Vorbis I. Biblioteka
Tremor libvorbisidec udostępnia API pomyślane jako najbliższe jak to
tylko możliwe znanej biblioteki vorbisfile zawartej w referencyjnych
bibliotekach Vorbis udostępnianych na wolnej licencji wraz ze źródłami
przez Xiph.org.

%package devel
Summary:	Header files for Tremor library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Tremor
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel >= 1:1.0

%description devel
Header files for Tremor library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Tremor.

%package static
Summary:	Static Tremor library
Summary(pl.UTF-8):	Statyczna biblioteka Tremor
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Tremor library.

%description static -l pl.UTF-8
Statyczna biblioteka Tremor.

%prep
%setup -q -n %{name}-%{gitref}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvorbisidec.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING README
%attr(755,root,root) %{_libdir}/libvorbisidec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvorbisidec.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/*.{css,html}
%attr(755,root,root) %{_libdir}/libvorbisidec.so
%{_includedir}/tremor
%{_pkgconfigdir}/vorbisidec.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvorbisidec.a
