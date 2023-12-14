# Released under the MIT License. See LICENSE for details.
#
"""Ballistica user interface api version 1"""

# ba_meta require api 8

# The stuff we expose here at the top level is our 'public' api.
# It should only be imported by code outside of this package or
# from 'if TYPE_CHECKING' blocks (which will not exec at runtime).
# Code within our package should import things directly from their
# submodules.

from __future__ import annotations

# pylint: disable=redefined-builtin

import logging

from efro.util import set_canonical_module_names
from babase import (
    add_clean_frame_callback,
    app,
    AppIntent,
    AppIntentDefault,
    AppIntentExec,
    AppMode,
    appname,
    appnameupper,
    apptime,
    AppTime,
    apptimer,
    AppTimer,
    Call,
    fullscreen_control_available,
    fullscreen_control_get,
    fullscreen_control_key_shortcut,
    fullscreen_control_set,
    charstr,
    clipboard_is_supported,
    clipboard_set_text,
    commit_app_config,
    ContextRef,
    displaytime,
    DisplayTime,
    displaytimer,
    DisplayTimer,
    do_once,
    fade_screen,
    get_display_resolution,
    get_ip_address_type,
    get_low_level_config_value,
    get_max_graphics_quality,
    get_remote_app_name,
    get_replays_dir,
    get_string_height,
    get_string_width,
    get_type_name,
    getclass,
    have_permission,
    in_logic_thread,
    increment_analytics_count,
    is_browser_likely_available,
    is_running_on_fire_tv,
    is_xcode_build,
    lock_all_input,
    LoginAdapter,
    LoginInfo,
    Lstr,
    native_review_request,
    native_review_request_supported,
    NotFoundError,
    Permission,
    Plugin,
    PluginSpec,
    pushcall,
    quit,
    QuitType,
    request_permission,
    safecolor,
    screenmessage,
    set_analytics_screen,
    set_low_level_config_value,
    set_ui_input_device,
    SpecialChar,
    supports_max_fps,
    supports_vsync,
    timestring,
    UIScale,
    unlock_all_input,
    WeakCall,
    workspaces_in_use,
)

from _bauiv1 import (
    buttonwidget,
    checkboxwidget,
    columnwidget,
    containerwidget,
    get_qrcode_texture,
    get_special_widget,
    getmesh,
    getsound,
    gettexture,
    hscrollwidget,
    imagewidget,
    is_party_icon_visible,
    Mesh,
    open_file_externally,
    open_url,
    rowwidget,
    scrollwidget,
    set_party_icon_always_visible,
    set_party_window_open,
    show_ad,
    show_ad_2,
    show_online_score_ui,
    Sound,
    Texture,
    textwidget,
    uibounds,
    Widget,
    widget,
)
from bauiv1._keyboard import Keyboard
from bauiv1._uitypes import Window, uicleanupcheck
from bauiv1._subsystem import UIV1Subsystem

__all__ = [
    'add_clean_frame_callback',
    'app',
    'AppIntent',
    'AppIntentDefault',
    'AppIntentExec',
    'AppMode',
    'appname',
    'appnameupper',
    'appnameupper',
    'apptime',
    'AppTime',
    'apptimer',
    'AppTimer',
    'buttonwidget',
    'Call',
    'fullscreen_control_available',
    'fullscreen_control_get',
    'fullscreen_control_key_shortcut',
    'fullscreen_control_set',
    'charstr',
    'checkboxwidget',
    'clipboard_is_supported',
    'clipboard_set_text',
    'columnwidget',
    'commit_app_config',
    'containerwidget',
    'ContextRef',
    'displaytime',
    'DisplayTime',
    'displaytimer',
    'DisplayTimer',
    'do_once',
    'fade_screen',
    'get_display_resolution',
    'get_ip_address_type',
    'get_low_level_config_value',
    'get_max_graphics_quality',
    'get_qrcode_texture',
    'get_remote_app_name',
    'get_replays_dir',
    'get_special_widget',
    'get_string_height',
    'get_string_width',
    'get_type_name',
    'getclass',
    'getmesh',
    'getsound',
    'gettexture',
    'have_permission',
    'hscrollwidget',
    'imagewidget',
    'in_logic_thread',
    'increment_analytics_count',
    'is_browser_likely_available',
    'is_party_icon_visible',
    'is_running_on_fire_tv',
    'is_xcode_build',
    'Keyboard',
    'lock_all_input',
    'LoginAdapter',
    'LoginInfo',
    'Lstr',
    'Mesh',
    'native_review_request',
    'native_review_request_supported',
    'NotFoundError',
    'open_file_externally',
    'open_url',
    'Permission',
    'Plugin',
    'PluginSpec',
    'pushcall',
    'quit',
    'QuitType',
    'request_permission',
    'rowwidget',
    'safecolor',
    'screenmessage',
    'scrollwidget',
    'set_analytics_screen',
    'set_low_level_config_value',
    'set_party_icon_always_visible',
    'set_party_window_open',
    'set_ui_input_device',
    'show_ad',
    'show_ad_2',
    'show_online_score_ui',
    'Sound',
    'SpecialChar',
    'supports_max_fps',
    'supports_vsync',
    'Texture',
    'textwidget',
    'timestring',
    'uibounds',
    'uicleanupcheck',
    'UIScale',
    'UIV1Subsystem',
    'unlock_all_input',
    'WeakCall',
    'widget',
    'Widget',
    'Window',
    'workspaces_in_use',
]

# We want stuff to show up as bauiv1.Foo instead of bauiv1._sub.Foo.
set_canonical_module_names(globals())

# Sanity check: we want to keep ballistica's dependencies and
# bootstrapping order clearly defined; let's check a few particular
# modules to make sure they never directly or indirectly import us
# before their own execs complete.
if __debug__:
    for _mdl in 'babase', '_babase':
        if not hasattr(__import__(_mdl), '_REACHED_END_OF_MODULE'):
            logging.warning(
                '%s was imported before %s finished importing;'
                ' should not happen.',
                __name__,
                _mdl,
            )
