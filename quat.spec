Summary:	Generation of 3d fractal objects
Name:		quat
Version:	1.20
Release:	14
Group: 		Graphics
License:	GPLv2+
Url:		https://www.physcip.uni-stuttgart.de/phy11733/quat_e.html
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



%changelog
* Wed Jun 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.20-14
+ Revision: 805421
- rebuild for fltk libs
- cleaned up spec

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.20-13mdv2011.0
+ Revision: 614697
- the mass rebuild of 2010.1 packages

* Mon Jan 18 2010 Jérôme Brenier <incubusss@mandriva.org> 1.20-12mdv2010.1
+ Revision: 493156
- rebuild for new fltk

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.20-11mdv2010.0
+ Revision: 442642
- rebuild

* Sun Dec 14 2008 Funda Wang <fwang@mandriva.org> 1.20-10mdv2009.1
+ Revision: 314176
- fix BR
- fix for new fltk

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.20-8mdv2009.0
+ Revision: 259997
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.20-7mdv2009.0
+ Revision: 247796
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 1.20-5mdv2008.1
+ Revision: 135458
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import quat


* Thu Dec 08 2005 Anssi Hannula <anssi.hannula@gmail.com> 1.20-5mdk
- fix menudir
- mkrel


* Fri Jul 09 2004 Michael Scherer <misc@mandrake.org> 1.20-4mdk 
- rebuild for new gcc

* Tue May 11 2004 Olivier Blin <blino@mandrake.org> 1.20-3mdk
- add clean section
- fix menu section
- fix configure script, fltk-config doesn't support --exec-prefix anymore
- fix menu (it made update-menus segfault, bug #9736)
- quiet setup

* Sun Feb 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.20-2mdk
- rebuild

* Tue Nov 26 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.20-1mdk
- new
