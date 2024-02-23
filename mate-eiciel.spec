Summary:	ACL viewer and editor for MATE
Name:		mate-eiciel
Version:	1.20.1
Release:	1
License:	GPL-2.0-or-later
Group:		Graphical desktop/Other
URL:		https://github.com/darkshram/mate-eiciel
Source:	 https://github.com/darkshram/mate-eiciel/releases/download/%{version}/%{name}-%{version}.tar.xz
# (opensuse)
Patch0:	 mate-eiciel-gtk-3.20.patch
Patch1:	 support-C++17.patch

BuildRequires:	mate-common
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(libacl)
BuildRequires:	pkgconfig(libattr)
BuildRequires:	pkgconfig(libcaja-extension)

%description
MATE eiciel is a Graphical editor for access control lists (ACLs)
and extended attributes (xattr), either as an extension within
Caja, or as a standalone utility.

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.{png,svg}
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*%{name}.appdata.xml
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------

%package -n caja-extension-eiciel
Summary:	Caja extension for the ACL viewer and editor
Group:		System/GUI/Other
Requires:	%{name} = %{version}

%description -n caja-extension-eiciel
A Caja extension that allows viewing and editing ACL permissions.

%files -n caja-extension-eiciel
%{_libdir}/caja/extensions-2.0/libeiciel-caja.so

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
#NOCONFIGURE=1 mate-autogen
%configure
%make_build

%install
%make_install

# remove static stuff
find %{buildroot} -type f -name "*.la" -delete -print

# locales
%find_lang %{name} --with-gnome --all-name

