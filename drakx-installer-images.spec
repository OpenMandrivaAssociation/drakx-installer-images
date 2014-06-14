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
Version:	2.6
Release:	3
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
#BuildConflicts:	distro-release-OpenMandriva
BuildConflicts:	distro-theme-OpenMandriva distro-theme-OpenMandriva-grub2
BuildRequires:	distro-theme-Moondrake distro-release-Moondrake distro-theme-Moondrake-grub2


%description
Images needed to build the Mandriva Linux installer (DrakX).

%prep
%setup -q
# workaround multiple threads consuming all of 32 bit address space
%ifarch %{ix86}
find -type f |xargs sed -e 's#xz -T0#xz#g' -i
%endif

%build
THEME=Mandriva-%{theme} make -C images KERNELS="$(rpm -q --requires %{kernels} |grep kernel)"

%install
%makeinstall_std -C images

%files
%dir %{_libdir}/%{family}
%dir %{_libdir}/%{family}/root
%dir %{_libdir}/%{family}/root/install
%dir %{_libdir}/%{family}/root/install/images/
%{_libdir}/%{family}/root/install/images/MD5SUM
%{_libdir}/%{family}/root/install/images/boot.iso
%{_libdir}/%{family}/root/install/images/hd_grub.img
%dir %{_libdir}/%{family}/root/grub
%{_libdir}/%{family}/root/grub/VERSION
%dir %{_libdir}/%{family}/root/grub/%{_target_cpu}/
%dir %{_libdir}/%{family}/root/grub/%{_target_cpu}/install
%dir %{_libdir}/%{family}/root/grub/%{_target_cpu}/install/images
%{_libdir}/%{family}/root/grub/%{_target_cpu}/install/images/all.cpio.xz
%dir %{_libdir}/%{family}/root/grub/boot/
%{_libdir}/%{family}/root/grub/boot/firmware.cpio.xz
%{_libdir}/%{family}/root/grub/boot/memtest.bin
%dir %{_libdir}/%{family}/root/grub/boot/alt?
%dir %{_libdir}/%{family}/root/grub/boot/alt?/*
%{_libdir}/%{family}/root/grub/boot/alt?/*/modules.cpio.xz
%{_libdir}/%{family}/root/grub/boot/alt?/*/vmlinuz
%dir %{_libdir}/%{family}/root/grub/boot/grub
%{_libdir}/%{family}/root/grub/boot/grub/grub.cfg
%dir %{_libdir}/%{family}/root/grub/boot/grub/themes
%dir %{_libdir}/%{family}/root/grub/boot/grub/themes/Moondrake
%{_libdir}/%{family}/root/grub/boot/grub/themes/Moondrake/*
#%dir %{_libdir}/%{family}/root/isolinux
#%{_libdir}/%{family}/root/isolinux/*
