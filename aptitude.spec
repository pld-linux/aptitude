# TODO:
# - proper functions_{groups,pkgs}
# - strange groups browsing(?)
# - browser doesn't show 1st line of descriptions
Summary:	Curses-based apt frontend
Summary(pt_BR):	Interface curses para o apt
Summary(pl):	Frontend dla apta oparty na bibliotece ncurses
Name:		aptitude
Version:	0.2.11.1
Release:	0.1
License:	GPL
Group:		Applications/Archiving
Source0:	http://ftp.debian.org/debian/pool/main/a/aptitude/%{name}_%{version}.orig.tar.gz
# Source0-md5:	c9a1af703b6d0e6e68e5ce8ae8b87b54
Patch0:		%{name}-gcc3.patch
Patch1:		%{name}-rpm.patch
Patch2:		%{name}-acfix.patch
Patch3:		%{name}-po-fix.patch
URL:		http://www.debian.org/Packages/unstable/admin/aptitude.html
BuildRequires:	apt-devel >= 0.5.4cnc7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libsigc++1-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Aptitude is a curses-based apt frontend with a number of useful
extended features, including a mutt-like syntax for matching packages
in a flexible and extreme flexibility and customization.

Despite the version number, aptitude is quite usable; it does almost
everything that dselect and console-apt do, and has its own extra
features as well.

%description -l pl
Aptitute jest graficzn�, bazuj�c� na ncurses nak�adk� na narz�dzie apt
z wieloma r�nymi, u�ytecznymi opcjami.

%description -l pt_BR
O Aptitude � uma interface curses para o apt com um n�mero de
caracter�sticas �teis e avan�adas, incluindo: uma sintaxe semelhante �
do mutt para casamento de padr�es em pacotes, de uma forma flex�vel e
personaliz�vel.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-Wno-deprecated -I/usr/include/ncurses"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/lib

install -D %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -D %{name}.fi.1 $RPM_BUILD_ROOT%{_mandir}/fi/man1/%{name}.1
install -D %{name}.fr.1 $RPM_BUILD_ROOT%{_mandir}/fr/man1/%{name}.1
install -D %{name}.gl.1 $RPM_BUILD_ROOT%{_mandir}/gl/man1/%{name}.1
install -D %{name}.pl.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1/%{name}.1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/[!hm]*
%{_datadir}/%{name}/help.txt
%lang(fi) %{_datadir}/%{name}/help-fi.txt
%lang(fr) %{_datadir}/%{name}/help-fr.txt
%lang(gl) %{_datadir}/%{name}/help-gl.txt
%lang(pl) %{_datadir}/%{name}/help-pl.txt
%{_datadir}/%{name}/mine-help.txt
%lang(fi) %{_datadir}/%{name}/mine-help-fi.txt
%{_localstatedir}/lib/%{name}
%{_mandir}/man1/%{name}.1*
%lang(fi) %{_mandir}/fi/man1/%{name}.1*
%lang(fr) %{_mandir}/fr/man1/%{name}.1*
%lang(gl) %{_mandir}/gl/man1/%{name}.1*
%lang(pl) %{_mandir}/pl/man1/%{name}.1*
