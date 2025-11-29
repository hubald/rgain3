# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_example_spec_file

%define debug_package %{nil}

%define _name rgain3

%define mybuildnumber %{?build_number}%{?!build_number:1}

Name:           python-%{_name}
Version:        1.3.5
Release:        %{mybuildnumber}%{?dist}
Summary:        ReplayGain manipulator in Python

License:        GPLv2
URL:            https://github.com/Rudd-O/%{_name}
Source:         rgain3-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel, python3-setuptools, python-types-cryptography, openssl
Requires:       gobject-introspection python3-gobject-base gstreamer-plugins-base gstreamer-plugins-good gstreamer-plugins-bad gstreamer-plugins-ugly

%global _description %{expand:
A set of Python modules and utility programmes to deal with
Replay Gain information – calculate it (with GStreamer), read
and write it (with Mutagen). It has support for Ogg Vorbis (or
probably anything stored in an Ogg container), Flac, WavPack,
MP4 (aka AAC) and MP3 (in different incarnations).}

%description %_description

%package -n python3-%{_name}
Summary:        %{summary}

%description -n python3-%{_name} %_description

%prep
%autosetup -p1 -n %{_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{_name}


%check
true
# percent tox disabled


# Note that there is no %%files section for
# the unversioned python module, python-pello.

# For python3-pello, %%{pyproject_files} handles code files and %%license,
# but executables and documentation must be listed in the spec file:

%files -n python3-%{_name} -f %{pyproject_files}
%attr(0755,root,root) %{_bindir}/collectiongain
%attr(0755,root,root) %{_bindir}/replaygain

%doc README.md


%changelog
* Wed Feb 21 2024 Manuel Amador <rudd-o@rudd-o.com> 1.1.1-1
- First RPM packaging release
