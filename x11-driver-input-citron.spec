Name: x11-driver-input-citron
Version: 2.2.1
Release: %mkrel 5
Summary: X.org input driver for Citron Infrared Touch (CiTouch) devices
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-citron-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.4
BuildRequires: x11-server-devel >= 1.4
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: x11-server < 1.4

Patch1: 0001-Don-t-call-missing-functions-xf86SoundKbdBell-and-xf.patch

%description
Citron is a Xorg input driver for Citron Infrared Touch devices (CiTouch).

%prep
%setup -q -n xf86-input-citron-%{version}

%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/citron_drv.la
%{_libdir}/xorg/modules/input/citron_drv.so
%{_mandir}/man4/citron.*
