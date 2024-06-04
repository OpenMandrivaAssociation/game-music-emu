%define major	0
%define libname	%mklibname gme
%define oldlibname	%mklibname gme 0
%define devname	%mklibname -d gme

Summary:	Game Music Emulators library
Name:		game-music-emu
Version:	0.6.3
Release:	1
License:	LGPLv2+
Group:		Sound
Url:		https://code.google.com/p/game-music-emu/
Source0:  https://github.com/libgme/game-music-emu/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
#Source0:	https://bitbucket.org/mpyne/game-music-emu/downloads/%{name}-%{version}.tar.xz
BuildRequires:	cmake

%description
This is a collection of video game music file emulators that supports a
variety of formats and systems.

%package -n %{libname}
Group:		System/Libraries
Summary:	Game Music Emulators library
%rename %{oldlibname}

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
%make

%install
cd build
%makeinstall_std

%files -n %{libname}
%_libdir/libgme.so.%{major}*

%files -n %{devname}
%doc readme.txt gme.txt changes.txt design.txt
%_libdir/libgme.so
%_includedir/gme
%{_libdir}/pkgconfig/libgme.pc

