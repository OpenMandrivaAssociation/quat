Summary:	Generation of 3d fractal objects
Name:		quat
Version:	1.20
Release:	14
Group: 		Graphics
License:	GPLv2+
Url:		http://www.physcip.uni-stuttgart.de/phy11733/quat_e.html
Source0:	%{name}-%{version}.tar.bz2
Patch0:		quat-1.20-new-fltk.patch
BuildRequires:	fltk-devel

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
%makeinstall_std

rm -f %{buildroot}/%{_datadir}/%{name}.iss

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=quat
Name=Quat
Comment=Generate 3D fractal objects
Icon=other_sciences
Categories=Science;
EOF

%files
%doc COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

