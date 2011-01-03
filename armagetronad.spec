#
# TODO: - start scripts for server
#	- fix build on 64 bits
#
Summary:	A Tron lightcycle game with focus on multiplayer mode
Summary(pl.UTF-8):	Gra Tron ze światłocyklem skupiająca się na trybie dla wielu graczy
Name:		armagetronad
Version:	0.2.8.3.1
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/armagetronad/%{name}-%{version}.src.tar.bz2
# Source0-md5:	d4957ee0c2d3ae9d630d1362a6dcee70
#Source1:	%{name}.desktop
#Source2:	%{name}.png
Source3:	http://armagetron.sourceforge.net/addons/moviepack.zip
# Source3-md5:	e2d40309dde7e1339ca6aff7599cdfa3
URL:		http://armagetronad.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libxml2-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In Armagetron, you ride a lightcycle around the game grid. You can
only make sharp turns of 90 degrees and a wall constantly builds up
after you. Make your enemies crash into your wall, but be aware that
they are trying to do the same to you. If you are fast enough, you may
be able to trap them, but the only way to speed up your lightcycle is
to drive close to the dangerous walls. Prepare for exciting strategic
preparations followed by action-packed close combat!

%description -l pl.UTF-8
W grze Armagetron jedzie się światłocyklem dookoła planszy. Można
wykonywać tylko ostre zakręty o 90 stopni, a za graczem ciągle buduje
się ściana. Trzeba spowodować, by wrogowie roztrzaskali się na tej
ścianie, ale także uważać, bo oni próbują zrobić to samo. Jeśli gracz
jest szybki, może złapać ich wszystkich, ale jedynym sposobem na
przyspieszenie światłocyklu jest jazda blisko niebezpiecznych ścian.
Trzeba się przygotować na ekscytujące strategiczne przygotowania i
następującą po nich walkę w zbliżeniu!

%package moviepack
Summary:	Moviepack addon
Summary(pl.UTF-8):	Dodatek Moviepack
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description moviepack
Moviepack addon.

%description moviepack -l pl.UTF-8
Dodatek Moviepack.

%package server
Summary:	Armagetron server
Summary(pl.UTF-8):	Serwer Armagetrona
Group:		Applications/Games

%description server
Armagetron server.

%description server -l pl.UTF-8
Serwer Armagetrona.

%prep
%setup -q -a3

# fix build with libpng >= 2:1.4.0
%{__sed} -i 's/png_check_sig/png_sig_cmp/' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-music \
	--disable-sysinstall \
	--disable-uninstall
#	--disable-glout \
#	--enable-games \
#	--enable-main \
#	--enable-master \
#	--enable-music \
#	--disable-initscripts \
#	--disable-useradd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_bindir}} \
#	$RPM_BUILD_ROOT%{_prefix}/games/%{name}/moviepack \
#	$RPM_BUILD_ROOT%{_sysconfdir_server}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
#
#cp $RPM_BUILD_ROOT%{_sysconfdir}/* $RPM_BUILD_ROOT%{_sysconfdir_server}
#cp -R moviepack $RPM_BUILD_ROOT%{_prefix}/games/%{name}
#rm -f $RPM_BUILD_ROOT%{_prefix}/games/%{name}/moviepack/art_read_me.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS src/doc/{*.html,net}
%dir %{_sysconfdir}/games
%dir %{_sysconfdir}/games/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/games/%{name}/*.cfg
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.cfg
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.srv
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/games/armagetronad
%dir %{_datadir}/games/armagetronad/language
%{_datadir}/games/armagetronad/language/*.txt
%dir %{_datadir}/games/armagetronad/models
%{_datadir}/games/armagetronad/models/*.mod
%dir %{_datadir}/games/armagetronad/resource
%dir %{_datadir}/games/armagetronad/resource/included
%{_datadir}/games/armagetronad/resource/included/*.dtd
%dir %{_datadir}/games/armagetronad/resource/included/AATeam
%{_datadir}/games/armagetronad/resource/included/AATeam/*.dtd
%dir %{_datadir}/games/armagetronad/resource/included/Anonymous
%dir %{_datadir}/games/armagetronad/resource/included/Anonymous/polygon
%dir %{_datadir}/games/armagetronad/resource/included/Anonymous/polygon/regular
%{_datadir}/games/armagetronad/resource/included/Anonymous/polygon/regular/*.xml
%dir %{_datadir}/games/armagetronad/resource/included/Your_mom
%dir %{_datadir}/games/armagetronad/resource/included/Your_mom/clever
%{_datadir}/games/armagetronad/resource/included/Your_mom/clever/*.xml
%dir %{_datadir}/games/armagetronad/resource/included/Z-Man
%dir %{_datadir}/games/armagetronad/resource/included/Z-Man/fortress
%{_datadir}/games/armagetronad/resource/included/Z-Man/fortress/*.xml
%dir %{_datadir}/games/armagetronad/sound
%{_datadir}/games/armagetronad/sound/*.wav
%dir %{_datadir}/games/armagetronad/textures
%{_datadir}/games/armagetronad/textures/*.jpg
%{_datadir}/games/armagetronad/textures/*.png

%files moviepack
%defattr(644,root,root,755)
#%%doc moviepack/art_read_me.txt
#%%{_prefix}/games/%{name}/moviepack

%files server
%defattr(644,root,root,755)
%if 0
%attr(755,root,root) %{_bindir}/armagetronad-dedicated
%dir %{_prefix}/games/armagetronad-dedicated
%{_datadir}/games/armagetronad-dedicated/bin
%attr(755,root,root) %{_prefix}/games/armagetronad-dedicated/bin/*
%exclude %{_prefix}/games/armagetronad-dedicated/bin/uninstall
%{_prefix}/games/armagetronad-dedicated/language
%dir %{_sysconfdir_server}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir_server}/*.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir_server}/*.srv
%endif
