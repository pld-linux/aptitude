Summary:	Curses-based apt frontend
Summary(pt_BR):	Interface curses para o apt
Summary(pl):	Frontend dla apta oparty na bibliotece ncurses
Name:		aptitude
Version:	0.0.8.6
Release:	2cl
License:	GPL
Group:		Applications/Archiving
URL:		http://www.debian.org/Packages/unstable/admin/aptitude.html
Source0:	http://ftp.debian.org/debian/pool/main/a/aptitude/%{name}_%{version}.orig.tar.gz
Patch0:		%{name}-patch
Patch1:		%{name}-rpm4.patch
Patch2:		%{name}-am_fix.patch
BuildRequires:	apt-devel >= 0.3.19cnc36
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
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
%patch2 -p1

%build
rm -f missing
gettextize --copy --force
aclocal
%{__autoconf}
autoheader
%{__automake}
%configure
%{__make}

gzip -9nf AUTHORS INSTALL NEWS README TODO %{name}-hackers-guide.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/

install -D -m755 src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D help.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/help.txt
install -D %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
cd po
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}
cd ..

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/help.txt
%{_localstatedir}/lib/%{name}
%doc AUTHORS.gz INSTALL.gz NEWS.gz
%doc README.gz TODO.gz %{name}-hackers-guide.txt.gz
