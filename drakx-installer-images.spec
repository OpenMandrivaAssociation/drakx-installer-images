%define theme Free
%define main_kernel_version 3.1.4-1.1

%ifarch %ix86
%define kernels kernel-generic-%main_kernel_version kernel-server-%main_kernel_version
%else
%ifarch ppc
%define kernels kernel-legacy-%main_kernel_version
%else
%define kernels kernel-desktop-%main_kernel_version kernel-server-%main_kernel_version
%endif
%endif

Summary: DrakX installer images
Name: drakx-installer-images
Version: 1.53
Release: 2
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: %kernels kernel-firmware
%ifarch %ix86 x86_64
BuildRequires: memtest86+
BuildRequires: grub
BuildRequires: syslinux >= 3.72
%endif
%ifarch ppc
BuildRequires: yaboot
%endif
BuildRequires: drakx-installer-binaries >= 1.47
BuildRequires: ldetect-lst >= 0.1.291-2
BuildRequires: mandriva-theme-%{theme}
BuildRequires: pcmciautils
BuildRequires: perl-XML-Parser

BuildRequires: cdrkit-genisoimage
BuildRequires: mknod-m600
BuildRequires: mtools dosfstools
Buildrequires: busybox-static
Buildrequires: ka-deploy-source-node

%description
images needed to build Mandriva installer (DrakX)

%prep
%setup -q

%build
THEME=Mandriva-%{theme} make -C images KERNELS="%{kernels}"

%install
rm -rf %{buildroot}

dest=%{buildroot}%{_libdir}/%name
mkdir -p $dest
make -C images install ROOTDEST=$dest

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/%name


