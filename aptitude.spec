Summary:	Curses-based apt frontend
Summary(pt_BR):	Interface curses para o apt
Summary(pl):	Frontend dla apta oparty na bibliotece ncurses
Name:		aptitude
Version:	0.0.8.6
Release:	2cl
URL:		http://www.debian.org/Packages/unstable/admin/aptitude.html
Source0:	http://ftp.debian.org/debian/pool/main/a/aptitude/%{name}_%{version}.orig.tar.gz
Patch0:		%{name}-patch
Patch1:		%{name}-rpm4.patch
License:	GPL
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
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
Aptitute jest graficzn±, bazuj±c± na ncurses nak³adk± na narzêdzie apt
z wieloma ró¿nimi, u¿ytecznymi opcjami.

%description -l pt_BR
O Aptitude é uma interface curses para o apt com um número de
características úteis e avançadas, incluindo: uma sintaxe semelhante à
do mutt para casamento de padrões em pacotes, de uma forma flexível e
personalizável.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
rm -f missing
gettextize --copy --force
aclocal
autoconf
autoheader
automake -a -c
%configure
%{__make}

gzip -9nf AUTHORS INSTALL NEWS COPYING README TODO %{name}-hackers-guide.txt

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
