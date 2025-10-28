[app]
title = MAX
package.name = max
package.domain = com.max.app

source.dir = .
source.include_exts = py,dummy.bin

version = 1.0
requirements = python3,kivy==2.3.0

[buildozer]
log_level = 2

android.api = 35
android.minapi = 21
android.ndk = 26b
android.sdk = 35

android.add_assets = dummy.bin
