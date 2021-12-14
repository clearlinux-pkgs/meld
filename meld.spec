#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : meld
Version  : 3.20.4
Release  : 49
URL      : https://download.gnome.org/sources/meld/3.20/meld-3.20.4.tar.xz
Source0  : https://download.gnome.org/sources/meld/3.20/meld-3.20.4.tar.xz
Summary  : Visual diff and merge tool
Group    : Development/Tools
License  : BSD-2-Clause CC-BY-SA-3.0 GPL-2.0 GPL-2.0+
Requires: meld-bin = %{version}-%{release}
Requires: meld-data = %{version}-%{release}
Requires: meld-license = %{version}-%{release}
Requires: meld-locales = %{version}-%{release}
Requires: meld-man = %{version}-%{release}
Requires: meld-python = %{version}-%{release}
Requires: meld-python3 = %{version}-%{release}
Requires: compat-gtksourceview-soname3
Requires: pygobject
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : compat-gtksourceview-soname3
BuildRequires : glib
BuildRequires : gtk3
BuildRequires : intltool
BuildRequires : libxml2
BuildRequires : pygobject

%description
Meld is the visual diff and merge tool of GNOME, targeted at developers. It
allows users to compare two or three files or directories visually,
color-coding the different lines.

%package bin
Summary: bin components for the meld package.
Group: Binaries
Requires: meld-data = %{version}-%{release}
Requires: meld-license = %{version}-%{release}

%description bin
bin components for the meld package.


%package data
Summary: data components for the meld package.
Group: Data

%description data
data components for the meld package.


%package doc
Summary: doc components for the meld package.
Group: Documentation
Requires: meld-man = %{version}-%{release}

%description doc
doc components for the meld package.


%package license
Summary: license components for the meld package.
Group: Default

%description license
license components for the meld package.


%package locales
Summary: locales components for the meld package.
Group: Default

%description locales
locales components for the meld package.


%package man
Summary: man components for the meld package.
Group: Default

%description man
man components for the meld package.


%package python
Summary: python components for the meld package.
Group: Default
Requires: meld-python3 = %{version}-%{release}

%description python
python components for the meld package.


%package python3
Summary: python3 components for the meld package.
Group: Default
Requires: python3-core

%description python3
python3 components for the meld package.


%prep
%setup -q -n meld-3.20.4
cd %{_builddir}/meld-3.20.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635752814
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/meld
cp %{_builddir}/meld-3.20.4/COPYING %{buildroot}/usr/share/package-licenses/meld/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/meld-3.20.4/data/icons/COPYING %{buildroot}/usr/share/package-licenses/meld/3e0c4049892ab31e3aaf45c71f830176bc566c14
cp %{_builddir}/meld-3.20.4/data/icons/COPYING_CCBYSA3 %{buildroot}/usr/share/package-licenses/meld/80059f30d312011eaf041ce648eeca6473a08746
cp %{_builddir}/meld-3.20.4/meld/vc/COPYING %{buildroot}/usr/share/package-licenses/meld/14c4e1f2e383319099e47e974f26fba40e0c975d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
%find_lang meld
## Remove excluded files
rm -f %{buildroot}*/usr/share/glib-2.0/schemas/gschemas.compiled
rm -f %{buildroot}*/usr/share/icons/hicolor/icon-theme.cache

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/meld

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.meld.desktop
/usr/share/glib-2.0/schemas/org.gnome.meld.gschema.xml
/usr/share/icons/HighContrast/scalable/apps/org.gnome.meld.svg
/usr/share/icons/hicolor/16x16/actions/meld-change-apply-left.png
/usr/share/icons/hicolor/16x16/actions/meld-change-apply-right.png
/usr/share/icons/hicolor/16x16/actions/meld-change-copy.png
/usr/share/icons/hicolor/16x16/actions/meld-change-delete.png
/usr/share/icons/hicolor/16x16/apps/meld-version-control.png
/usr/share/icons/hicolor/16x16/apps/org.gnome.meld.png
/usr/share/icons/hicolor/22x22/apps/org.gnome.meld.png
/usr/share/icons/hicolor/32x32/apps/org.gnome.meld.png
/usr/share/icons/hicolor/48x48/apps/meld-version-control.png
/usr/share/icons/hicolor/48x48/apps/org.gnome.meld.png
/usr/share/icons/hicolor/scalable/apps/org.gnome.meld.svg
/usr/share/meld/icons/COPYING
/usr/share/meld/icons/COPYING_CCBYSA3
/usr/share/meld/icons/emblem-meld-newer-file.png
/usr/share/meld/icons/filter-ignored-24.png
/usr/share/meld/icons/filter-modified-24.png
/usr/share/meld/icons/filter-nonvc-24.png
/usr/share/meld/icons/filter-normal-24.png
/usr/share/meld/icons/vc-add-24.png
/usr/share/meld/icons/vc-checkout-24.png
/usr/share/meld/icons/vc-commit-24.png
/usr/share/meld/icons/vc-push-24.png
/usr/share/meld/icons/vc-remove-24.png
/usr/share/meld/icons/vc-resolve-24.png
/usr/share/meld/icons/vc-update-24.png
/usr/share/meld/meld.css
/usr/share/meld/styles/meld-base.style-scheme.xml
/usr/share/meld/styles/meld-base.xml
/usr/share/meld/styles/meld-dark.style-scheme.xml
/usr/share/meld/styles/meld-dark.xml
/usr/share/meld/ui/EditableList.ui
/usr/share/meld/ui/application.ui
/usr/share/meld/ui/appmenu-fallback.xml
/usr/share/meld/ui/dirdiff-ui.xml
/usr/share/meld/ui/dirdiff.ui
/usr/share/meld/ui/encoding-selector.ui
/usr/share/meld/ui/filediff-ui.xml
/usr/share/meld/ui/filediff.ui
/usr/share/meld/ui/findbar.ui
/usr/share/meld/ui/language-selector.ui
/usr/share/meld/ui/meldapp-ui.xml
/usr/share/meld/ui/meldapp.ui
/usr/share/meld/ui/patch-dialog.ui
/usr/share/meld/ui/preferences.ui
/usr/share/meld/ui/shortcuts.ui
/usr/share/meld/ui/tab-placeholder.ui
/usr/share/meld/ui/vcview-ui.xml
/usr/share/meld/ui/vcview.ui
/usr/share/metainfo/org.gnome.meld.appdata.xml
/usr/share/mime-packages/org.gnome.meld.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/meld-3.20.4/COPYING
/usr/share/doc/meld-3.20.4/NEWS
/usr/share/help/C/meld/command-line.page
/usr/share/help/C/meld/file-changes.page
/usr/share/help/C/meld/file-filters.page
/usr/share/help/C/meld/file-mode.page
/usr/share/help/C/meld/flattened-view.page
/usr/share/help/C/meld/folder-mode.page
/usr/share/help/C/meld/index.page
/usr/share/help/C/meld/introduction.page
/usr/share/help/C/meld/keyboard-shortcuts.page
/usr/share/help/C/meld/legal.xml
/usr/share/help/C/meld/missing-functionality.page
/usr/share/help/C/meld/preferences.page
/usr/share/help/C/meld/resolving-conflicts.page
/usr/share/help/C/meld/text-filters.page
/usr/share/help/C/meld/vc-mode.page
/usr/share/help/C/meld/vc-supported.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/meld/14c4e1f2e383319099e47e974f26fba40e0c975d
/usr/share/package-licenses/meld/3e0c4049892ab31e3aaf45c71f830176bc566c14
/usr/share/package-licenses/meld/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/meld/80059f30d312011eaf041ce648eeca6473a08746

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/meld.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f meld.lang
%defattr(-,root,root,-)

