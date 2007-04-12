%define name drakx-installer-images
%define version 1.9
%define release %mkrel 1

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
%ifarch %ix86 ppc
BuildRequires: kernel-legacy-2.6.17.13mdv
%endif
%ifarch %ix86 x86_64
BuildRequires: memtest86+
BuildRequires: grub
BuildRequires: syslinux
%endif
%ifarch ppc
BuildRequires: yaboot
%endif
BuildRequires: drakx-installer-binaries >= 1.7
BuildRequires: mandriva-theme
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
make -C images

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


