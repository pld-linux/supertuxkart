%define	_rc	rc1
Summary:	SuperTuxKart - an enhanced version of TuxKart
Summary(pl.UTF-8):	SuperTuxKart - ulepszona wersja gry TuxKart
Name:		supertuxkart
Version:	0.5
Release:	0.%{_rc}.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/supertuxkart/%{name}-%{version}%{_rc}-src.tar.bz2
# Source0-md5:	e25de6af29d36918bf76d386d0a093f3
Source1:	%{name}.desktop
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
%setup -q -n %{name}-%{version}%{_rc}

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

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}_32.xpm
