Name: x11-driver-input-citron
Version: 2.2.0
Release: %mkrel 2
Summary: X.org input driver for Citron Infrared Touch (CiTouch) devices
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-citron-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
Citron is a Xorg input driver for Citron Infrared Touch devices (CiTouch).

%prep
%setup -q -n xf86-input-citron-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/citron_drv.la
%{_libdir}/xorg/modules/input/citron_drv.so
%{_mandir}/man4/citron.4.bz2


