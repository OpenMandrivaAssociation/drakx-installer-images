%define	theme	Free
%define	server_kernel_version 3.4.0-1.1
%define	main_kernel_version 3.4.0-2.1

%ifarch %ix86
%define kernels kernel-generic = %{main_kernel_version} kernel-server = %{server_kernel_version}
%else
%ifarch ppc
%define kernels kernel-legacy = %{main_kernel_version}
%else
%define kernels kernel-desktop = %{main_kernel_version} kernel-server = %{server_kernel_version}
%endif
%endif

Summary:	DrakX installer images
Name:		drakx-installer-images
Version:	1.53
Release:	3
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.mandriva.com/Tools/DrakX
BuildRequires:	%{kernels} kernel-firmware
%ifarch %ix86 x86_64
BuildRequires:	memtest86+
BuildRequires:	grub
BuildRequires:	syslinux >= 3.72
%endif
%ifarch ppc
BuildRequires:	yaboot
%endif
BuildRequires:	drakx-installer-binaries >= 1.47
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
dest=%{buildroot}%{_libdir}/%{name}
mkdir -p $dest
make -C images install ROOTDEST=$dest

%files
%{_libdir}/%{name}
