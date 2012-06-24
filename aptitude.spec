Summary:	curses-based apt frontend
Summary(pt_BR):Interface curses para o apt
Summary(es):	Curses-based apt frontend
Name:		aptitude
Version:	0.0.7.15
Release:	1
URL:		http://www.debian.org/Packages/unstable/admin/aptitude.html
Source0:	http://ftp.debian.org/debian/pool/main/a/aptitude/%{name}_%{version}.orig.tar.gz
Patch0:		aptitude-make.patch
License:	GPL
Group:		Applications/Archiving
BuildRequires:	gzip
BuildRequires:	apt-devel >= 0.3.19cnc36
BuildRequires:	ncurses-devel
BuildRequires:	libstdc++-devel
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Aptitude is a curses-based apt frontend with a number of useful
extended features, including a mutt-like syntax for matching packages
in a flexible and extreme flexibility and customization.

Despite the version number, aptitude is quite usable; it does almost
everything that dselect and console-apt do, and has its own extra
features as well.

%description -l pl
Aptitute jest graficzn�, bazuj�c� na ncurses nak�adk� na narz�dzie
apt z wieloma r�nimi, u�ytecznymi opcjami.

%description -l pt_BR
O Aptitude � uma interface curses para o apt com um n�mero de
caracter�sticas �teis e avan�adas, incluindo: uma sintaxe semelhante �
do mutt para casamento de padr�es em pacotes, de uma forma flex�vel e
personaliz�vel.

%description -l es
Aptitude is a curses-based apt frontend with a number of useful
extended features, including: a mutt-like syntax for matching packages
in a flexible and extreme flexibility and customization.

%prep
%setup -q -n %{name}-%{version}
%patch -p1

%build
automake -a -c
aclocal
autoheader
autoconf
%configure
%{__make}

gzip AUTHORS INSTALL NEWS COPYING README TODO %{name}-hackers-guide.txt

%install
rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
install -d %{buildroot}%{_localstatedir}/lib/%{name}/
install -D -m755 src/%{name} %{buildroot}/%{_bindir}/%{name}
install -D help.txt %{buildroot}%{_datadir}/%{name}/help.txt
install -D %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
(cd po;make install prefix=%{buildroot}/%{_prefix})
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/help.txt
%{_localstatedir}/lib/%{name}
%doc AUTHORS.gz INSTALL.gz NEWS.gz COPYING.gz
%doc README.gz TODO.gz %{name}-hackers-guide.txt.gz
