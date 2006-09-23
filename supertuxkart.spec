%define	_rc	rc2
Summary:	SuperTuxKart is an enhanced version of TuxKart
Summary(pl):	SuperTuxKart jest ulepszon± wersj± gry TuxKart
Name:		supertuxkart
Version:	0.2
Release:	0.%{_rc}.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/supertuxkart/%{name}-%{version}%{_rc}.tar.bz2
# Source0-md5:	77d4715424a969bf102a9fdca3cb1f55
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
%setup -q -n %{name}-%{version}%{_rc}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
