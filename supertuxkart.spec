Summary:	SuperTuxKart - an enhanced version of TuxKart
Summary(pl):	SuperTuxKart - ulepszona wersja gry TuxKart
Name:		supertuxkart
Version:	0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/supertuxkart/SuperTuxKart-%{version}.tar.bz2
# Source0-md5:	c31c35af3a9c12f2890b4076cf55267b
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://supertuxkart.berlios.de
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	plib-devel >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SuperTuxKart is an enhanced version of TuxKart, a kart racing game,
originaly done by Steve Baker, featuring Tux and a bunch of his
friends.

%description -l pl
SuperTuxKart jest ulepszon± wersj± gry TuxKart, stworzonej przez
Steve'a Bakera, w której bierzemy udzia³ w wy¶cigach gokartowych jako
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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
