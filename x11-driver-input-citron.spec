Name: x11-driver-input-citron
Version: 2.2.1
Release: %mkrel 2
Summary: X.org input driver for Citron Infrared Touch (CiTouch) devices
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-citron xorg/drivers/xf86-input-citron
# cd xorg/drivers/xf86-input-citron
# git-archive --format=tar --prefix=xf86-input-citron-2.2.1/ xf86-input-citron-2.2.1 | bzip2 -9 > xf86-input-citron-2.2.1.tar.bz2
########################################################################
Source0: xf86-input-citron-%{version}.tar.bz2
License: MIT

########################################################################
# git-format-patch xf86-input-citron-2.2.1..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.4
BuildRequires: x11-server-devel >= 1.4
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: x11-server < 1.4

%description
Citron is a Xorg input driver for Citron Infrared Touch devices (CiTouch).
THIS DRIVER IS BROKEN:
Missing symbols xf86SoundKbdBell and xf86XInputSetSendCoreEvents no longer
present due to X Input Hotplug rework.

%prep
%setup -q -n xf86-input-citron-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
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
