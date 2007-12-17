%define name quat
%define version 1.20
%define release %mkrel 5

Summary:	Generation of 3d fractal objects
Name:		%name
Version:	%version
Release:	%release
Source0:	%{name}-%{version}.tar.bz2
Url:		http://www.physcip.uni-stuttgart.de/phy11733/quat_e.html
Group: 		Graphics
License:	GPL
BuildRequires:	libfltk-devel

%description
Quat is a program for generation of 3d fractal objects. 
These objects are Julia sets using quaternions. Features 
include calculation of usual images and stereo pair images 
for real 3d views, a user-specified true color palette for 
flexible coloring, 5 iteration formulas, and intersection 
planes to view the interior of the three-dimensional fractal. 

A text mode version for batch calculation is also available. 

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

perl -pi -e 's,\`\$FLTK --exec-prefix\`,%{_prefix},' configure
%configure

%make

%install

%makeinstall

rm $RPM_BUILD_ROOT/%_datadir/%name.iss

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): command="quat" title="Quat" longtitle="Generate 3D fractal objects" needs="x11" icon="other_sciences.png" section="More Applications/Sciences/Other"
EOF

%clean
rm -fr $RPM_BUILD_ROOT

%post
%update_menus

%postun
%update_menus

%files
%defattr(-,root,root)
%doc COPYING INSTALL 
%_bindir/*
%_datadir/%name
%_menudir/*

