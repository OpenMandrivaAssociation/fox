%define major		1.7

%define name		fox
%define version 1.7.46
%define release  1

%define libname		%mklibname %{name} %{major}
%define libnamedev	%mklibname -d %{name}

%define name_ex_apps	%{name}-example-apps

%define icon_name_calc	%{name}-calculator.png
%define icon_name_adie	%{name}-adie.png

#should fix unpacked dir/subdir....
%define _unpackaged_subdirs_terminate_build 0

#debuginfo-without-sources
%define debug_package	%{nil}

Summary:	The FOX C++ GUI Toolkit
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		Development/C++
URL:		http://www.fox-toolkit.org
Source: 	ftp://ftp.fox-toolkit.org/pub/%{name}-%{version}.tar.gz
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
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glut)
BuildRequires:	cups-devel
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	jpeg-devel
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
make GL_LIBS="-lGL -lGLU"

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
%doc LICENSE README
%{_libdir}/*%{major}.so.0*

%files -n %{libnamedev}
%doc doc ADDITIONS TRACING
%doc installed-docs
%doc %{_mandir}/man1/reswrap*
%{_bindir}/reswrap
%{_bindir}/fox-config
%dir %{_includedir}/fox-%{major}
%{_includedir}/fox-%{major}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc





