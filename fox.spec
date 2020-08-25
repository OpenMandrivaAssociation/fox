%define major		1.7

%define libname		%mklibname %{name} %{major}
%define libnamedev	%mklibname -d %{name}
%define name_ex_apps	%{name}-example-apps

%define icon_name_calc	%{name}-calculator.png
%define icon_name_adie	%{name}-adie.png
%define	debug_package	%nil

%define _disable_rebuild_configure 1

Summary:	The FOX C++ GUI Toolkit
Name:		fox
Version:	1.7.73
Release:	1
License:	LGPLv2+
Group:		Development/C++
URL:		http://www.fox-toolkit.org
Source0:	ftp://ftp.fox-toolkit.org/pub/%{name}-%{version}.tar.gz
Source1:	fox-shutterbug-16.png
Source2:	fox-shutterbug-32.png
Source3:	fox-shutterbug-48.png
Source10:	%{name}_adie_16.png
Source11:	%{name}_adie_32.png
Source12:	%{name}_adie_48.png
Source20:	%{name}_calc_16.png
Source21:	%{name}_calc_32.png
Source22:	%{name}_calc_48.png
BuildRequires:	pkgconfig(glu)
BuildRequires:	cups-devel
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xft)
BuildRequires:	freetype-devel
BuildRequires:	doxygen


%description
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for
3D graphics.  Subclassing of basic FOX widgets allows for easy
extension beyond the built-in widgets by application writers.

%package -n %{name_ex_apps}
Summary:	FOX example applications
Group:		Office
Requires:	%{libname} >= %{version}

%description -n %{name_ex_apps}
Editor, file browser and calculator, written with FOX

%package -n %{libname}
Summary:	The FOX C++ GUI Toolkit - Libraries
Group:		System/Libraries

%description -n %{libname}
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for
3D graphics.  Subclassing of basic FOX widgets allows for easy
extension beyond the built-in widgets by application writers.

%package -n %{libnamedev}
Summary:	FOX header files
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	libfox-devel = %version-%release
Provides:	fox%{major}-devel = %version-%release
Provides:	libfox%{major}-devel = %version-%release
Conflicts:	%mklibname -d fox 1.4
Obsoletes:	%mklibname -d fox 1.7

%description -n %{libnamedev}
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for
3D graphics.  Subclassing of basic FOX widgets allows for easy
extension beyond the built-in widgets by application writers.

This package contains the necessary files to develop applications
with FOX.

%prep
%setup -q

%build
#gw the examples don't link
##define _disable_ld_no_undefined 1
%configure2_5x --with-opengl=mesa --enable-cups LIBS='-lfontconfig'
%make GL_LIBS="-lGL -lGLU"

%install
rm -rf %{buildroot} installed-docs
%makeinstall_std
mv %buildroot%_datadir/doc/fox-%{major}/* installed-docs
cp -p pathfinder/PathFinder %{buildroot}/usr/bin

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-foxcalculator.desktop << EOF
[Desktop Entry]
Name=FOX Calculator
Comment=Calculator using the FOX toolkit
Exec=%{_bindir}/calculator %U
Icon=%{icon_name_calc}
Terminal=false
Type=Application
StartupNotify=true
Categories=Science;Math;
EOF
cat > %{buildroot}%{_datadir}/applications/mandriva-foxadie.desktop << EOF
[Desktop Entry]
Name=FOX Adie
Comment=A.D.I.E. - Advanced Interactive Editor using the FOX toolkit
Exec=%{_bindir}/adie %U
Icon=%{icon_name_adie}
Terminal=false
Type=Application
StartupNotify=true
Categories=TextEditor;Utility;
EOF
cat > %{buildroot}%{_datadir}/applications/mandriva-shutterbug.desktop << EOF
[Desktop Entry]
Name=FOX Shutterbug
Comment=Takes a screenshot and saves it to a file
Exec=%{_bindir}/shutterbug %U
Icon=shutterbug
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;
EOF

install -D -m 644 %{SOURCE10} %{buildroot}%{_miconsdir}/%{icon_name_adie}
install -D -m 644 %{SOURCE11} %{buildroot}%{_iconsdir}/%{icon_name_adie}
install -D -m 644 %{SOURCE12} %{buildroot}%{_liconsdir}/%{icon_name_adie}

install -m 644 %{SOURCE20} %{buildroot}%{_miconsdir}/%{icon_name_calc}
install -m 644 %{SOURCE21} %{buildroot}%{_iconsdir}/%{icon_name_calc}
install -m 644 %{SOURCE22} %{buildroot}%{_liconsdir}/%{icon_name_calc}

install -m 644 %{SOURCE1} %{buildroot}%{_miconsdir}/shutterbug.png
install -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/shutterbug.png
install -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/shutterbug.png

rm -rf %buildroot%_prefix/fox

%files -n %{name_ex_apps}
%doc %{_mandir}/man1/ControlPanel*
%doc %{_mandir}/man1/PathFinder*
%doc %{_mandir}/man1/adie*
%doc %{_mandir}/man1/calculator*
%doc %{_mandir}/man1/shutterbug.1*
%{_bindir}/calculator
%{_bindir}/ControlPanel
%{_bindir}/PathFinder
%{_bindir}/adie
%{_bindir}/Adie.stx
%{_bindir}/shutterbug
%{_datadir}/applications/mandriva*
%{_miconsdir}/%{icon_name_adie}
%{_iconsdir}/%{icon_name_adie}
%{_liconsdir}/%{icon_name_adie}
%{_miconsdir}/%{icon_name_calc}
%{_iconsdir}/%{icon_name_calc}
%{_liconsdir}/%{icon_name_calc}
%{_miconsdir}/shutterbug.png
%{_iconsdir}/shutterbug.png
%{_liconsdir}/shutterbug.png

%files -n %{libname}
%doc AUTHORS LICENSE README
%{_libdir}/*%{major}.so.0*

%files -n %{libnamedev}
%doc doc ADDITIONS INSTALL TRACING
%doc installed-docs
%doc %{_mandir}/man1/reswrap*
%{_bindir}/reswrap
%{_bindir}/fox-config
%dir %{_includedir}/fox-%{major}
%{_includedir}/fox-%{major}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc




%changelog
* Mon Feb 13 2012 Andrey Bondrov <abondrov@mandriva.org> 1.7.32-1mdv2012.0
+ Revision: 773779
- New version 1.7.32

* Wed May 18 2011 Funda Wang <fwang@mandriva.org> 1.7.26-1
+ Revision: 676055
- update file list
- there is no config now
- clean spec
- update to new version 1.7.26

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 1.7.25-2
+ Revision: 640437
- rebuild to obsolete old packages

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1.7.25-1
+ Revision: 636289
- update to new version 1.7.25

* Sat Feb 05 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.7.23-1
+ Revision: 636201
- update build deps
- update to new version 1.7.23

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.21-3mdv2011.0
+ Revision: 610742
- rebuild

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 1.7.21-2mdv2010.1
+ Revision: 492244
- rebuild for new libjpeg v8

* Tue Dec 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.7.21-1mdv2010.1
+ Revision: 479067
- update to new version 1.7.21

* Wed Aug 19 2009 Frederik Himpe <fhimpe@mandriva.org> 1.7.20-1mdv2010.0
+ Revision: 418242
- update to new version 1.7.20

* Sat Mar 07 2009 Emmanuel Andry <eandry@mandriva.org> 1.7.19-1mdv2009.1
+ Revision: 351904
- New version 1.7.19

* Mon Dec 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.7.18-1mdv2009.1
+ Revision: 311757
- fix build deps
- new version
- fix build
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 07 2007 Funda Wang <fwang@mandriva.org> 1.7.13-1mdv2008.1
+ Revision: 116222
- New version 1.7.13
- drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.7.11-1mdv2008.0
+ Revision: 57706
- new version
- new devel name


* Wed Dec 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.7.6-1mdv2007.0
+ Revision: 91604
- Import fox

* Wed Dec 06 2006 Götz Waschk <waschk@mandriva.org> 1.7.6-1mdv2007.1
- New version 1.7.6

* Tue Aug 01 2006 Götz Waschk <waschk@mandriva.org> 1.7.1-1mdv2007.0
- new major
- New release 1.7.1

* Mon Jul 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.10-1mdv2007.0
- New release 1.6.10

* Wed Jul 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.9-1
- New release 1.6.9

* Wed Jul 19 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.8-1mdv2007.0
- New release 1.6.8

* Sat Jun 24 2006 Götz Waschk <waschk@mandriva.org> 1.6.6-2mdv2007.0
- xdg menu

* Fri Jun 16 2006 Götz Waschk <waschk@mandriva.org> 1.6.6-1mdv2007.0
- update file list
- fix buildrequires
- New release 1.6.6

* Thu Apr 20 2006 Götz Waschk <waschk@mandriva.org> 1.6.4-1mdk
- add devel conflict
- New release 1.6.4

* Wed Apr 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.3-1mdk
- New release 1.6.3

* Thu Apr 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.2-1mdk
- New release 1.6.2

* Mon Apr 03 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.1-1mdk
- New release 1.6.1

* Tue Mar 21 2006 Götz Waschk <waschk@mandriva.org> 1.6.0-1mdk
- new major
- New release 1.6.0

* Fri Dec 16 2005 Götz Waschk <waschk@mandriva.org> 1.4.27-1mdk
- fix configure call
- New release 1.4.27
- use mkrel

* Wed Nov 16 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4.24-1mdk
- New release 1.4.24

* Tue Nov 08 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4.22-1mdk
- New release 1.4.22

* Sun Oct 30 2005 Götz Waschk <waschk@mandriva.org> 1.4.21-1mdk
- disable parallel build
- New release 1.4.21

* Thu Oct 27 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4.20-1mdk
- New release 1.4.20

* Sat Sep 10 2005 Olivier Blin <oblin@mandriva.com> 1.4.17-2mdk
- fix typo in summary

* Wed Aug 03 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4.17-1mdk
- New release 1.4.17

* Mon Jun 13 2005 Götz Waschk <waschk@mandriva.org> 1.4.16-1mdk
- New release 1.4.16

* Wed Jun 08 2005 Götz Waschk <waschk@mandriva.org> 1.4.15-1mdk
- New release 1.4.15

* Wed Apr 27 2005 Götz Waschk <waschk@mandriva.org> 1.4.12-1mdk
- New release 1.4.12

* Thu Apr 07 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.4.11-1mdk
- New release 1.4.11

* Thu Mar 17 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.4.8-1mdk
- New release 1.4.8

* Thu Mar 10 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.4.7-1mdk
- New release 1.4.7

* Wed Feb 23 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.4.6-1mdk
- New release 1.4.6

* Tue Feb 15 2005 Götz Waschk <waschk@linux-mandrake.com> 1.4.4-1mdk
- update file list
- New release 1.4.4

* Wed Oct 13 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.11-1mdk
- New release 1.2.11

* Sat Aug 14 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.8-1mdk
- New release 1.2.8

* Wed Jul 14 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.7-1mdk
- New release 1.2.7

* Mon Jul 05 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.6-1mdk
- new version

* Fri Jun 25 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.5-1mdk
- fix devel provides
- New release 1.2.5

* Thu Jun 17 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.4-1mdk
- New release 1.2.4

* Wed Jun 09 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.3-1mdk
- fix installation
- New release 1.2.3

* Thu May 20 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.1-1mdk
- new major
- New release 1.2.1

* Tue May 18 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.0-1mdk
- new major 1.1
- New release 1.2.0

* Tue Apr 27 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.53-1mdk
- new major
- new version

* Wed Apr 21 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.52-1mdk
- new major
- new version

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.51-1mdk
- new version

* Mon Mar 15 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.49-1mdk
- new version

* Fri Mar 05 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.47-1mdk
- new version

* Mon Feb 09 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.46-1mdk
- new version

* Thu Jan 22 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.45-1mdk
- new version

* Mon Jan 19 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1.44-1mdk
- fix file list
- new version

