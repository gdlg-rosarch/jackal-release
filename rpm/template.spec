Name:           ros-indigo-jackal-navigation
Version:        0.5.4
Release:        0%{?dist}
Summary:        ROS jackal_navigation package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-amcl
Requires:       ros-indigo-gmapping
Requires:       ros-indigo-map-server
Requires:       ros-indigo-move-base
Requires:       ros-indigo-urdf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
Launch files and code for autonomous navigation of the Jackal

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Apr 12 2018 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.5.4-0
- Autogenerated by Bloom

* Wed Jun 01 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.5.3-0
- Autogenerated by Bloom

* Thu Mar 24 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.5.2-1
- Autogenerated by Bloom

* Mon Feb 02 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.5.1-0
- Autogenerated by Bloom

* Tue Jan 20 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.5.0-0
- Autogenerated by Bloom

* Wed Jan 14 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.4.2-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.4.1-0
- Autogenerated by Bloom

