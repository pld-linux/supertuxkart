Summary:	SuperTuxKart - an enhanced version of TuxKart
Summary(pl.UTF-8):	SuperTuxKart - ulepszona wersja gry TuxKart
Name:		supertuxkart
Version:	0.4
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/supertuxkart/%{name}-%{version}-src.tar.bz2
# Source0-md5:	badcaf9cb51afc11c1abf126b2cbba74
Source1:	%{name}.desktop
URL:		http://supertuxkart.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	plib-devel >= 1.8.0
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
%setup -q

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
