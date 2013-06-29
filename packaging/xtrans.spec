Name:           xtrans
Version:        1.2.7
Release:        0
License:        MIT
Summary:        Library to handle network protocol transport in X
Url:            http://xorg.freedesktop.org/
Group:          Development/Libraries/X11
Source:         %{name}-%{version}.tar.bz2
Source1001: 	xtrans.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildArch:      noarch

%description
xtrans is a library of code that is shared among various X packages to
handle network protocol transport in a modular fashion, allowing a
single place to add new transport types. It is used by the X server,
libX11, libICE, the X font server, and related components.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --docdir=%{_docdir}/xtrans
make %{?_smp_mflags}

%install
%make_install

%pre
test -L usr/include/X11 && rm usr/include/X11
exit 0

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%doc %{_docdir}/xtrans/xtrans.xml
%{_includedir}/X11/Xtrans/
%{_datadir}/aclocal/xtrans.m4
%{_datadir}/pkgconfig/xtrans.pc

%changelog
