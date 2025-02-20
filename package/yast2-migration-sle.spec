#
# spec file for package yast2-migration-sle
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           yast2-migration-sle
Version:        4.5.1
Release:        0
Summary:        YaST2 - Online migration
Group:          System/YaST
License:        GPL-2.0-only
URL:            https://github.com/yast/yast-migration-sle

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-buildtools
BuildRequires:  yast2-ruby-bindings
BuildRequires:  yast2-migration
BuildRequires:  yast2-registration
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

Requires:       yast2
Requires:       yast2-migration
Requires:       yast2-registration
Requires:       yast2-ruby-bindings

Supplements:    yast2-registration

BuildArch:      noarch

%description
This package contains the YaST2 component for migrating an openSUSE Leap
system to the SUSE Linux Enterprise (SLE) system.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%files
%{yast_clientdir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%license COPYING
%doc %{yast_docdir}

%changelog
