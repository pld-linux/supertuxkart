Summary:	SuperTuxKart - an enhanced version of TuxKart
Summary(pl.UTF-8):	SuperTuxKart - ulepszona wersja gry TuxKart
Name:		supertuxkart
Version:	0.6.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/supertuxkart/%{name}-%{version}-src.tar.bz2
# Source0-md5:	7cddf934b9d5364a983b12b129fe91fa
Source1:	http://dl.sourceforge.net/supertuxkart/addon%{version}-1.zip
# Source1-md5:	28c2a6aff5190072e5b81b88d09126b8
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-useless_files.patch
Patch2:		%{name}-gettext.patch
URL:		http://supertuxkart.sourceforge.net/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freealut-devel >= 1.0.0
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
Steve'a Bakera, w której bierzemy udział w wyścigach gokartowych
jako Tux lub jego przyjaciele.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
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
cp -rf tracks/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}/data/tracks
cp -rf karts/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}/data/karts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO data/CREDITS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}_32.xpm
