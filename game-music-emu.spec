%define major	0
%define libname	%mklibname gme %{major}
%define devname	%mklibname -d gme

Summary:	Game Music Emulators library
Name:		game-music-emu
Version:	0.5.5
Release:	4
License:	LGPLv2+
Group:		Sound
Url:		http://code.google.com/p/game-music-emu/
Source0:	http://game-music-emu.googlecode.com/files/%{name}-%{version}.tbz2
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
%if %{_lib} != lib
mv %{buildroot}%{_prefix}/lib/ %{buildroot}%{_libdir}
%endif

%files -n %{libname}
%_libdir/libgme.so.%{major}*

%files -n %{devname}
%doc readme.txt gme.txt changes.txt design.txt
%_libdir/libgme.so
%_includedir/gme

