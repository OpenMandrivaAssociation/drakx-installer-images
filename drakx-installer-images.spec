%define	theme	Free

%ifarch %{ix86}
%define kernels kernel-desktop kernel-generic
%else
%ifarch ppc
%define kernels kernel-legacy
%else
%define kernels kernel-desktop kernel-server
%endif
%endif

%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define	family	drakx-installer

Summary:	DrakX installer images
Name:		%{family}-images
Version:	1.57
Release:	1
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.mandriva.com/Tools/DrakX
BuildRequires:	%{kernels} kernel-firmware
%ifarch %{ix86} x86_64
BuildRequires:	memtest86+
BuildRequires:	grub
BuildRequires:	syslinux >= 4.05-4
%endif
%ifarch ppc
BuildRequires:	yaboot
%endif
BuildRequires:	drakx-installer-binaries >= 1.55
BuildRequires:	ldetect-lst >= 0.1.291-2
BuildRequires:	mandriva-theme-%{theme}
BuildRequires:	pcmciautils
BuildRequires:	perl-XML-Parser

BuildRequires:	cdrkit-genisoimage
BuildRequires:	mknod-m600
BuildRequires:	mtools dosfstools
Buildrequires:	busybox-static
Buildrequires:	ka-deploy-source-node
BuildRequires:	uclibc-pppoe uclibc-pppd
BuildRequires:	zd1211-firmware

%description
Images needed to build the Mandriva Linux installer (DrakX).

%prep
%setup -q

%build
THEME=Mandriva-%{theme} make -C images KERNELS="%{kernels}"

%install
%makeinstall_std -C images

%files
%dir %{_libdir}/%{family}
%dir %{_libdir}/%{family}/root
%dir %{_libdir}/%{family}/root/install
%{_libdir}/%{family}/root/install/*
%dir %{_libdir}/%{family}/root/isolinux
%{_libdir}/%{family}/root/isolinux/*
