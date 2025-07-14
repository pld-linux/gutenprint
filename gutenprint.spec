# TODO
# - port info_and_pdf_only.patch and install documentation in correct place.
#
# Conditional build:
%bcond_without	cups		# CUPS plugin
%bcond_with	gimp		# GIMP plugin
%bcond_without	static_libs	# static libraries
#
Summary:	Collection of high-quality printer drivers
Summary(pl.UTF-8):	Zestaw wysokiej jakości sterowników do drukarek
%define	majorver	5.3
Name:		gutenprint
Version:	%{majorver}.4
Release:	2
License:	GPL
Group:		Applications/Printing
Source0:	http://downloads.sourceforge.net/gimp-print/%{name}-%{version}.tar.bz2
# Source0-md5:	537851d7b82e77a4c466c2c4f3a6a43e
Patch0:		%{name}-opt.patch
Patch1:		%{name}-static.patch
Patch2:		%{name}-am.patch
URL:		http://sourceforge.net/projects/gimp-print/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.9
%{?with_cups:BuildRequires:	cups-devel >= 1.2}
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools >= 0.16
%{?with_gimp:BuildRequires:	gimp-devel >= 1:2.4.0}
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimpplugindir	%(gimptool --gimpplugindir)/plug-ins
%define		cupslibdir	%(cups-config --serverbin)

%description
Gutenprint is a collection of very high quality printer drivers for
UNIX/Linux. The goal of this project is uncompromising print quality
and robustness. Included with this package is the Print plugin for the
GIMP (hence the name), a CUPS driver, and a driver for Ghostscript
that may be compiled into that package. This driver package is
Foomatic-compatible to enable plug and play with many print spoolers.
In addition, various printer maintenance utilities are included. Many
users report that the quality of Gutenprint on high end Epson Stylus
printers matches or exceeds the quality of the drivers supplied for
Windows and Macintosh.

This package was previously named gimp-print.

%description -l pl.UTF-8
Gutenprint to zbiór bardzo wysokiej jakości sterowników do drukarek
dla systemów UNIX/Linux. Celem tego projektu jest jak najlepsza jakość
wydruku. Dołączone do tego pakietu są: wtyczka dla programu GIMP (stąd
nazwa), sterownik CUPS i sterownik Ghostscriptu. Sterownik umożliwia
bezpośrednią współpracę z wieloma kolejkami wydruku. Dodatkowo
dołączonych jest wiele programów do obsługi drukarki. Wielu
użytkowników twierdzi ze jakość wydruków na najlepszych drukarkach
Epson Stylus dorównuje albo nawet przerasta jakością to, co jest
oferowane przez sterowniki dla Windows i MacOS.

Ten pakiet wcześniej nazywał się gimp-print.

%package -n libgutenprint
Summary:	libgutenprint library
Summary(pl.UTF-8):	Biblioteka libgutenprint
Summary(pt_BR.UTF-8):	Bibliotecas dinâmicas para impressão de alta qualidade
Group:		Libraries
Obsoletes:	foomatic-db-gutenprint < 5.2.14
Obsoletes:	gimp-print-lib < 5
Obsoletes:	gutenprint-ijs < 5.2.14
Obsoletes:	libgimprint < 5

%description -n libgutenprint
libgutenprint library.

%description -n libgutenprint -l pl.UTF-8
Biblioteka libgutenprint.

%package -n libgutenprint-devel
Summary:	Header files for libgutenprint library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgutenprint
Summary(pt_BR.UTF-8):	Cabeçalhos e arquivos de desenvolvimento para o libgutenprint
Group:		Development/Libraries
Requires:	libgutenprint = %{version}-%{release}
Obsoletes:	gimp-print-devel < 5
Obsoletes:	libgimpprint-devel < 5

%description -n libgutenprint-devel
Header files for libgutenprint library.

%description -n libgutenprint-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgutenprint.

%description -n libgutenprint-devel -l pt_BR.UTF-8
Este são os arquivos de desenvolvimento para compilar programas com a
biblioteca libgutenprint.

%package -n libgutenprint-static
Summary:	libgutenprint static library
Summary(pl.UTF-8):	Statyczna biblioteka libgutenprint
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libgutenprint
Group:		Development/Libraries
Requires:	libgutenprint-devel = %{version}-%{release}
Obsoletes:	gimp-print-static < 5
Obsoletes:	libgimprint-static < 5

%description -n libgutenprint-static
libgutenprint static library.

%description -n libgutenprint-static -l pl.UTF-8
Biblioteka statyczna libgutenprint.

%description -n libgutenprint-static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libgutenprint.

%package -n libgutenprintui
Summary:	libgutenprintui library
Summary(pl.UTF-8):	Biblioteka libgutenprintui
Summary(pt_BR.UTF-8):	Bibliotecas dinâmicas para impressão de alta qualidade
Group:		Libraries
Requires:	libgutenprint = %{version}-%{release}
Obsoletes:	libgimprintui < 5

%description -n libgutenprintui
libgutenprintui library.

%description -n libgutenprintui -l pl.UTF-8
Biblioteka libgutenprintui.

%package -n libgutenprintui-devel
Summary:	Header files for libgutenprintui library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgutenprintui
Summary(pt_BR.UTF-8):	Cabeçalhos e arquivos de desenvolvimento para o libgutenprintui
Group:		Development/Libraries
Requires:	gtk+2-devel >= 2.0.0
Requires:	libgutenprint-devel = %{version}-%{release}
Requires:	libgutenprintui = %{version}-%{release}
Obsoletes:	libgimprintui-devel < 5

%description -n libgutenprintui-devel
Header files for libgutenprintui lirbary.

%description -n libgutenprintui-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgutenprint.

%description -n libgutenprintui-devel -l pt_BR.UTF-8
Este são os arquivos de desenvolvimento para compilar programas com a
biblioteca libgutenprintui.

%package -n libgutenprintui-static
Summary:	libgutenprintui static library
Summary(pl.UTF-8):	Statyczna biblioteka libgutenprintui
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libgutenprintui
Group:		Development/Libraries
Requires:	libgutenprintui-devel = %{version}-%{release}
Obsoletes:	libgimprintui-static < 5

%description -n libgutenprintui-static
libgutenprintui static library.

%description -n libgutenprintui-static -l pl.UTF-8
Biblioteka statyczna libgutenprintui.

%description -n libgutenprintui-static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libgutenprint.

%package -n escputil
Summary:	Tool for Epson ink printers
Summary(pl.UTF-8):	Narzędzie do drukarek atramentowych Epson
Summary(pt_BR.UTF-8):	Ferramenta de manutenção de impressoras ESPSON Stylus (R)
Group:		Applications/Printing
Requires:	libgutenprint = %{version}-%{release}

%description -n escputil
ESPSON Stylus (R) Printers Maintenance tool. This command line tool
can be used to perform the following tests:
- Clean head
- Nozzle check
- Align Head
- Printer Status
- Ink level
- Printer Identify

%description -n escputil -l pl.UTF-8
Działające z linii poleceń narzędzie dla drukarek atramentowych Epson.
Może być użyte do:
- oczyszczenia głowicy
- testu dysz
- wyrównania głowicy
- odczytu stanu drukarki
- odczytu ilości tuszu
- identyfikacji drukarki.

%description -n escputil -l pt_BR.UTF-8
Ferramenta de manutenção de impressoras ESPSON Stylus (R). Esta
ferramenta de linha de comando é usada para executar as seguintes
tarefas:
- Limpeza de cabeçote
- Checagem de Qualidade de impressão
- Alinhamento de cabeçote
- Estado da Impressora
- Nível de tinta
- Identificação da Impressora

%package cups
Summary:	Gutenprint as CUPS plugin
Summary(pl.UTF-8):	Gutenprint jako wtyczka do CUPS
Summary(pt_BR.UTF-8):	Entradas ppd para serem usadas com o cups
Group:		Applications/Printing
Requires:	cups >= 1.2
Requires:	libgutenprint = %{version}-%{release}
Obsoletes:	gimp-print-cups < 5

%description cups
Gutenprint as CUPS plugin.

%description cups -l pl.UTF-8
Wtyczka Gutenprint dla CUPS.

%description cups -l pt_BR.UTF-8
Este pacote contém os arquivos ppd para se usar o driver Gutenprint
com o sistema de impressão cups.

%package samples
Summary:	Gutenprint samples
Summary(pl.UTF-8):	Przykłady do Gutenprinta
Group:		Applications/Printing

%description samples
Gutenprint samples.

%description samples -l pl.UTF-8
Przykłady dla Gutenprinta.

%package -n gimp-plugin-gutenprint
Summary:	print plugin for Gimp
Summary(pl.UTF-8):	Wtyczka print dla Gimpa
Group:		Applications/Printing
Requires:	gimp >= 1:2.4.0
Requires:	libgutenprint = %{version}-%{release}
Obsoletes:	gimp-plugin-print < 5
# obsolete old plugin which used to come with gimp-print/gutenprint,
# not the one that comes with gimp
Obsoletes:	gimp-print < 1:2.0

%description -n gimp-plugin-gutenprint
print plugin for Gimp.

%description -n gimp-plugin-gutenprint -l pl.UTF-8
Wtyczka print dla Gimpa.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4 -I m4local
%{__autoconf}
%{__automake}
%configure \
	--enable-cups-level3-ppds \
	%{!?with_cups:--disable-cups-ppds} \
	%{?debug:--enable-debug} \
	--enable-escputil \
	--enable-libgutenprintui2 \
	--disable-rpath \
	--enable-samples \
	--enable-shared \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--disable-static-genppd \
	--disable-translated-cups-ppds \
	--with-cups%{!?with_cups:=no} \
	--with-gimp2%{!?with_gimp:=no} \
	--with-gimp2-as-gutenprint \
	--with-modules=dlopen
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
%if %{with gimp}
	gimp_plug_indir=%{gimpplugindir}
%endif

rm -rf doc-installed
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gutenprint/doc doc-installed
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gutenprint/samples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/%{majorver}/modules/*.{a,la}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgutenprint*.la
# locales source
%{__rm} $RPM_BUILD_ROOT%{_localedir}/*/gutenprint_*.po

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libgutenprint -p /sbin/ldconfig
%postun	-n libgutenprint -p /sbin/ldconfig

%post	-n libgutenprintui -p /sbin/ldconfig
%postun	-n libgutenprintui -p /sbin/ldconfig

%files -n libgutenprint -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/FAQ.html doc-installed/{gutenprint.pdf,gutenprint-users-manual.pdf}
%attr(755,root,root) %{_libdir}/libgutenprint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgutenprint.so.9
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{majorver}
%dir %{_libdir}/%{name}/%{majorver}/modules
%attr(755,root,root) %{_libdir}/%{name}/%{majorver}/modules/color-traditional.so
%attr(755,root,root) %{_libdir}/%{name}/%{majorver}/modules/print-*.so
%{_libdir}/%{name}/%{majorver}/config.summary
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{majorver}
#%{_mandir}/man7/gutenprint-*.7*

%files -n libgutenprint-devel
%defattr(644,root,root,755)
%doc doc-installed/reference-html
%attr(755,root,root) %{_libdir}/libgutenprint.so
%{_includedir}/gutenprint
%{_pkgconfigdir}/gutenprint.pc
#%{_mandir}/man3/gutenprint.3*

%if %{with static_libs}
%files -n libgutenprint-static
%defattr(644,root,root,755)
%{_libdir}/libgutenprint.a
%endif

%files -n libgutenprintui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgutenprintui2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgutenprintui2.so.2

%files -n libgutenprintui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgutenprintui2.so
%{_includedir}/gutenprintui2
%{_pkgconfigdir}/gutenprintui2.pc

%if %{with static_libs}
%files -n libgutenprintui-static
%defattr(644,root,root,755)
%{_libdir}/libgutenprintui2.a
%endif

%files -n escputil
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/escputil
%attr(755,root,root) %{_bindir}/testpattern
%{_mandir}/man1/escputil.1*

%if %{with cups}
%files cups
%defattr(644,root,root,755)
%doc src/cups/{command.txt,commands}
%{_sysconfdir}/cups/command.types
%attr(755,root,root) %{_bindir}/cups-calibrate
%attr(755,root,root) %{_sbindir}/cups-genppd.%{majorver}
%attr(755,root,root) %{_sbindir}/cups-genppdupdate
%attr(755,root,root) %{cupslibdir}/driver/gutenprint.%{majorver}
%attr(755,root,root) %{cupslibdir}/filter/commandtocanon
%attr(755,root,root) %{cupslibdir}/filter/commandtoepson
%attr(755,root,root) %{cupslibdir}/filter/rastertogutenprint.%{majorver}
%attr(755,root,root) %{cupslibdir}/backend/gutenprint53+usb
%{_datadir}/cups/calibrate.ppm
%dir %{_datadir}/cups/usb
%{_datadir}/cups/usb/net.sf.gimp-print.usb-quirks
%{_mandir}/man8/cups-calibrate.8*
%{_mandir}/man8/cups-genppd.8*
%{_mandir}/man8/cups-genppdupdate.8*
%endif

%files samples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%if %{with gimp}
%files -n gimp-plugin-gutenprint
%defattr(644,root,root,755)
%attr(755,root,root) %{gimpplugindir}/gutenprint
%endif
