%define major	0
%define libname	%mklibname gme %{major}
%define devname	%mklibname -d gme

Summary:	Game Music Emulators library
Name:		game-music-emu
Version:	0.6.4
Release:	1
License:	LGPLv2+
Group:		Sound
Url:		https://github.com/libgme/game-music-emu/
Source0:	https://github.com/libgme/game-music-emu/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake

%description
This is a collection of video game music file emulators that supports a
variety of formats and systems.

%package -n %{libname}
Group:		System/Libraries
Summary:	Game Music Emulators library

%description -n %{libname}
This is a collection of video game music file emulators that supports a
variety of formats and systems.

%package -n %{devname}
Group:		Development/C++
Summary:	Game Music Emulators development library
Requires:	%{libname} = %{version}-%{release}
Provides:	libgme-devel = %{version}-%{release}

%description -n %{devname}
This is a collection of video game music file emulators that supports a
variety of formats and systems.

%prep
%setup -q

%build
%cmake
%make_build

%install
cd build
%make_install

%files -n %{libname}
%_libdir/libgme.so.%{major}*

%files -n %{devname}
%doc readme.txt gme.txt changes.txt design.txt
%_libdir/libgme.so
%_includedir/gme
%{_libdir}/pkgconfig/libgme.pc

