[app]
title = MAX
package.name = maxapp
package.domain = com.max.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,dummy.bin

version = 1.0
requirements = python3,kivy

[buildozer]
log_level = 2

android.permissions =

android.api = 35
android.minapi = 21
android.ndk = 26b
android.sdk = 35

android.add_assets = dummy.bin