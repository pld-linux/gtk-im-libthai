#
# Conditional build:
%bcond_without	gtk2	# GTK+2 support
%bcond_without	gtk3	# GTK+3 support
#
Summary:	GTK+ Thai input method based on libthai
Summary(pl.UTF-8):	Metoda wprowadzania znaków tajskich dla GTK+ oparta na libthai
Name:		gtk-im-libthai
Version:	0.2.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
# Source0-md5:	7985535703e6770983469a0e60779b15
URL:		https://linux.thai.net/projects/libthai
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.22}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	libthai-devel >= 0.1.2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ Thai input method based on libthai.

%description -l pl.UTF-8
Metoda wprowadzania znaków tajskich dla GTK+ oparta na libthai.

%package -n gtk+2-im-libthai
Summary:	GTK+ 2 Thai input method based on libthai
Summary(pl.UTF-8):	Metoda wprowadzania znaków tajskich dla GTK+ 2 oparta na libthai
Group:		Libraries
Requires(post,postun):	gtk+2 >= 2:2.22
Requires:	gtk+2 >= 2:2.22
Requires:	libthai >= 0.1.2

%description -n gtk+2-im-libthai
GTK+ 2 Thai input method based on libthai.

%description -n gtk+2-im-libthai -l pl.UTF-8
Metoda wprowadzania znaków tajskich dla GTK+ 2 oparta na libthai.

%package -n gtk+3-im-libthai
Summary:	GTK+ 3 Thai input method based on libthai
Summary(pl.UTF-8):	Metoda wprowadzania znaków tajskich dla GTK+ 3 oparta na libthai
Group:		Libraries
Requires(post,postun):	gtk+3 >= 3.0.0
Requires:	gtk+3 >= 3.0.0
Requires:	libthai >= 0.1.2

%description -n gtk+3-im-libthai
GTK+ 3 Thai input method based on libthai.

%description -n gtk+3-im-libthai -l pl.UTF-8
Metoda wprowadzania znaków tajskich dla GTK+ 3 oparta na libthai.

%prep
%setup -q

%build
%configure \
	%{!?with_gtk2:--disable-gtk2} \
	%{!?with_gtk3:--disable-gtk3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_gtk2:%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.10.0/immodules/*.la}
%{?with_gtk3:%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.0.0/immodules/*.la}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n gtk+2-im-libthai
%if "%{_lib}" == "lib64"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%postun -n gtk+2-im-libthai
%if "%{_lib}" == "lib64"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%post -n gtk+3-im-libthai
%if "%{_lib}" == "lib64"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%postun -n gtk+3-im-libthai
%if "%{_lib}" == "lib64"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%if %{with gtk2}
%files -n gtk+2-im-libthai
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/gtk-2.0/2.10.0/immodules/im-thai-libthai.so
%endif

%if %{with gtk3}
%files -n gtk+3-im-libthai
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/gtk-3.0/3.0.0/immodules/im-thai-libthai.so
%endif
