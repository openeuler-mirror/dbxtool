Name: dbxtool
Version: 8
Release: 8
Summary: Tool for managing dbx updates installed on a machine.
License: GPLv2
URL: https://github.com/vathpela/dbxtool
#The file dbxtool-8.tar.bz2 is from fedora:https://kojipkgs.fedoraproject.org//packages/dbxtool/8/7.fc29/src/dbxtool-8-7.fc29.src.rpm.
Source0: https://github.com/vathpela/dbxtool/releases/download/dbxtool-%{version}/dbxtool-%{version}.tar.bz2
#Patch0,Patch1 and Patch2 are from fedora:https://kojipkgs.fedoraproject.org//packages/dbxtool/8/7.fc29/src/dbxtool-8-7.fc29.src.rpm.
Patch0: dbxtool-8-ccldflags.patch
Patch1: 0001-don-t-use-f-in-dbxtool.service.patch
Patch2: 0002-Make-quiet-exit-on-missing-PK-KEK-not-return-error-s.patch

BuildRequires: gcc popt-devel efivar-devel >= 31-3 systemd
Requires: efivar systemd

%description
Tool for managing dbx updates installed on a machine.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" CCLDFLAGS="%{__global_ldflags}"

%install
%make_install

%preun
%systemd_preun dbxtool.service

%post
%systemd_post dbxtool.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%exclude %{_docdir}/%{name}/COPYING
%{_unitdir}/dbxtool.service
%{_bindir}/dbxtool
%dir %{_datadir}/dbxtool/
%{_datadir}/dbxtool/*.bin

%files help
%doc %{_mandir}/man1/*

%changelog
* Mon Sep 2 2019 openEuler Buildteam <buildteam@openeuler.org> - 8-8
- Package init
