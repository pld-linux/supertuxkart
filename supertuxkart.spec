Summary:	SuperTuxKart - an enhanced version of TuxKart
Summary(pl.UTF-8):	SuperTuxKart - ulepszona wersja gry TuxKart
Name:		supertuxkart
Version:	1.4
Release:	1
License:	GPL v1, GPL v2, GPL v3+, CC-BY-SA v3, CC-BY-SA v3+
Group:		X11/Applications/Games
Source0:	https://github.com/supertuxkart/stk-code/releases/download/%{version}/SuperTuxKart-%{version}-src.tar.xz
# Source0-md5:	c87a67ea6d5b52d464fe3d112db20263
Patch0:		gcc13.patch
URL:		https://supertuxkart.net/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	freetype-devel
BuildRequires:	harfbuzz-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	sqlite3-devel
BuildRequires:	squish-devel
BuildRequires:	wiiuse-devel
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SuperTuxKart is an enhanced version of TuxKart, a kart racing game,
originaly done by Steve Baker, featuring Tux and a bunch of his
friends.

%description -l pl.UTF-8
SuperTuxKart jest ulepszoną wersją gry TuxKart, stworzonej przez
Steve'a Bakera, w której bierzemy udział w wyścigach gokartowych jako
Tux lub jego przyjaciele.

%package data
Summary:	SuperTuxKart data files
Group:		X11/Applications/Games
BuildArch:	noarch

%description data
SuperTuxKart data files

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%prep
%setup -q -n SuperTuxKart-%{version}-src
%patch0 -p1

%build
mkdir -p build
cd build
# cmake makro doesnn't work in this case
cmake .. \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_C_FLAGS="%{optflags} -fno-strict-aliasing" \
        -DCMAKE_CXX_FLAGS="%{optflags} -fno-strict-aliasing" \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
        -DBUILD_RECORDER=0 \
        -DUSE_SYSTEM_WIIUSE:BOOL=ON \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# angelscript is not needed
%{__rm} $RPM_BUILD_ROOT%{_includedir}/angelscript.h
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/lib/cmake/Angelscript
%{__rm} $RPM_BUILD_ROOT%{_prefix}/lib/libangelscript.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md NETWORKING.md README.md data/CREDITS
%attr(755,root,root) %{_bindir}/supertuxkart
%{_desktopdir}/supertuxkart.desktop
%{_iconsdir}/hicolor/*x*/apps/supertuxkart.png
%{_datadir}/metainfo/supertuxkart.appdata.xml

%files data
%defattr(644,root,root,755)
%{_datadir}/%{name}
