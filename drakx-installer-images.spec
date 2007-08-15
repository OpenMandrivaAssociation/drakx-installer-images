%define name drakx-installer-images
%define version 1.15
%define release %mkrel 1
%define theme Free
%define main_kernel_version 2.6.22.5mdv

%ifarch %ix86 ppc
%define kernels kernel-legacy-%main_kernel_version
%else
%define kernels kernel-%main_kernel_version
%endif

%define mandriva_version %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' mandriva-release)

Summary: DrakX installer images
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: %kernels
%ifarch %ix86 x86_64
BuildRequires: memtest86+
BuildRequires: grub
BuildRequires: syslinux >= 3.51-4mdv2008.0
%endif
%ifarch ppc
BuildRequires: yaboot
%endif
BuildRequires: drakx-installer-binaries >= 1.11
BuildRequires: mandriva-theme-%{theme}
BuildRequires: pcmciautils
BuildRequires: perl-XML-Parser

BuildRequires: cdrkit-genisoimage
BuildRequires: mkdosfs-with-dir
BuildRequires: mknod-m600
BuildRequires: mtools

#- require the version used during build
Requires: mandriva-release = %mandriva_version

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


