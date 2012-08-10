%define name game-music-emu
%define version 0.5.5
%define release %mkrel 4

%define major 0
%define libname %mklibname gme %major
%define develname %mklibname -d gme

Summary: Game Music Emulators library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://game-music-emu.googlecode.com/files/%{name}-%{version}.tbz2
License: LGPLv2+
Group: Sound
Url: http://code.google.com/p/game-music-emu/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake

%description
This is a collection of video game music file emulators that supports a
variety of formats and systems.

%package -n %libname
Group: System/Libraries
Summary: Game Music Emulators library

%description -n %libname
This is a collection of video game music file emulators that supports a
variety of formats and systems.

%package -n %develname
Group: Development/C++
Summary: Game Music Emulators development library
Requires: %libname = %version-%release
Provides: libgme-devel = %version-%release

%description -n %develname
This is a collection of video game music file emulators that supports a
variety of formats and systems.


%prep
%setup -q

%build
%cmake
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/ %buildroot%_libdir
%endif

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%doc readme.txt gme.txt
%_libdir/libgme.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc changes.txt design.txt
%_libdir/libgme.so
%_includedir/gme
