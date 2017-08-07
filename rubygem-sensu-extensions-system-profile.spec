# Generated from sensu-extensions-system-profile-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-extensions-system-profile

Name:           rubygem-%{gem_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Check extension to collect Linux system metrics
Group:          Development/Languages
License:        MIT
URL:            https://github.com/sensu-extensions/sensu-extensions-debug
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        https://github.com/sensu-extensions/%{gem_name}/archive/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(sensu-extension)
BuildRequires:  rubygem(sensu-logger)
BuildRequires:  rubygem(sensu-settings)
BuildRequires:  rubygem(eventmachine)

Requires:       rubygem(sensu-extension)

BuildArch: noarch
%if 0%{?rhel}
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Check extension to collect Linux system metrics.


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%if 0%{?dlrn} > 0
%setup -q -D -T -n  %{dlrn_nvr}
%else
%setup -q -D -T -n  %{gem_name}-%{version}
%endif

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

install -d -p %{_builddir}%{gem_instdir}
%if 0%{?dlrn} > 0
tar -xvzf %{SOURCE1} -C %{_builddir}/%{dlrn_nvr}/%{gem_instdir} --strip-components=1 %{gem_name}-%{version}/spec
%else
tar -xvzf %{SOURCE1} -C %{_builddir}/%{gem_name}-%{version}/%{gem_instdir} --strip-components=1 %{gem_name}-%{version}/spec
%endif

# Run the test suite
%check
pushd .%{gem_instdir}
rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Fri Dec 23 2016 Martin Mágr <mmagr@redhat.com> - 1.0.0-1
- Initial package
