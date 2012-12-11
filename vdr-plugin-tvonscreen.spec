
%define plugin	tvonscreen
%define name	vdr-plugin-%plugin
%define version	1.0.141
%define rel	12

# backportability
%define _localstatedir %{_var}

Summary:	VDR plugin: Shows the EPG info in form of a typical TV magazine
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.js-home.org/vdr/tvonscreen/
Source:		vdr-%plugin-%version.tar.bz2
# dpatches from e-tobi repo
Patch0:		02_tvonscreen-1.0-fixes.dpatch
Patch1:		90_tvonscreen-1.0.141-1.5.3.dpatch
Patch2:		tvonscreen-1.0.141-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugins shows the EPG data in the typical way a TV magazine
does. The channels are shown from left to right, 3 on one screen.

You can scroll though the channels and the time, create timers,
show details, search for events and add vdradmin auto timers.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# optional path for the XPM channel logos
var=CHANLOGOS
param="-l CHANLOGOS"
default=%{_vdr_chanlogodir}
# path and filename to vdradmin at file
var=VDRADMIN_TIMERFILE
param="-v VDRADMIN_TIMERFILE"
default=%{_localstatedir}/lib/vdradmin/vdradmin.at
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.0.141-12mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.0.141-11mdv2009.1
+ Revision: 359379
- rebuild for new vdr
- define %%_localstatedir locally for backportability

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 1.0.141-10mdv2009.0
+ Revision: 197992
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 1.0.141-9mdv2009.0
+ Revision: 197737
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.5.3 (P1 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 1.0.141-8mdv2008.1
+ Revision: 145237
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 1.0.141-7mdv2008.1
+ Revision: 103226
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 1.0.141-6mdv2008.0
+ Revision: 50060
- rebuild for new vdr

* Fri Jun 22 2007 Anssi Hannula <anssi@mandriva.org> 1.0.141-5mdv2008.0
+ Revision: 42702
- rebuild due to buildsystem failure
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 1.0.141-3mdv2008.0
+ Revision: 22718
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 1.0.141-2mdv2007.0
+ Revision: 90981
- rebuild for new vdr

* Wed Nov 29 2006 Anssi Hannula <anssi@mandriva.org> 1.0.141-1mdv2007.1
+ Revision: 88577
- Import vdr-plugin-tvonscreen

