[app]

# (str) Title of your application
title = 商品期货复盘

# (str) Package name
package.name = futuresreview

# (str) Package domain (needed for android/ios packaging)
package.domain = org.futures

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
source.exclude_patterns =

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
# garden_requirements =

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) List of service to declare
# services =

#
# OSX Specific
#
# (str) Path to a custom kivy_ios directory
# ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
# ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
# ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
# ios.ios_deploy_branch = 1.10.0

# (int) Number of seconds to wait for ios-deploy to initialize
# ios.ios_deploy_timeout = 5

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray, darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy, olive, purple, silver, teal.
# android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/ for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
# android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
# adaptive_icon.filename = %(source.dir)s/data/icon.png

# (str) Adaptive icon background color (for android toolchain)
# adaptive_icon.background_color = #FFFFFF

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
android.permissions = INTERNET

# (list) features (adds uses-feature -tags to manifest)
# android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
# android.api = 31

# (int) Minimum API your APK / AAB will support.
# android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 24

# (str) Android NDK version to use
# android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
# android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_dir =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_dir =

# (str) ANT directory (if empty, it will be automatically downloaded.)
# android.ant_dir =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
# If set to False, the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
# android.activity_class_name =

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to add permissions or other tags not covered by the previous parameters
# android.extra_manifest_xml =

# (str) Extra xml to write directly inside the <application> element of AndroidManifest.xml
# use that parameter to add custom entries like service, receiver, etc.
# android.extra_application_xml =

# (str) Procfile for pyjnius networking
# android.procfile =

# (str) URL to the hook for p4a
# android.p4a_hook = 

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = @android:style/Theme.Holo.Light

# (list) Pattern to whitelist for the whole project
# android.whitelist = 

# (str) Path to a custom whitelist file
# android.whitelist_src = 

# (str) Path to a custom blacklist file
# android.blacklist_src = 

# (list) List of Java .jar files to add to the libs so that pyjnius can access it
# android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a directory containing the files)
# android.add_src = 

# (list) Android AAR archives to add
# android.add_aars = 

# (list) Put these files or directories in the apk assets directory. 
# Either form may be used, and assets need not be in 'assets' folder in app source
# android.add_assets = src/main/assets/,src/main/assets/asset.png

# (list) Put these files or directories in the apk res directory. 
# The option may be used in addition to android.add_assets or android.add_jars
# android.add_res = 

# (str) Path to a custom build.xml file
# android.custom_build_xml =

# (str) Path to a custom gradle.properties file
# android.custom_gradle_properties =

# (list) List of application modules to load at startup
# android.startup_modules = 

# (bool) If True, the application will be restarted instead of paused when the user switches apps
# android.restart_on_resume = False

# (str) Custom application name used in the status bar
# android.statusbar_background = 

# (str) Custom application name used in the title bar
# android.titlebar_background = 

# (list) Ordered list of fonts to use, use the >> token to separate the names of fonts
# If the first font fails to load, the next one will be used. Only the first font that loads will be used.
# android.fonts = >>font1.ttf>>font2.ttf

#
# Python for android (p4a) specific
#

# (str) python-for-android directory (if empty, it will be automatically downloaded.)
# p4a.source_dir = ../python-for-android

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) Filename to the hook for p4a
# p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
# p4a.port = 

# (str) p4a theme, default is ok for Kivy-based app
# p4a.theme = @android:style/Theme.Holo.Light

# (str) android.apptheme to use in build-system, default is None
# p4a.apptheme = 

# (bool) Create a debug apk
# p4a.debug = False

# (str) The extra args to pass to build.py
# p4a.extra_args = --debug

#
# iOS specific
#

# (str) Path to a custom kivy-ios directory
# ios.kivy_ios_dir = ../kivy-ios

# (str) Name of the certificate to use for signing the debug version
# Get a list of available certificates: buildozer ios list_identities
# ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
# ios.codesign.release = %(ios.codesign.debug)s

#
# Distribute section
#

# (str) Upload your application to the Play Store
# deploy.google_play_store = True

# (str) The API key to use for the Play Store
# deploy.google_play_store_key = <your-api-key>

# (str) The APK path to upload
# deploy.google_play_store_apk = bin/myapp-release.apk

# (str) The aab path to upload
# deploy.google_play_store_aab = bin/myapp-release.aab

# (str) The Android App Bundle name
# package.aab.name = My Application


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = .buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa)
# bin_dir = ./bin

# (list) The list of available actions
# actions = android, ios, osx, windows, linux

# (int) amount of parallel workers to use for the build, for --debug 
# builds 1 will be used by default (can be overridden by --buildworkers option)
# buildworkers = 4

# (str) The build target architecture, in case of Android: armeabi-v7a, arm64-v8a, x86, x86_64
# android.arch = armeabi-v7a

# (str) The output directory used for build artifacts
# android.build_dir = ./build

# (str) The directory in which android projects are stored
# android.project_dir = ./project

# (str) The directory in which android builds are stored
# android.sdk_dir = ./sdk

# (str) The directory in which the buildozer.py script is located
# buildozer_dir = .

# (str) The directory in which the build.py script is located
# build_script_dir = .

# (str) The directory in which the buildozer.spec file is located
# spec_dir = .

# (str) The directory in which the build artifacts are stored
# dist_dir = ./dist

# (str) The directory in which the build artifacts are stored for android
# android.dist_dir = ./dist/android

# (str) The directory in which the build artifacts are stored for ios
# ios.dist_dir = ./dist/ios

# (str) The directory in which the build artifacts are stored for osx
# osx.dist_dir = ./dist/osx

# (str) The directory in which the build artifacts are stored for windows
# windows.dist_dir = ./dist/windows

# (str) The directory in which the build artifacts are stored for linux
# linux.dist_dir = ./dist/linux

# (bool) Automatically remove the build directory
# auto_clean = False

# (bool) Automatically remove the distribution directory
# auto_clean_dist = False

# (bool) Allow to run the same build again, skipping the clean step
# no_clean = False

# (bool) Skip trying to update the build tools
# no_update = False

# (bool) Use the date as the version number
# use_date_version = False

# (bool) Use the git commit hash as the version number
# use_git_version = False

# (str) The git branch to use for versioning
# git_branch = master

# (bool) Use the git tag as the version number
# use_git_tag = False

# (str) The git remote to use for versioning
# git_remote = origin

# (bool) Always use the latest version of the build tools
# always_use_latest_version = False

# (bool) Always use the latest version of the dependencies
# always_use_latest_deps = False

# (bool) [EXPERIMENTAL] Use ccache instead of distcc for compilation
# use_ccache = False

# (bool) [EXPERIMENTAL] Use distcc for compilation
# use_distcc = False

# (str) The command to use for distcc
# distcc_cmd = distcc

# (bool) [EXPERIMENTAL] Use parallel compilation
# use_parallel_compile = True

# (bool) [EXPERIMENTAL] Use parallel link
# use_parallel_link = True

# (bool) [EXPERIMENTAL] Use lto for compilation
# use_lto = False

# (bool) [EXPERIMENTAL] Use gold linker
# use_gold_linker = False

# (bool) [EXPERIMENTAL] Use incremental compilation
# use_incremental_compile = False

# (bool) [EXPERIMENTAL] Use incremental link
# use_incremental_link = False

# (bool) [EXPERIMENTAL] Use ccache for incremental compilation
# use_ccache_incremental = False

# (bool) [EXPERIMENTAL] Use distcc for incremental compilation
# use_distcc_incremental = False

# (bool) [EXPERIMENTAL] Use parallel compilation for incremental builds
# use_parallel_compile_incremental = True

# (bool) [EXPERIMENTAL] Use parallel link for incremental builds
# use_parallel_link_incremental = True

# (bool) [EXPERIMENTAL] Use lto for incremental compilation
# use_lto_incremental = False

# (bool) [EXPERIMENTAL] Use gold linker for incremental builds
# use_gold_linker_incremental = False

# (str) The path to the ccache executable
# ccache_path = /usr/bin/ccache

# (str) The path to the distcc executable
# distcc_path = /usr/bin/distcc

# (str) The path to the ccache directory
# ccache_dir = ~/.ccache

# (int) The maximum size of the ccache directory in MB
# ccache_size = 50

# (bool) [EXPERIMENTAL] Use ccache for the android ndk build
# android.use_ccache = False

# (bool) [EXPERIMENTAL] Use distcc for the android ndk build
# android.use_distcc = False

# (bool) [EXPERIMENTAL] Use parallel compilation for the android ndk build
# android.use_parallel_compile = True

# (bool) [EXPERIMENTAL] Use incremental compilation for the android ndk build
# android.use_incremental_compile = False

# (bool) [EXPERIMENTAL] Use incremental link for the android ndk build
# android.use_incremental_link = False

# (bool) [EXPERIMENTAL] Use ccache for incremental android ndk builds
# android.use_ccache_incremental = False

# (bool) [EXPERIMENTAL] Use distcc for incremental android ndk builds
# android.use_distcc_incremental = False

# (bool) [EXPERIMENTAL] Use parallel compilation for incremental android ndk builds
# android.use_parallel_compile_incremental = True

# (bool) [EXPERIMENTAL] Use parallel link for incremental android ndk builds
# android.use_parallel_link_incremental = True

# (int) The number of parallel workers to use for the android ndk build
# android.ndk_workers = 4

# (bool) Use the android ndk r17c
# android.ndk_api_17 = False

# (str) The android ndk version to use
# android.ndk_version = 23b

# (str) The android sdk version to use
# android.sdk_version = 24

# (str) The android api level to use
# android.api_level = 31

# (str) The android min api level to use
# android.minapi_level = 21

# (str) The android target api level to use
# android.targetapi_level = 31

# (bool) Use the android sdk tools
# android.sdk_tools = True

# (str) The android build tools version to use
# android.build_tools_version = 31.0.0

# (bool) Use the android platform tools
# android.platform_tools = True

# (str) The android platform tools version to use
# android.platform_tools_version = 31.0.0

# (bool) Use the android support repository
# android.support_repository = True

# (str) The android support repository version to use
# android.support_repository_version = 47.0.0

# (bool) Use the android google repository
# android.google_repository = True

# (str) The android google repository version to use
# android.google_repository_version = 47.0.0

# (bool) Use the android constraint layout repository
# android.constraint_layout_repository = True

# (str) The android constraint layout repository version to use
# android.constraint_layout_repository_version = 2.1.0

# (bool) Use the android material components repository
# android.material_components_repository = True

# (str) The android material components repository version to use
# android.material_components_repository_version = 1.4.0

# (bool) Use the android androidx repository
# android.androidx_repository = True

# (str) The android androidx repository version to use
# android.androidx_repository_version = 1.0.0

# (bool) Use the android google play services repository
# android.google_play_services_repository = True

# (str) The android google play services repository version to use
# android.google_play_services_repository_version = 47.0.0

# (bool) Use the android google play services maps repository
# android.google_play_services_maps_repository = True

# (str) The android google play services maps repository version to use
# android.google_play_services_maps_repository_version = 47.0.0

# (bool) Use the android google play services location repository
# android.google_play_services_location_repository = True

# (str) The android google play services location repository version to use
# android.google_play_services_location_repository_version = 47.0.0

# (bool) Use the android google play services auth repository
# android.google_play_services_auth_repository = True

# (str) The android google play services auth repository version to use
# android.google_play_services_auth_repository_version = 47.0.0

# (bool) Use the android google play services base repository
# android.google_play_services_base_repository = True

# (str) The android google play services base repository version to use
# android.google_play_services_base_repository_version = 47.0.0

# (bool) Use the android google play services analytics repository
# android.google_play_services_analytics_repository = True

# (str) The android google play services analytics repository version to use
# android.google_play_services_analytics_repository_version = 47.0.0

# (bool) Use the android google play services ads repository
# android.google_play_services_ads_repository = True

# (str) The android google play services ads repository version to use
# android.google_play_services_ads_repository_version = 47.0.0

# (bool) Use the android google play services ads lite repository
# android.google_play_services_ads_lite_repository = True

# (str) The android google play services ads lite repository version to use
# android.google_play_services_ads_lite_repository_version = 47.0.0

# (bool) Use the android google play services ads identifier repository
# android.google_play_services_ads_identifier_repository = True

# (str) The android google play services ads identifier repository version to use
# android.google_play_services_ads_identifier_repository_version = 47.0.0

# (bool) Use the android google play services ads base repository
# android.google_play_services_ads_base_repository = True

# (str) The android google play services ads base repository version to use
# android.google_play_services_ads_base_repository_version = 47.0.0

# (bool) Use the android google play services ads consent repository
# android.google_play_services_ads_consent_repository = True

# (str) The android google play services ads consent repository version to use
# android.google_play_services_ads_consent_repository_version = 47.0.0

# (bool) Use the android google play services ads native repository
# android.google_play_services_ads_native_repository = True

# (str) The android google play services ads native repository version to use
# android.google_play_services_ads_native_repository_version = 47.0.0

# (bool) Use the android google play services ads unified repository
# android.google_play_services_ads_unified_repository = True

# (str) The android google play services ads unified repository version to use
# android.google_play_services_ads_unified_repository_version = 47.0.0

# (bool) Use the android google play services auth api phone repository
# android.google_play_services_auth_api_phone_repository = True

# (str) The android google play services auth api phone repository version to use
# android.google_play_services_auth_api_phone_repository_version = 47.0.0

# (bool) Use the android google play services auth base repository
# android.google_play_services_auth_base_repository = True

# (str) The android google play services auth base repository version to use
# android.google_play_services_auth_base_repository_version = 47.0.0

# (bool) Use the android google play services auth cas repository
# android.google_play_services_auth_cas_repository = True

# (str) The android google play services auth cas repository version to use
# android.google_play_services_auth_cas_repository_version = 47.0.0

# (bool) Use the android google play services auth drive repository
# android.google_play_services_auth_drive_repository = True

# (str) The android google play services auth drive repository version to use
# android.google_play_services_auth_drive_repository_version = 47.0.0

# (bool) Use the android google play services auth identity repository
# android.google_play_services_auth_identity_repository = True

# (str) The android google play services auth identity repository version to use
# android.google_play_services_auth_identity_repository_version = 47.0.0

# (bool) Use the android google play services auth instantapps repository
# android.google_play_services_auth_instantapps_repository = True

# (str) The android google play services auth instantapps repository version to use
# android.google_play_services_auth_instantapps_repository_version = 47.0.0

# (bool) Use the android google play services auth internal repository
# android.google_play_services_auth_internal_repository = True

# (str) The android google play services auth internal repository version to use
# android.google_play_services_auth_internal_repository_version = 47.0.0

# (bool) Use the android google play services auth profile repository
# android.google_play_services_auth_profile_repository = True

# (str) The android google play services auth profile repository version to use
# android.google_play_services_auth_profile_repository_version = 47.0.0

# (bool) Use the android google play services auth proxy repository
# android.google_play_services_auth_proxy_repository = True

# (str) The android google play services auth proxy repository version to use
# android.google_play_services_auth_proxy_repository_version = 47.0.0

# (bool) Use the android google play services auth vision repository
# android.google_play_services_auth_vision_repository = True

# (str) The android google play services auth vision repository version to use
# android.google_play_services_auth_vision_repository_version = 47.0.0

# (bool) Use the android google play services base license repository
# android.google_play_services_base_license_repository = True

# (str) The android google play services base license repository version to use
# android.google_play_services_base_license_repository_version = 47.0.0

# (bool) Use the android google play services cast repository
# android.google_play_services_cast_repository = True

# (str) The android google play services cast repository version to use
# android.google_play_services_cast_repository_version = 47.0.0

# (bool) Use the android google play services cast framework repository
# android.google_play_services_cast_framework_repository = True

# (str) The android google play services cast framework repository version to use
# android.google_play_services_cast_framework_repository_version = 47.0.0

# (bool) Use the android google play services clearcut repository
# android.google_play_services_clearcut_repository = True

# (str) The android google play services clearcut repository version to use
# android.google_play_services_clearcut_repository_version = 47.0.0

# (bool) Use the android google play services context manager repository
# android.google_play_services_context_manager_repository = True

# (str) The android google play services context manager repository version to use
# android.google_play_services_context_manager_repository_version = 47.0.0

# (bool) Use the android google play services drive repository
# android.google_play_services_drive_repository = True

# (str) The android google play services drive repository version to use
# android.google_play_services_drive_repository_version = 47.0.0

# (bool) Use the android google play services fitness repository
# android.google_play_services_fitness_repository = True

# (str) The android google play services fitness repository version to use
# android.google_play_services_fitness_repository_version = 47.0.0

# (bool) Use the android google play services games repository
# android.google_play_services_games_repository = True

# (str) The android google play services games repository version to use
# android.google_play_services_games_repository_version = 47.0.0

# (bool) Use the android google play services games configuration repository
# android.google_play_services_games_configuration_repository = True

# (str) The android google play services games configuration repository version to use
# android.google_play_services_games_configuration_repository_version = 47.0.0

# (bool) Use the android google play services gass repository
# android.google_play_services_gass_repository = True

# (str) The android google play services gass repository version to use
# android.google_play_services_gass_repository_version = 47.0.0

# (bool) Use the android google play services gcm repository
# android.google_play_services_gcm_repository = True

# (str) The android google play services gcm repository version to use
# android.google_play_services_gcm_repository_version = 47.0.0

# (bool) Use the android google play services location repository
# android.google_play_services_location_repository = True

# (str) The android google play services location repository version to use
# android.google_play_services_location_repository_version = 47.0.0

# (bool) Use the android google play services maps repository
# android.google_play_services_maps_repository = True

# (str) The android google play services maps repository version to use
# android.google_play_services_maps_repository_version = 47.0.0

# (bool) Use the android google play services measurement repository
# android.google_play_services_measurement_repository = True

# (str) The android google play services measurement repository version to use
# android.google_play_services_measurement_repository_version = 47.0.0

# (bool) Use the android google play services measurement base repository
# android.google_play_services_measurement_base_repository = True

# (str) The android google play services measurement base repository version to use
# android.google_play_services_measurement_base_repository_version = 47.0.0

# (bool) Use the android google play services measurement converter repository
# android.google_play_services_measurement_converter_repository = True

# (str) The android google play services measurement converter repository version to use
# android.google_play_services_measurement_converter_repository_version = 47.0.0

# (bool) Use the android google play services measurement impl repository
# android.google_play_services_measurement_impl_repository = True

# (str) The android google play services measurement impl repository version to use
# android.google_play_services_measurement_impl_repository_version = 47.0.0

# (bool) Use the android google play services measurement sdk api repository
# android.google_play_services_measurement_sdk_api_repository = True

# (str) The android google play services measurement sdk api repository version to use
# android.google_play_services_measurement_sdk_api_repository_version = 47.0.0

# (bool) Use the android google play services ml kit barcode scanning repository
# android.google_play_services_ml_kit_barcode_scanning_repository = True

# (str) The android google play services ml kit barcode scanning repository version to use
# android.google_play_services_ml_kit_barcode_scanning_repository_version = 47.0.0

# (bool) Use the android google play services ml kit common repository
# android.google_play_services_ml_kit_common_repository = True

# (str) The android google play services ml kit common repository version to use
# android.google_play_services_ml_kit_common_repository_version = 47.0.0

# (bool) Use the android google play services ml kit face detection repository
# android.google_play_services_ml_kit_face_detection_repository = True

# (str) The android google play services ml kit face detection repository version to use
# android.google_play_services_ml_kit_face_detection_repository_version = 47.0.0

# (bool) Use the android google play services ml kit image labeling repository
# android.google_play_services_ml_kit_image_labeling_repository = True

# (str) The android google play services ml kit image labeling repository version to use
# android.google_play_services_ml_kit_image_labeling_repository_version = 47.0.0

# (bool) Use the android google play services ml kit image labeling custom repository
# android.google_play_services_ml_kit_image_labeling_custom_repository = True

# (str) The android google play services ml kit image labeling custom repository version to use
# android.google_play_services_ml_kit_image_labeling_custom_repository_version = 47.0.0

# (bool) Use the android google play services ml kit language id repository
# android.google_play_services_ml_kit_language_id_repository = True

# (str) The android google play services ml kit language id repository version to use
# android.google_play_services_ml_kit_language_id_repository_version = 47.0.0

# (bool) Use the android google play services ml kit object detection and tracking repository
# android.google_play_services_ml_kit_object_detection_and_tracking_repository = True

# (str) The android google play services ml kit object detection and tracking repository version to use
# android.google_play_services_ml_kit_object_detection_and_tracking_repository_version = 47.0.0

# (bool) Use the android google play services ml kit pose detection repository
# android.google_play_services_ml_kit_pose_detection_repository = True

# (str) The android google play services ml kit pose detection repository version to use
# android.google_play_services_ml_kit_pose_detection_repository_version = 47.0.0

# (bool) Use the android google play services ml kit pose detection accurate repository
# android.google_play_services_ml_kit_pose_detection_accurate_repository = True

# (str) The android google play services ml kit pose detection accurate repository version to use
# android.google_play_services_ml_kit_pose_detection_accurate_repository_version = 47.0.0

# (bool) Use the android google play services ml kit text recognition repository
# android.google_play_services_ml_kit_text_recognition_repository = True

# (str) The android google play services ml kit text recognition repository version to use
# android.google_play_services_ml_kit_text_recognition_repository_version = 47.0.0

# (bool) Use the android google play services ml kit text recognition chinese repository
# android.google_play_services_ml_kit_text_recognition_chinese_repository = True

# (str) The android google play services ml kit text recognition chinese repository version to use
# android.google_play_services_ml_kit_text_recognition_chinese_repository_version = 47.0.0

# (bool) Use the android google play services ml kit text recognition devanagari repository
# android.google_play_services_ml_kit_text_recognition_devanagari_repository = True

# (str) The android google play services ml kit text recognition devanagari repository version to use
# android.google_play_services_ml_kit_text_recognition_devanagari_repository_version = 47.0.0

# (bool) Use the android google play services ml kit text recognition japanese repository
# android.google_play_services_ml_kit_text_recognition_japanese_repository = True

# (str) The android google play services ml kit text recognition japanese repository version to use
# android.google_play_services_ml_kit_text_recognition_japanese_repository_version = 47.0.0

# (bool) Use the android google play services ml kit text recognition korean repository
# android.google_play_services_ml_kit_text_recognition_korean_repository = True

# (str) The android google play services ml kit text recognition korean repository version to use
# android.google_play_services_ml_kit_text_recognition_korean_repository_version = 47.0.0

# (bool) Use the android google play services near me repository
# android.google_play_services_near_me_repository = True

# (str) The android google play services near me repository version to use
# android.google_play_services_near_me_repository_version = 47.0.0

# (bool) Use the android google play services panorama repository
# android.google_play_services_panorama_repository = True

# (str) The android google play services panorama repository version to use
# android.google_play_services_panorama_repository_version = 47.0.0

# (bool) Use the android google play services places repository
# android.google_play_services_places_repository = True

# (str) The android google play services places repository version to use
# android.google_play_services_places_repository_version = 47.0.0

# (bool) Use the android google play services places compat repository
# android.google_play_services_places_compat_repository = True

# (str) The android google play services places compat repository version to use
# android.google_play_services_places_compat_repository_version = 47.0.0

# (bool) Use the android google play services safetynet repository
# android.google_play_services_safetynet_repository = True

# (str) The android google play services safetynet repository version to use
# android.google_play_services_safetynet_repository_version = 47.0.0

# (bool) Use the android google play services tagmanager repository
# android.google_play_services_tagmanager_repository = True

# (str) The android google play services tagmanager repository version to use
# android.google_play_services_tagmanager_repository_version = 47.0.0

# (bool) Use the android google play services tagmanager api repository
# android.google_play_services_tagmanager_api_repository = True

# (str) The android google play services tagmanager api repository version to use
# android.google_play_services_tagmanager_api_repository_version = 47.0.0

# (bool) Use the android google play services tagmanager v4 impl repository
# android.google_play_services_tagmanager_v4_impl_repository = True

# (str) The android google play services tagmanager v4 impl repository version to use
# android.google_play_services_tagmanager_v4_impl_repository_version = 47.0.0

# (bool) Use the android google play services tasks repository
# android.google_play_services_tasks_repository = True

# (str) The android google play services tasks repository version to use
# android.google_play_services_tasks_repository_version = 47.0.0

# (bool) Use the android google play services vision repository
# android.google_play_services_vision_repository = True

# (str) The android google play services vision repository version to use
# android.google_play_services_vision_repository_version = 47.0.0

# (bool) Use the android google play services vision common repository
# android.google_play_services_vision_common_repository = True

# (str) The android google play services vision common repository version to use
# android.google_play_services_vision_common_repository_version = 47.0.0

# (bool) Use the android google play services vision face detector repository
# android.google_play_services_vision_face_detector_repository = True

# (str) The android google play services vision face detector repository version to use
# android.google_play_services_vision_face_detector_repository_version = 47.0.0

# (bool) Use the android google play services vision image labeler repository
# android.google_play_services_vision_image_labeler_repository = True

# (str) The android google play services vision image labeler repository version to use
# android.google_play_services_vision_image_labeler_repository_version = 47.0.0

# (bool) Use the android google play services vision text detector repository
# android.google_play_services_vision_text_detector_repository = True

# (str) The android google play services vision text detector repository version to use
# android.google_play_services_vision_text_detector_repository_version = 47.0.0

# (bool) Use the android google play services wallet repository
# android.google_play_services_wallet_repository = True

# (str) The android google play services wallet repository version to use
# android.google_play_services_wallet_repository_version = 47.0.0

# (bool) Use the android google play services wearable repository
# android.google_play_services_wearable_repository = True

# (str) The android google play services wearable repository version to use
# android.google_play_services_wearable_repository_version = 47.0.0

# (bool) Use the android jetifier
# android.jetifier = True

# (str) The android jetifier version to use
# android.jetifier_version = 1.0.0-beta09

# (bool) Use the android androidx
# android.androidx = True

# (str) The android androidx version to use
# android.androidx_version = 1.0.0

# (bool) Use the android constraint layout
# android.constraint_layout = True

# (str) The android constraint layout version to use
# android.constraint_layout_version = 2.1.0

# (bool) Use the android material components
# android.material_components = True

# (str) The android material components version to use
# android.material_components_version = 1.4.0

# (bool) Use the android legacy support
# android.legacy_support = True

# (str) The android legacy support version to use
# android.legacy_support_version = 1.0.0

# (bool) Use the android multidex
# android.multidex = True

# (int) The android multidex min sdk
# android.multidex_min_sdk = 21

# (bool) Use the android androidx appcompat
# android.androidx_appcompat = True

# (str) The android androidx appcompat version to use
# android.androidx_appcompat_version = 1.4.0

# (bool) Use the android androidx cardview
# android.androidx_cardview = True

# (str) The android androidx cardview version to use
# android.androidx_cardview_version = 1.0.0

# (bool) Use the android androidx constraint layout
# android.androidx_constraint_layout = True

# (str) The android androidx constraint layout version to use
# android.androidx_constraint_layout_version = 2.1.0

# (bool) Use the android androidx core
# android.androidx_core = True

# (str) The android androidx core version to use
# android.androidx_core_version = 1.7.0

# (bool) Use the android androidx design
# android.androidx_design = True

# (str) The android androidx design version to use
# android.androidx_design_version = 1.4.0

# (bool) Use the android androidx drawerlayout
# android.androidx_drawerlayout = True

# (str) The android androidx drawerlayout version to use
# android.androidx_drawerlayout_version = 1.1.1

# (bool) Use the android androidx gridlayout
# android.androidx_gridlayout = True

# (str) The android androidx gridlayout version to use
# android.androidx_gridlayout_version = 1.0.0

# (bool) Use the android androidx lifecycle
# android.androidx_lifecycle = True

# (str) The android androidx lifecycle version to use
# android.androidx_lifecycle_version = 2.4.0

# (bool) Use the android androidx preference
# android.androidx_preference = True

# (str) The android androidx preference version to use
# android.androidx_preference_version = 1.1.1

# (bool) Use the android androidx recyclerview
# android.androidx_recyclerview = True

# (str) The android androidx recyclerview version to use
# android.androidx_recyclerview_version = 1.2.1

# (bool) Use the android androidx transition
# android.androidx_transition = True

# (str) The android androidx transition version to use
# android.androidx_transition_version = 1.4.1

# (bool) Use the android androidx vector drawable
# android.androidx_vector_drawable = True

# (str) The android androidx vector drawable version to use
# android.androidx_vector_drawable_version = 1.1.0

# (bool) Use the android androidx viewpager
# android.androidx_viewpager = True

# (str) The android androidx viewpager version to use
# android.androidx_viewpager_version = 1.0.0

# (bool) Use the android androidx viewpager2
# android.androidx_viewpager2 = True

# (str) The android androidx viewpager2 version to use
# android.androidx_viewpager2_version = 1.0.0

# (bool) Use the android androidx swiperefreshlayout
# android.androidx_swiperefreshlayout = True

# (str) The android androidx swiperefreshlayout version to use
# android.androidx_swiperefreshlayout_version = 1.1.0

# (bool) Use the android androidx coordinatorlayout
# android.androidx_coordinatorlayout = True

# (str) The android androidx coordinatorlayout version to use
# android.androidx_coordinatorlayout_version = 1.1.0

# (bool) Use the android androidx asynclayoutinflater
# android.androidx_asynclayoutinflater = True

# (str) The android androidx asynclayoutinflater version to use
# android.androidx_asynclayoutinflater_version = 1.0.0

# (bool) Use the android androidx customview
# android.androidx_customview = True

# (str) The android androidx customview version to use
# android.androidx_customview_version = 1.1.0

# (bool) Use the android androidx documentfile
# android.androidx_documentfile = True

# (str) The android androidx documentfile version to use
# android.androidx_documentfile_version = 1.0.1

# (bool) Use the android androidx localbroadcastmanager
# android.androidx_localbroadcastmanager = True

# (str) The android androidx localbroadcastmanager version to use
# android.androidx_localbroadcastmanager_version = 1.0.0

# (bool) Use the android androidx print
# android.androidx_print = True

# (str) The android androidx print version to use
# android.androidx_print_version = 1.0.0

# (bool) Use the android androidx slidingpanelayout
# android.androidx_slidingpanelayout = True

# (str) The android androidx slidingpanelayout version to use
# android.androidx_slidingpanelayout_version = 1.2.0

# (bool) Use the android androidx versionedparcelable
# android.androidx_versionedparcelable = True

# (str) The android androidx versionedparcelable version to use
# android.androidx_versionedparcelable_version = 1.1.1

# (bool) Use the android androidx cursoradapter
# android.androidx_cursoradapter = True

# (str) The android androidx cursoradapter version to use
# android.androidx_cursoradapter_version = 1.0.0

# (bool) Use the android androidx fragment
# android.androidx_fragment = True

# (str) The android androidx fragment version to use
# android.androidx_fragment_version = 1.4.0

# (bool) Use the android androidx loader
# android.androidx_loader = True

# (str) The android androidx loader version to use
# android.androidx_loader_version = 1.1.0

# (bool) Use the android androidx resourceinspection
# android.androidx_resourceinspection = True

# (str) The android androidx resourceinspection version to use
# android.androidx_resourceinspection_version = 1.0.1

# (bool) Use the android androidx savedstate
# android.androidx_savedstate = True

# (str) The android androidx savedstate version to use
# android.androidx_savedstate_version = 1.1.0

# (bool) Use the android androidx viewpager2
# android.androidx_viewpager2 = True

# (str) The android androidx viewpager2 version to use
# android.androidx_viewpager2_version = 1.0.0

# (bool) Use the android androidx work
# android.androidx_work = True

# (str) The android androidx work version to use
# android.androidx_work_version = 2.7.0

# (bool) Use the android androidx datastore
# android.androidx_datastore = True

# (str) The android androidx datastore version to use
# android.androidx_datastore_version = 1.0.0

# (bool) Use the android androidx datastore preferences
# android.androidx_datastore_preferences = True

# (str) The android androidx datastore preferences version to use
# android.androidx_datastore_preferences_version = 1.0.0

# (bool) Use the android androidx navigation
# android.androidx_navigation = True

# (str) The android androidx navigation version to use
# android.androidx_navigation_version = 2.4.0

# (bool) Use the android androidx navigation fragment
# android.androidx_navigation_fragment = True

# (str) The android androidx navigation fragment version to use
# android.androidx_navigation_fragment_version = 2.4.0

# (bool) Use the android androidx navigation ui
# android.androidx_navigation_ui = True

# (str) The android androidx navigation ui version to use
# android.androidx_navigation_ui_version = 2.4.0

# (bool) Use the android androidx navigation dynamic features fragment
# android.androidx_navigation_dynamic_features_fragment = True

# (str) The android androidx navigation dynamic features fragment version to use
# android.androidx_navigation_dynamic_features_fragment_version = 2.4.0

# (bool) Use the android androidx paging
# android.androidx_paging = True

# (str) The android androidx paging version to use
# android.androidx_paging_version = 3.1.0

# (bool) Use the android androidx paging common
# android.androidx_paging_common = True

# (str) The android androidx paging common version to use
# android.androidx_paging_common_version = 3.1.0

# (bool) Use the android androidx paging runtime
# android.androidx_paging_runtime = True

# (str) The android androidx paging runtime version to use
# android.androidx_paging_runtime_version = 3.1.0

# (bool) Use the android androidx paging rxjava2
# android.androidx_paging_rxjava2 = True

# (str) The android androidx paging rxjava2 version to use
# android.androidx_paging_rxjava2_version = 3.1.0

# (bool) Use the android androidx paging rxjava3
# android.androidx_paging_rxjava3 = True

# (str) The android androidx paging rxjava3 version to use
# android.androidx_paging_rxjava3_version = 3.1.0

# (bool) Use the android androidx paging guava
# android.androidx_paging_guava = True

# (str) The android androidx paging guava version to use
# android.androidx_paging_guava_version = 3.1.0

# (bool) Use the android androidx room
# android.androidx_room = True

# (str) The android androidx room version to use
# android.androidx_room_version = 2.4.0

# (bool) Use the android androidx room common
# android.androidx_room_common = True

# (str) The android androidx room common version to use
# android.androidx_room_common_version = 2.4.0

# (bool) Use the android androidx room runtime
# android.androidx_room_runtime = True

# (str) The android androidx room runtime version to use
# android.androidx_room_runtime_version = 2.4.0

# (bool) Use the android androidx room rxjava2
# android.androidx_room_rxjava2 = True

# (str) The android androidx room rxjava2 version to use
# android.androidx_room_rxjava2_version = 2.4.0

# (bool) Use the android androidx room rxjava3
# android.androidx_room_rxjava3 = True

# (str) The android androidx room rxjava3 version to use
# android.androidx_room_rxjava3_version = 2.4.0

# (bool) Use the android androidx room guava
# android.androidx_room_guava = True

# (str) The android androidx room guava version to use
# android.androidx_room_guava_version = 2.4.0

# (bool) Use the android androidx room testing
# android.androidx_room_testing = True

# (str) The android androidx room testing version to use
# android.androidx_room_testing_version = 2.4.0

# (bool) Use the android androidx sqlite
# android.androidx_sqlite = True

# (str) The android androidx sqlite version to use
# android.androidx_sqlite_version = 2.2.0

# (bool) Use the android androidx sqlite framework
# android.androidx_sqlite_framework = True

# (str) The android androidx sqlite framework version to use
# android.androidx_sqlite_framework_version = 2.2.0

# (bool) Use the android androidx annotations
# android.androidx_annotations = True

# (str) The android androidx annotations version to use
# android.androidx_annotations_version = 1.3.0

# (bool) Use the android androidx collection
# android.androidx_collection = True

# (str) The android androidx collection version to use
# android.androidx_collection_version = 1.2.0

# (bool) Use the android androidx concurrent
# android.androidx_concurrent = True

# (str) The android androidx concurrent version to use
# android.androidx_concurrent_version = 1.1.0

# (bool) Use the android androidx interpolator
# android.androidx_interpolator = True

# (str) The android androidx interpolator version to use
# android.androidx_interpolator_version = 1.0.0

# (bool) Use the android androidx cursoradapter
# android.androidx_cursoradapter = True

# (str) The android androidx cursoradapter version to use
# android.androidx_cursoradapter_version = 1.0.0

# (bool) Use the android androidx fragment
# android.androidx_fragment = True

# (str) The android androidx fragment version to use
# android.androidx_fragment_version = 1.4.0

# (bool) Use the android androidx loader
# android.androidx_loader = True

# (str) The android androidx loader version to use
# android.androidx_loader_version = 1.1.0

# (bool) Use the android androidx resourceinspection
# android.androidx_resourceinspection = True

# (str) The android androidx resourceinspection version to use
# android.androidx_resourceinspection_version = 1.0.1

# (bool) Use the android androidx savedstate
# android.androidx_savedstate = True

# (str) The android androidx savedstate version to use
# android.androidx_savedstate_version = 1.1.0

# (bool) Use the android androidx viewpager2
# android.androidx_viewpager2 = True

# (str) The android androidx viewpager2 version to use
# android.androidx_viewpager2_version = 1.0.0

# (bool) Use the android androidx work
# android.androidx_work = True

# (str) The android androidx work version to use
# android.androidx_work_version = 2.7.0

# (bool) Use the android androidx datastore
# android.androidx_datastore = True

# (str) The android androidx datastore version to use
# android.androidx_datastore_version = 1.0.0

# (bool) Use the android androidx datastore preferences
# android.androidx_datastore_preferences = True

# (str) The android androidx datastore preferences version to use
# android.androidx_datastore_preferences_version = 1.0.0

# (bool) Use the android androidx navigation
# android.androidx_navigation = True

# (str) The android androidx navigation version to use
# android.androidx_navigation_version = 2.4.0

# (bool) Use the android androidx navigation fragment
# android.androidx_navigation_fragment = True

# (str) The android androidx navigation fragment version to use
# android.androidx_navigation_fragment_version = 2.4.0

# (bool) Use the android androidx navigation ui
# android.androidx_navigation_ui = True

# (str) The android androidx navigation ui version to use
# android.androidx_navigation_ui_version = 2.4.0

# (bool) Use the android androidx navigation dynamic features fragment
# android.androidx_navigation_dynamic_features_fragment = True

# (str) The android androidx navigation dynamic features fragment version to use
# android.androidx_navigation_dynamic_features_fragment_version = 2.4.0

# (bool) Use the android androidx paging
# android.androidx_paging = True

# (str) The android androidx paging version to use
# android.androidx_paging_version = 3.1.0

# (bool) Use the android androidx paging common
# android.androidx_paging_common = True

# (str) The android androidx paging common version to use
# android.androidx_paging_common_version = 3.1.0

# (bool) Use the android androidx paging runtime
# android.androidx_paging_runtime = True

# (str) The android androidx paging runtime version to use
# android.androidx_paging_runtime_version = 3.1.0

# (bool) Use the android androidx paging rxjava2
# android.androidx_paging_rxjava2 = True

# (str) The android androidx paging rxjava2 version to use
# android.androidx_paging_rxjava2_version = 3.1.0

# (bool) Use the android androidx paging rxjava3
# android.androidx_paging_rxjava3 = True

# (str) The android androidx paging rxjava3 version to use
# android.androidx_paging_rxjava3_version = 3.1.0

# (bool) Use the android androidx paging guava
# android.androidx_paging_guava = True

# (str) The android androidx paging guava version to use
# android.androidx_paging_guava_version = 3.1.0

# (bool) Use the android androidx room
# android.androidx_room = True

# (str) The android androidx room version to use
# android.androidx_room_version = 2.4.0

# (bool) Use the android androidx room common
# android.androidx_room_common = True

# (str) The android androidx room common version to use
# android.androidx_room_common_version = 2.4.0

# (bool) Use the android androidx room runtime
# android.androidx_room_runtime = True

# (str) The android androidx room runtime version to use
# android.androidx_room_runtime_version = 2.4.0

# (bool) Use the android androidx room rxjava2
# android.androidx_room_rxjava2 = True

# (str) The android androidx room rxjava2 version to use
# android.androidx_room_rxjava2_version = 2.4.0

# (bool) Use the android androidx room rxjava3
# android.androidx_room_rxjava3 = True

# (str) The android androidx room rxjava3 version to use
# android.androidx_room_rxjava3_version = 2.4.0

# (bool) Use the android androidx room guava
# android.androidx_room_guava = True

# (str) The android androidx room guava version to use
# android.androidx_room_guava_version = 2.4.0

# (bool) Use the android androidx room testing
# android.androidx_room_testing = True

# (str) The android androidx room testing version to use
# android.androidx_room_testing_version = 2.4.0

# (bool) Use the android androidx sqlite
# android.androidx_sqlite = True

# (str) The android androidx sqlite version to use
# android.androidx_sqlite_version = 2.2.0

# (bool) Use the android androidx sqlite framework
# android.androidx_sqlite_framework = True

# (str) The android androidx sqlite framework version to use
# android.androidx_sqlite_framework_version = 2.2.0

# (bool) Use the android androidx annotations
# android.androidx_annotations = True

# (str) The android androidx annotations version to use
# android.androidx_annotations_version = 1.3.0

# (bool) Use the android androidx collection
# android.androidx_collection = True

# (str) The android androidx collection version to use
# android.androidx_collection_version = 1.2.0

# (bool) Use the android androidx concurrent
# android.androidx_concurrent = True

# (str) The android androidx concurrent version to use
# android.androidx_concurrent_version = 1.1.0

# (bool) Use the android androidx interpolator
# android.androidx_interpolator = True

# (str) The android androidx interpolator version to use
# android.androidx_interpolator_version = 1.0.0
