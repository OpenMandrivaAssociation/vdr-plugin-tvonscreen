%define plugin	tvonscreen

# backportability
%define _localstatedir %{_var}

Summary:	VDR plugin: Shows the EPG info in form of a typical TV magazine
Name:		vdr-plugin-%plugin
Version:	1.0.141
Release:	15
Group:		Video
License:	GPL
URL:		https://www.js-home.org/vdr/tvonscreen/
Source:		vdr-%plugin-%{version}.tar.bz2
# dpatches from e-tobi repo
Patch0:		02_tvonscreen-1.0-fixes.dpatch
Patch1:		90_tvonscreen-1.0.141-1.5.3.dpatch
Patch2:		tvonscreen-1.0.141-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugins shows the EPG data in the typical way a TV magazine
does. The channels are shown from left to right, 3 on one screen.

You can scroll though the channels and the time, create timers,
show details, search for events and add vdradmin auto timers.

%prep
%setup -q -n %plugin-%{version}
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
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY




