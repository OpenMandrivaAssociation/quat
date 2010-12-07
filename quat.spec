%define name quat
%define version 1.20
%define release %mkrel 13

Summary:	Generation of 3d fractal objects
Name:		%name
Version:	%version
Release:	%release
Source0:	%{name}-%{version}.tar.bz2
Patch0:		quat-1.20-new-fltk.patch
Url:		http://www.physcip.uni-stuttgart.de/phy11733/quat_e.html
Group: 		Graphics
License:	GPLv2+
BuildRequires:	fltk-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Quat is a program for generation of 3d fractal objects. 
These objects are Julia sets using quaternions. Features 
include calculation of usual images and stereo pair images 
for real 3d views, a user-specified true color palette for 
flexible coloring, 5 iteration formulas, and intersection 
planes to view the interior of the three-dimensional fractal. 

A text mode version for batch calculation is also available. 

%prep
%setup -q
%patch0 -p0

%build
perl -pi -e 's,\`\$FLTK --exec-prefix\`,%{_prefix},' configure
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

rm $RPM_BUILD_ROOT/%_datadir/%name.iss

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=quat
Name=Quat
Comment=Generate 3D fractal objects
Icon=other_sciences
Categories=Science;
EOF

%clean
rm -fr $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%files
%defattr(-,root,root)
%doc COPYING INSTALL 
%_bindir/*
%_datadir/%name
%{_datadir}/applications/mandriva-*.desktop

