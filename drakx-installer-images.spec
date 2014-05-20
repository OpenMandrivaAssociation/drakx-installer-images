%define	theme	Moondrake

%if "%{kernels}" == "%%{kernels}"
%ifarch %{ix86}
%global kernels kernel-nrjQL-desktop-latest
# kernel-generic
%else
%ifarch ppc
%global kernels kernel-legacy
%else
%global kernels kernel-nrjQL-desktop-latest
%endif
%endif
%endif

%define	kernel	%(rpm -q --qf '%{REQUIRENAME}\n' kernel-nrjQL-desktop-latest)

%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define	family	drakx-installer

Summary:	DrakX installer images
Name:		%{family}-images
Version:	2.5
Release:	1
Source0:	%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.mandriva.com/Tools/DrakX

%rename		%{family}-rescue

BuildRequires:	%{kernels} kernel-firmware
BuildRequires:	zd1211-firmware
BuildRequires:	atmel-firmware isicom-firmware
BuildRequires:	iwlwifi-agn-ucode
%ifarch %{ix86} x86_64
BuildRequires:	memtest86+
BuildRequires:	grub
BuildRequires:	syslinux >= 4.05-4
%endif
%ifarch ppc
BuildRequires:	yaboot
%endif
BuildRequires:	ldetect-lst >= 0.1.291-2
BuildRequires:	mandriva-theme-%{theme}
BuildRequires:	pcmciautils
BuildRequires:	perl-XML-Parser
BuildRequires:	drakx-kbd-mouse-x11
BuildRequires:	termcap gpm lvm2 dmraid-events pciutils setserial smartmontools linux_logo
BuildRequires:	krb5-appl-clients

BuildRequires:	cdrkit-genisoimage
BuildRequires:	mknod-m600
BuildRequires:	dosfstools
BuildRequires:	mtools uclibc-dosfstools
Buildrequires:	busybox
#Buildrequires:	ka-deploy-source-node
BuildRequires:	uclibc-pppoe uclibc-pppd
BuildRequires:	prelink
BuildRequires:	fonts-ttf-liberation


#BuildRequires:	uclibc-mc
# taken from drakx-installer-rescue
BuildRequires:	uclibc-squashfs-tools uclibc-udev
BuildRequires:	ldetect-lst-devel
BuildRequires:	uclibc-hexedit grub2 uclibc-rsync openssh-clients uclibc-ncftp uclibc-strace
BuildRequires:	uclibc-gpart uclibc-parted uclibc-partimage uclibc-e2fsprogs
BuildRequires:	uclibc-dump uclibc-xfsdump uclibc-testdisk
BuildRequires:	uclibc-xfsprogs uclibc-reiserfsprogs uclibc-jfsutils uclibc-btrfs-progs
BuildRequires:	uclibc-lvm2 uclibc-dmraid uclibc-kpartx uclibc-dmraid-events uclibc-dmsetup
BuildRequires:	uclibc-mdadm uclibc-sg3_utils uclibc-smartmontools
BuildRequires:	tcpdump
BuildRequires:	uclibc-mt-st uclibc-file uclibc-ncurses
Buildrequires:	uclibc-db52-utils
# include tools for generating metadata? yeah right..
#BuildRequires:	packdrake rpmtools
BuildRequires:	drakx-installer-binaries #drakxtools-backend drakx-kbd-mouse-x11
BuildRequires:	uclibc-cdialog
BuildRequires:	uclibc-ntfs-3g
BuildRequires:	uclibc-cryptsetup uclibc-photorec uclibc-quota
BuildRequires:	uclibc-pv
BuildRequires:	uclibc-dropbear uclibc-screen
BuildRequires:	uclibc-ddrescue
BuildRequires:	uclibc-nilfs-utils
BuildRequires:	uclibc-kmod
BuildRequires:	uclibc-hdparm uclibc-dmidecode
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	grub2-theme
BuildRequires:	uclibc-udhcp
# only needed for /etc/fb.modes
BuildRequires:	fbset

BuildRequires:	extipl


%description
Images needed to build the Mandriva Linux installer (DrakX).

%prep
%setup -q

%build
THEME=Mandriva-%{theme} make -C images KERNELS="$(rpm -q --requires %{kernels} |grep kernel)"

%install
%makeinstall_std -C images

%files
%dir %{_libdir}/%{family}
%dir %{_libdir}/%{family}/root
%dir %{_libdir}/%{family}/root/install
%dir %{_libdir}/%{family}/root/install/images/
%{_libdir}/%{family}/root/install/images/all.cpio.xz
%dir %{_libdir}/%{family}/root/grub
%{_libdir}/%{family}/root/grub/*
#%dir %{_libdir}/%{family}/root/isolinux
#%{_libdir}/%{family}/root/isolinux/*
