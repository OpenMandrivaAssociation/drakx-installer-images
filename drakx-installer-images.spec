%define name drakx-installer-images
%define version 1.41
%define release %mkrel 1
%define theme Free
%define main_kernel_version 2.6.29.1-2mnb

%ifarch %ix86
%define kernels kernel-desktop586-%main_kernel_version kernel-server-%main_kernel_version
%else
%ifarch ppc
%define kernels kernel-legacy-%main_kernel_version
%else
%define kernels kernel-desktop-%main_kernel_version kernel-server-%main_kernel_version
%endif
%endif

Summary: DrakX installer images
Name: %{name}
Version: %{version}
Release: %{release}
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
BuildRequires: drakx-installer-binaries >= 1.36
BuildRequires: ldetect-lst >= 0.1.199
BuildRequires: mandriva-theme-%{theme}
BuildRequires: pcmciautils
BuildRequires: perl-XML-Parser

BuildRequires: cdrkit-genisoimage
BuildRequires: mkdosfs-with-dir
BuildRequires: mknod-m600
BuildRequires: mtools
Buildrequires: busybox
Buildrequires: ka-deploy-source-node

%description
images needed to build Mandriva installer (DrakX)

%prep
%setup -q

%build
THEME=Mandriva-%{theme} make -C images KERNELS="%{kernels}"

%install
rm -rf $RPM_BUILD_ROOT

dest=$RPM_BUILD_ROOT%{_libdir}/%name
mkdir -p $dest
make -C images install ROOTDEST=$dest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/%name


