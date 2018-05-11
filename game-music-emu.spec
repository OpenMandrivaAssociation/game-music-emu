%define major	0
%define libname	%mklibname gme %{major}
%define devname	%mklibname -d gme

Summary:	Game Music Emulators library
Name:		game-music-emu
Version:	0.6.2
Release:	1
License:	LGPLv2+
Group:		Sound
Url:		http://code.google.com/p/game-music-emu/
Source0:	https://bitbucket.org/mpyne/game-music-emu/downloads/%{name}-%{version}.tar.xz
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

