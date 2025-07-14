# TODO:
# - proper functions_{groups,pkgs}
# - strange groups browsing(?)
# - browser doesn't show 1st line of descriptions
Summary:	Curses-based apt frontend
Summary(pl.UTF-8):	Frontend dla apta oparty na bibliotece ncurses
Summary(pt_BR.UTF-8):	Interface curses para o apt
Name:		aptitude
Version:	0.3.5.1
Release:	0.1
License:	GPL v2+
Group:		Applications/Archiving
#Source0:	http://ftp.debian.org/debian/pool/main/a/aptitude/%{name}_%{version}.orig.tar.gz
# no longer available on debian.org, use some old mirror
Source0:	ftp://ftp.gnome.org/mirror/debian-misc/debian-armeb/pool/main/a/aptitude/%{name}_%{version}.orig.tar.gz
# Source0-md5:	ac47b705bcbec6f0b45732d16ecdd82b
# http://apt-rpm.org/patches/aptitude-0.3.5.1-apt-rpm.patch
Patch0:		%{name}-apt-rpm.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-format.patch
Patch3:		%{name}-sigc.patch
URL:		http://aptitude.alioth.debian.org/
BuildRequires:	apt-devel >= 0.5.15lorg3.94a
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libsigc++-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpm-devel >= 5
Requires:	apt >= 0.5.15lorg3.94a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir		/var/lib

%description
Aptitude is a curses-based apt frontend with a number of useful
extended features, including a mutt-like syntax for matching packages
in a flexible and extreme flexibility and customization.

Despite the version number, aptitude is quite usable; it does almost
everything that dselect and console-apt do, and has its own extra
features as well.

%description -l pl.UTF-8
Aptitute jest graficzną, bazującą na ncurses nakładką na narzędzie apt
z wieloma różnymi, użytecznymi opcjami.

%description -l pt_BR.UTF-8
O Aptitude é uma interface curses para o apt com um número de
características úteis e avançadas, incluindo: uma sintaxe semelhante à
do mutt para casamento de padrões em pacotes, de uma forma flexível e
personalizável.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses -I/usr/include/rpm"
%configure \
	--disable-werror

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/lib

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc or dummy files
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/{COPYING,NEWS,README*}
# already packaged in proper locations
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/aptitude.{fi,fr}.8

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS FAQ NEWS TODO
%attr(755,root,root) %{_bindir}/aptitude
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/[!hm]*
%{_datadir}/%{name}/help.txt
%lang(cs) %{_datadir}/%{name}/help-cs.txt
%lang(de) %{_datadir}/%{name}/help-de.txt
%lang(es) %{_datadir}/%{name}/help-es.txt
%lang(eu) %{_datadir}/%{name}/help-eu.txt
%lang(fi) %{_datadir}/%{name}/help-fi.txt
%lang(fr) %{_datadir}/%{name}/help-fr.txt
%lang(gl) %{_datadir}/%{name}/help-gl.txt
%lang(it) %{_datadir}/%{name}/help-it.txt
%lang(ja) %{_datadir}/%{name}/help-ja.txt
%lang(pl) %{_datadir}/%{name}/help-pl.txt
%lang(pt_BR) %{_datadir}/%{name}/help-pt_BR.txt
%lang(sv) %{_datadir}/%{name}/help-sv.txt
%lang(tr) %{_datadir}/%{name}/help-tr.txt
%lang(zh_CN) %{_datadir}/%{name}/help-zh_CN.txt
%lang(zh_TW) %{_datadir}/%{name}/help-zh_TW.txt
%{_datadir}/%{name}/mine-help.txt
%lang(cs) %{_datadir}/%{name}/mine-help-cs.txt
%lang(de) %{_datadir}/%{name}/mine-help-de.txt
%lang(fi) %{_datadir}/%{name}/mine-help-fi.txt
%lang(fr) %{_datadir}/%{name}/mine-help-fr.txt
%lang(it) %{_datadir}/%{name}/mine-help-it.txt
%{_localstatedir}/aptitude
%dir %{_docdir}/aptitude
%dir %{_docdir}/aptitude/html
%lang(cs) %{_docdir}/aptitude/html/cs
%{_docdir}/aptitude/html/en
%lang(fi) %{_docdir}/aptitude/html/fi
%lang(fr) %{_docdir}/aptitude/html/fr
%{_mandir}/man8/aptitude.8*
%lang(cs) %{_mandir}/cs/man8/aptitude.8*
%lang(de) %{_mandir}/de/man8/aptitude.8*
%lang(fi) %{_mandir}/fi/man8/aptitude.8*
%lang(fr) %{_mandir}/fr/man8/aptitude.8*
%lang(gl) %{_mandir}/gl/man8/aptitude.8*
%lang(it) %{_mandir}/it/man8/aptitude.8*
%lang(pl) %{_mandir}/pl/man8/aptitude.8*
