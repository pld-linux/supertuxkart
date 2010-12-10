
%define		_rc		rc1
%define		_addons_ver	0.6.1

Summary:	SuperTuxKart - an enhanced version of TuxKart
Summary(pl.UTF-8):	SuperTuxKart - ulepszona wersja gry TuxKart
Name:		supertuxkart
Version:	0.7
Release:	0.%{_rc}.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/supertuxkart/%{name}-%{version}%{_rc}-src.tar.bz2
# Source0-md5:	da55995f47b76f2749fcaf37726a08df
Source1:	http://downloads.sourceforge.net/supertuxkart/addon%{_addons_ver}-1.zip
# Source1-md5:	28c2a6aff5190072e5b81b88d09126b8
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-useless_files.patch
Patch2:		%{name}-gettext.patch
Patch3:		%{name}-duplicate_files.patch
URL:		http://supertuxkart.sourceforge.net/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libvorbis-devel
BuildRequires:	plib-devel >= 1.8.4
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SuperTuxKart is an enhanced version of TuxKart, a kart racing game,
originaly done by Steve Baker, featuring Tux and a bunch of his
friends.

%description -l pl.UTF-8
SuperTuxKart jest ulepszoną wersją gry TuxKart, stworzonej przez
Steve'a Bakera, w której bierzemy udział w wyścigach gokartowych jako
Tux lub jego przyjaciele.

%prep
%setup -q -n %{name}-%{version}%{_rc} -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%{__sed} -i -e 's#$(prefix)/games#%{_bindir}#' src/Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a tracks/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}/data/tracks
cp -a karts/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}/data/karts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO data/CREDITS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}_32.xpm
