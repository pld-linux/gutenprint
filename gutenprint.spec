#
# Conditional build:
%bcond_without	cups		# don't build CUPS plugin
%bcond_without	gimp		# build GIMP plugin subpackage
%bcond_without	ijs		# don't build IJS server for Ghostscript
%bcond_without	foomatic	# don't generate foomatic data
#
# TODO:
# - port info_and_pdf_only.patch and install documentation in correct place.
# - think about not including PPDs in package and allow generation by cups-genppd
#
%include	/usr/lib/rpm/macros.perl
Summary:	Collection of high-quality printer drivers
Summary(pl):	Zestaw wysokiej jako¶ci sterowników do drukarek
Name:		gutenprint
Version:	5.0.0
%define	bver	rc1
Release:	0.%{bver}.1
License:	GPL
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/gimp-print/%{name}-%{version}-%{bver}.tar.bz2
# Source0-md5:	4ac4602e81713825665435205661bbd1
Patch0:		%{name}-usb.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-static.patch
# http://gutenprint.sf.net/ not ready yet
URL:		http://gimp-print.sf.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_cups:BuildRequires:	cups-devel >= 1.1.15}
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-utils
%{?with_foomatic:BuildRequires:	foomatic-db-engine >= 2.9.1}
BuildRequires:	gettext-autopoint
%{?with_ijs:BuildRequires:	ghostscript-ijs-devel}
%{?with_gimp:BuildRequires:	gimp-devel >= 1:2.0.0}
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 3.0.3-16
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

%description -l pl
Gutenprint to zbiór bardzo wysokiej jako¶ci sterowników do drukarek
dla systemów UNIX/Linux. Celem tego projektu jest jak najlepsza jako¶æ
wydruku. Do³±czone do tego pakietu s±: wtyczka dla programu GIMP (st±d
nazwa), sterownik CUPS i sterownik Ghostscriptu. Sterownik umo¿liwia
bezpo¶redni± wspó³pracê z wieloma kolejkami wydruku. Dodatkowo
do³±czonych jest wiele programów do obs³ugi drukarki. Wielu
u¿ytkowników twierdzi ze jako¶æ wydruków na najlepszych drukarkach
Epson Stylus dorównuje albo nawet przerasta jako¶ci± to, co jest
oferowane przez sterowniki dla Windows i MacOS.

Ten pakiet wcze¶niej nazywa³ siê gimp-print.

%package -n libgutenprint
Summary:	libgutenprint library
Summary(pl):	Biblioteka libgutenprint
Summary(pt_BR):	Bibliotecas dinâmicas para impressão de alta qualidade
Group:		Libraries
# uncomment when it becomes stable
#Obsoletes:	gimp-print-lib
Obsoletes:	libgimprint

%description -n libgutenprint
libgutenprint library.

%description -n libgutenprint -l pl
Biblioteka libgutenprint.

%package -n libgutenprint-devel
Summary:	Header files for libgutenprint library
Summary(pl):	Pliki nag³ówkowe biblioteki libgutenprint
Summary(pt_BR):	Cabeçalhos e arquivos de desenvolvimento para o libgutenprint
Group:		Development/Libraries
Requires:	libgutenprint = %{version}-%{release}
#Obsoletes:	gimp-print-devel
Obsoletes:	libgimpprint-devel

%description -n libgutenprint-devel
Header files for libgutenprint library.

%description -n libgutenprint-devel -l pl
Pliki nag³ówkowe biblioteki libgutenprint.

%description -n libgutenprint-devel -l pt_BR
Este são os arquivos de desenvolvimento para compilar programas com a
biblioteca libgutenprint.

%package -n libgutenprint-static
Summary:	libgutenprint static library
Summary(pl):	Statyczna biblioteka libgutenprint
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libgutenprint
Group:		Development/Libraries
Requires:	libgutenprint-devel = %{version}-%{release}
#Obsoletes:	gimp-print-static
Obsoletes:	libgimprint-static

%description -n libgutenprint-static
libgutenprint static library.

%description -n libgutenprint-static -l pl
Biblioteka statyczna libgutenprint.

%description -n libgutenprint-static -l pt_BR
Bibliotecas estáticas para desenvolvimento com libgutenprint.

%package -n libgutenprintui
Summary:	libgutenprintui library
Summary(pl):	Biblioteka libgutenprintui
Summary(pt_BR):	Bibliotecas dinâmicas para impressão de alta qualidade
Group:		Libraries
Requires:	libgutenprint = %{version}-%{release}
Obsoletes:	libgimprintui

%description -n libgutenprintui
libgutenprintui library.

%description -n libgutenprintui -l pl
Biblioteka libgutenprintui.

%package -n libgutenprintui-devel
Summary:	Header files for libgutenprintui library
Summary(pl):	Pliki nag³ówkowe biblioteki libgutenprintui
Summary(pt_BR):	Cabeçalhos e arquivos de desenvolvimento para o libgutenprintui
Group:		Development/Libraries
Requires:	libgutenprintui = %{version}-%{release}
Requires:	libgutenprint-devel = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0.0
Obsoletes:	libgimprintui-devel

%description -n libgutenprintui-devel
Header files for libgutenprintui lirbary.

%description -n libgutenprintui-devel -l pl
Pliki nag³ówkowe biblioteki libgutenprint.

%description -n libgutenprintui-devel -l pt_BR
Este são os arquivos de desenvolvimento para compilar programas com a
biblioteca libgutenprintui.

%package -n libgutenprintui-static
Summary:	libgutenprintui static library
Summary(pl):	Statyczna biblioteka libgutenprintui
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libgutenprintui
Group:		Development/Libraries
Requires:	libgutenprintui-devel = %{version}-%{release}
Obsoletes:	libgimprintui-static

%description -n libgutenprintui-static
libgutenprintui static library.

%description -n libgutenprintui-static -l pl
Biblioteka statyczna libgutenprintui.

%description -n libgutenprintui-static -l pt_BR
Bibliotecas estáticas para desenvolvimento com libgutenprint.

%package -n escputil
Summary:	Tool for Epson ink printers
Summary(pl):	Narzêdzie do drukarek atramentowych Epson
Summary(pt_BR):	Ferramenta de manutenção de impressoras ESPSON Stylus (R)
Group:		Applications/Printing

%description -n escputil
ESPSON Stylus (R) Printers Maintenance tool. This command line tool
can be used to perform the following tests:
- Clean head
- Nozzle check
- Align Head
- Printer Status
- Ink level
- Printer Identify

%description -n escputil -l pl
Dzia³aj±ce z linii poleceñ narzêdzie dla drukarek atramentowych Epson.
Mo¿e byæ u¿yte do:
- oczyszczenia g³owicy
- testu dysz
- wyrównania g³owicy
- odczytu stanu drukarki
- odczytu ilo¶ci tuszu
- identyfikacji drukarki.

%description -n escputil -l pt_BR
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
Summary(pl):	Gutenprint jako wtyczka do CUPS
Summary(pt_BR):	Entradas ppd para serem usadas com o cups
Group:		Applications/Printing
Requires:	libgutenprint = %{version}-%{release}
Requires:	cups >= 1.1.15
Obsoletes:	gimp-print-cups

%description cups
Gutenprint as CUPS plugin.

%description cups -l pl
Wtyczka Gutenprint dla CUPS.

%description cups -l pt_BR
Este pacote contém os arquivos ppd para se usar o driver Gutenprint
com o sistema de impressão cups.

%package samples
Summary:	Gutenprint samples
Summary(pl):	Przyk³ady do Gutenprinta
Group:		Applications/Printing

%description samples
Gutenprint samples.

%description samples -l pl
Przyk³ady dla Gutenprinta.

%package ijs
Summary:	gutenprint IJS driver for GhostScript
Summary(pl):	Sterownik IJS gutenprint dla GhostScripta
Group:		Applications/Printing
Requires:	libgutenprint = %{version}-%{release}
Obsoletes:	gimp-print-ijs

%description ijs
gutenprint IJS driver for GhostScript.

%description ijs -l pl
Sterownik IJS gutenprint dla GhostScripta.

%package -n foomatic-db-gutenprint
Summary:	foomatic data for gutenprint IJS driver
Summary(pl):	Dane foomatic dla sterownika IJS gutenprint
Group:		Applications/Printing
Requires:	%{name}-ijs = %{version}-%{release}
Requires:	foomatic-db-engine >= 2.9.1
Obsoletes:	foomatic-db-gimp-print

%description -n foomatic-db-gutenprint
foomatic data for gimp-print IJS driver.

%description -n foomatic-db-gutenprint -l pl
Dane foomatic dla sterownika IJS gutenprint.

%package -n gimp-plugin-print
Summary:	print plugin for Gimp
Summary(pl):	Wtyczka print dla Gimpa
Group:		Applications/Print
Requires:	libgutenprint = %{version}-%{release}
Requires:	gimp >= 1:2.0.0
Obsoletes:	gimp-print

%description -n gimp-plugin-print
print plugin for Gimp.

%description -n gimp-plugin-print -l pl
Wtyczka print dla Gimpa.

%prep 
%setup -q -n %{name}-%{version}-%{bver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

echo 'AC_DEFUN([AM_PATH_GTK],[$3])' > m4/gtk.m4
%{__sed} -i 's,AM_PATH_GLIB,,' m4/stp_gimp.m4

%build
rm -f m4extra/{libtool.m4,gettext.m4,lcmessage.m4,progtest.m4}
%{?with_gimp:rm -f m4extra/gimp.m4}
%{__libtoolize}
%{__autopoint}
%{__aclocal} -I m4 -I m4extra
%{__automake}
%{__autoconf}

%configure \
	%{?debug:--enable-debug} \
	--with%{!?with_cups:out}-cups \
	--without-gimp \
	--with%{!?with_gimp:out}-gimp2 \
	--with%{!?with_ijs:out}-ijs \
	--with%{!?with_foomatic:out}-foomatic \
	--with%{!?with_foomatic:out}-foomatic3 \
	%{?with_static_libs:--enable-static} \
	--with-modules=dlopen \
	--enable-escputil \
	%{!?with_cups:--disable-cups-ppds} \
	--disable-libgutenprintui \
	--disable-rpath \
	--disable-static-genppd \
	--disable-translated-cups-ppds \
	--enable-cups-level3-ppds \
	--enable-lexmarkutil \
	--enable-libgutenprintui2 \
	--enable-samples \
	--enable-shared \
	--enable-user-guide \
	--enable-xmldef \
	--without-ghost 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
%if %{with gimp}
	gimp_plug_indir=%{gimpplugindir}
%endif

mv -f $RPM_BUILD_ROOT%{_datadir}/gutenprint/doc doc-installed
mv -f $RPM_BUILD_ROOT%{_datadir}/gutenprint/samples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with cups}
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/update-cups-genppd.8
echo '.so cups-genppdconfig.8' > $RPM_BUILD_ROOT%{_mandir}/man8/update-cups-genppd.8
%endif

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}*/modules/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libgutenprint -p /sbin/ldconfig
%postun	-n libgutenprint -p /sbin/ldconfig

%post	-n libgutenprintui -p /sbin/ldconfig
%postun	-n libgutenprintui -p /sbin/ldconfig

%files -n libgutenprint -f %{name}.lang
%defattr(644,root,root,755)
%doc doc-installed/{gutenprint.pdf,html,users-guide.pdf}
%doc doc/FAQ.html AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgutenprint.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}*
%dir %{_libdir}/%{name}/%{version}*/modules
%attr(755,root,root) %{_libdir}/%{name}/%{version}*/modules/*.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{version}*
#%{_mandir}/man7/gutenprint-*.7*

%files -n libgutenprint-devel
%defattr(644,root,root,755)
%doc doc-installed/reference-html
%attr(755,root,root) %{_libdir}/libgutenprint.so
%{_libdir}/libgutenprint.la
%{_includedir}/gutenprint
%{_pkgconfigdir}/gutenprint.pc
#%{_mandir}/man3/gutenprint.3*

%files -n libgutenprint-static
%defattr(644,root,root,755)
%{_libdir}/libgutenprint.a

%files -n libgutenprintui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgutenprintui2.so.*.*

%files -n libgutenprintui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgutenprintui2.so
%{_libdir}/libgutenprintui2.la
%{_includedir}/gutenprintui2
%{_pkgconfigdir}/gutenprintui2.pc

%files -n libgutenprintui-static
%defattr(644,root,root,755)
%{_libdir}/libgutenprintui2.a

%files -n escputil
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/escputil
%{_mandir}/man1/escputil.1*

%if %{with cups}
%files cups
%defattr(644,root,root,755)
%doc src/cups/{README,command.txt,commands}
%{_sysconfdir}/cups/command.types
%attr(755,root,root) %{_bindir}/cups-*
%attr(755,root,root) %{_sbindir}/cups-*
%{_datadir}/cups/calibrate.ppm
%dir %{_datadir}/cups/model/gutenprint
%dir %{_datadir}/cups/model/gutenprint/*
%{_datadir}/cups/model/gutenprint/*/C
%attr(755,root,root) %{cupslibdir}/backend/*
%attr(755,root,root) %{cupslibdir}/filter/*
%{_mandir}/man8/*cups*.8*
%endif

%files samples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%if %{with ijs}
%files ijs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijsgutenprint*
%{_mandir}/man1/ijsgutenprint.1*
%endif

%if %{with foomatic}
%files -n foomatic-db-gutenprint
%defattr(644,root,root,755)
%{_datadir}/foomatic/db/source/driver/*
%{_datadir}/foomatic/db/source/opt/*
%endif

%if %{with gimp}
%files -n gimp-plugin-print
%defattr(644,root,root,755)
%attr(755,root,root) %{gimpplugindir}/print
%endif
