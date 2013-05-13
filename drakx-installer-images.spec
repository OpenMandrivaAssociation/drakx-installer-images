%define	theme	Free

%ifarch %{ix86}
%define kernels kernel-desktop
# kernel-generic
%else
%ifarch ppc
%define kernels kernel-legacy
%else
%define kernels kernel-desktop
%endif
%endif

%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define	family	drakx-installer

Summary:	DrakX installer images
Name:		%{family}-images
Version:	2.0
Release:	1
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.mandriva.com/Tools/DrakX

%rename		%{family}-rescue

BuildRequires:	%{kernels} kernel-firmware
%ifarch %{ix86} x86_64
BuildRequires:	memtest86+
BuildRequires:	grub
BuildRequires:	syslinux >= 4.05-4
%endif
%ifarch ppc
BuildRequires:	yaboot
%endif
#BuildRequires:	drakx-installer-binaries >= 2.0
BuildRequires:	ldetect-lst >= 0.1.291-2
BuildRequires:	mandriva-theme-%{theme}
BuildRequires:	pcmciautils
BuildRequires:	perl-XML-Parser

BuildRequires:	cdrkit-genisoimage
BuildRequires:	mknod-m600
BuildRequires:	mtools uclibc-dosfstools
Buildrequires:	busybox
Buildrequires:	ka-deploy-source-node
BuildRequires:	uclibc-pppoe uclibc-pppd
BuildRequires:	zd1211-firmware


#BuildRequires:	uclibc-mc
# taken from drakx-installer-rescue
BuildRequires:	squashfs-tools
BuildRequires:	ldetect-lst-devel
BuildRequires:	uclibc-hexedit grub rsync openssh-clients uclibc-ncftp strace
BuildRequires:	uclibc-gpart uclibc-parted uclibc-partimage uclibc-e2fsprogs
BuildRequires:	uclibc-dump uclibc-xfsdump uclibc-testdisk extipl
BuildRequires:	uclibc-xfsprogs uclibc-reiserfsprogs uclibc-jfsutils uclibc-btrfs-progs
BuildRequires:	uclibc-mdadm uclibc-lvm2 uclibc-dmraid uclibc-kpartx uclibc-dmraid-events uclibc-dmsetup
BuildRequires:	tcpdump
BuildRequires:	uclibc-mt-st
Buildrequires:	krb5-appl-clients
Buildrequires:	db52-utils
BuildRequires:	packdrake rpmtools
#BuildRequires:	drakx-installer-binaries drakxtools-backend drakx-kbd-mouse-x11
BuildRequires:	bind-utils nfs-utils-clients
BuildRequires:	uclibc-cdialog
BuildRequires:	uclibc-ntfs-3g
BuildRequires:	uclibc-cryptsetup uclibc-photorec quota
BuildRequires:	uclibc-pv
BuildRequires:	uclibc-dropbear screen
BuildRequires:	nilfs-utils
BuildRequires:	uclibc-kmod
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	grub2-theme
BuildRequires:	fbset
BuildRequires:	udhcpc

%description
Images needed to build the Mandriva Linux installer (DrakX).

%prep
%setup -q

%build
THEME=Mandriva-%{theme} make -C images
# KERNELS="%{kernels}"

%install
%makeinstall_std -C images

%files
%dir %{_libdir}/%{family}
%dir %{_libdir}/%{family}/root
%dir %{_libdir}/%{family}/root/install
%{_libdir}/%{family}/root/install/*
#%dir %{_libdir}/%{family}/root/isolinux
#%{_libdir}/%{family}/root/isolinux/*
