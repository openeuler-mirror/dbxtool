%global git_commit_hash 889594ffb104e3384fd91395f4f26b8b68fc38e1

Name: dbxtool
Version: 8
Release: 9
Summary: Tool for managing dbx updates installed on a machine.
License: GPLv2
URL: https://github.com/vathpela/dbxtool-devel
Source0: https://github.com/vathpela/%{name}-devel/archive/%{git_commit_hash}/%{name}-devel-889594f.tar.gz
Patch0: dbxtool-8-ccldflags.patch

BuildRequires: gcc popt-devel efivar-devel >= 35-1 systemd
Requires: efivar systemd

%description
Tool for managing dbx updates installed on a machine.

%package_help

%prep
%autosetup -n %{name}-devel-%{git_commit_hash} -p1

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" CCLDFLAGS="%{__global_ldflags}"

%install
%make_install

%check

%pre

%preun
%systemd_preun dbxtool.service

%post
%systemd_post dbxtool.service

%postun

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%exclude %{_docdir}/%{name}/COPYING
%{_unitdir}/dbxtool.service
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.bin

%files help
%doc %{_mandir}/man1/*

%changelog
* Mon Oct 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 8-9
- Package rebuild.

* Mon Sep 02 2019 openEuler Buildteam <buildteam@openeuler.org> - 8-8
- Package init.
