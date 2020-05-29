# -*- coding: utf-8 -*-
#
# This file created with KivyCreatorProject
# <https://github.com/HeaTTheatR/KivyCreatorProgect
#
# Copyright (c) 2020 Ivanov Yuri and KivyMD
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>
#
# LICENSE: MIT

import os
import sys
from ast import literal_eval

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.clock import Clock
from kivy.utils import get_hex_from_color
import kivy.properties as properties

from main import __version__
from libs.translation import Translation
from libs.uix.baseclass.startscreen import StartScreen
from libs.uix.lists import Lists

from libs.applibs.kivymd.app import MDApp
from libs.applibs.kivymd.toast import toast
from kivy.core.text import LabelBase
from libs.applibs.kivymd.font_definitions import theme_font_styles


from libs.applibs.dialogs import card

import libs.applibs.profilem.profile as profile
import libs.applibs.profilem.enumandconst as enumandconst
import libs.applibs.persistence.profilepersistence as persistence
import libs.applibs.compendium.c01bicycling as c01
import libs.applibs.compendium.c02conditioningexercise as c02
import libs.applibs.compendium.c03dancing as c03
import libs.applibs.compendium.c04fishinghunting as c04
import libs.applibs.compendium.c05homeactivity as c05
import libs.applibs.compendium.c06homerepair as c06
import libs.applibs.compendium.c07inactivity as c07
import libs.applibs.compendium.c08lawngarden as c08
import libs.applibs.compendium.c09miscellaneous as c09
import libs.applibs.compendium.c10musicplaying as c10
import libs.applibs.compendium.c11occupation as c11
import libs.applibs.compendium.c12running as c12
import libs.applibs.compendium.c13selfcare as c13
import libs.applibs.compendium.c14sexualactivity as c14
import libs.applibs.compendium.c15sports as c15
import libs.applibs.compendium.c16transportation as c16
import libs.applibs.compendium.c17walking as c17
import libs.applibs.compendium.c18wateractivities as c18
import libs.applibs.compendium.c19winteractivities as c19
import libs.applibs.compendium.c20religiousactivities as c20
import libs.applibs.compendium.c21volunteeractivities as c21

class keepupthepaceMD(MDApp):
    title = 'keepupthepaceMD'
    icon = 'icon.png'
    nav_drawer = properties.ObjectProperty()
    lang = properties.StringProperty('en')
        #load saved profiles and instantiate the default one
    listofprofiles, myProfile = persistence.getDefaultProfileFromShelf()

    # define the properties that will be updated in the user interface
    knbmi = properties.StringProperty('0')
    kbbmi = properties.StringProperty('0')
    krmr1918 = properties.StringProperty('0')
    krmr1984 = properties.StringProperty('0')
    krmr1990 = properties.StringProperty('0')
    krmrml1918 = properties.StringProperty('0')
    krmrml1984 = properties.StringProperty('0')
    krmrml1990 = properties.StringProperty('0')
    khbe1918 = properties.StringProperty('0')
    khbe1984 = properties.StringProperty('0')
    khbe1990 = properties.StringProperty('0')
    kqfp = properties.StringProperty('0')
    kefp = properties.StringProperty('0')

    # initialize a profile to test the app, if none loaded
    if not(isinstance(myProfile, profile.Profile)):
        myProfile=profile.Profile('not coming from shelf')
        myProfile.isdefault = True
        myProfile.age = 35
        myProfile.gender = enumandconst.Gender.FEMALE
        myProfile.weightIntegerPart = 60
        myProfile.weightDecimalPart = 0
        myProfile.heightIntegerPart = 1
        myProfile.heightDecimalPart = 68
        myProfile.metricChoice = enumandconst.MetricChoice.ISO
        myProfile.computeAll()
    else:
        myProfile.computeAll()

    # initialize all the MET tables
    bicycling = c01.Bicycling
    conditionningExercises = c02.ConditionningExercises
    dancing = c03.Dancing
    fishingHunting = c04.FishingHunting
    homeActivity = c05.HomeActivity
    homeRepair = c06.HomeRepair
    inactivity = c07.Inactivity
    lawnGarden = c08.LawnGarden
    miscellaneous = c09.Miscellaneous
    musicPlaying = c10.MusicPlaying
    occupation = c11.Occupation
    running = c12.Running
    selfcare = c13.SelfCare
    sexualActivity = c14.SexualActivity
    sports = c15.Sports
    transportation = c16.Transportation
    walking = c17.Walking
    waterActivities = c18.WaterActivities
    winterActivites = c19.WinterActivities
    religiousActivities = c20.ReligiousActivities
    volunteeractivities = c21.VolunteerActivities

    def __init__(self, **kvargs):
        super(keepupthepaceMD, self).__init__(**kvargs)
        Window.bind(on_keyboard=self.events_program)
        Window.soft_input_mode = 'below_target'

        self.list_previous_screens = ['base']
        self.window = Window
        self.config = ConfigParser()
        self.manager = None
        self.window_language = None
        self.exit_interval = False
        self.gender_menu = None
        self.dict_language = literal_eval(
            open(
                os.path.join(self.directory, 'data', 'locales', 'locales.txt')).read()
        )
        self.translation = Translation(
            self.lang, 'Ttest', os.path.join(self.directory, 'data', 'locales')
        )

        self.listOfMetTables = [self.translation._('01-Bicycling'), 
        self.translation._('02-Conditionning Exercises'),
        self.translation._('03-Dancing'),
        self.translation._('04-Fishing & Hunting'),
        self.translation._('05-Home Activity'),
        self.translation._('06-Home Repair'),
        self.translation._('07-Inactivity'),
        self.translation._('08-Lawn Garden'),
        self.translation._('09-Miscellaneous'),
        self.translation._('10-Music Playing'),
        self.translation._('11-Occupation'),
        self.translation._('12-Runing'),
        self.translation._('13-Self Care'),
        self.translation._('14-Sexual Activity'),
        self.translation._('15-Sports'),
        self.translation._('16-Transportation'),
        self.translation._('17-Walking'),
        self.translation._('18-Water Activities'),
        self.translation._('19-Winter Activities'),
        self.translation._('20-Religious Activities'),
        self.translation._('21-Volunteer Activities')]

    def get_application_config(self):
        return super(keepupthepaceMD, self).get_application_config(
                        '{}/%(appname)s.ini'.format(self.directory))

    def build_config(self, config):
        config.adddefaultsection('General')
        config.setdefault('General', 'language', 'en')

    def set_value_from_config(self):
        self.config.read(os.path.join(self.directory, 'keepupthepacemd.ini'))
        self.lang = self.config.get('General', 'language')

    def build(self):
        LabelBase.register(
            name="Arial",
            fn_regular="Arial.ttf")

        theme_font_styles.append('Arial')
        self.theme_cls.font_styles["Arial"] = [
            "Arial",
            16,
            False,
            0.15,
        ]
        self.set_value_from_config()
        self.load_all_kv_files(os.path.join(self.directory, 'libs', 'uix', 'kv'))
        self.screen = StartScreen()
        self.manager = self.screen.ids.manager
        self.nav_drawer = self.screen.ids.nav_drawer

        return self.screen

    def refreshValuesToDisplayOnScreen(self):
        '''
            Refresh the values to display whenever it's needed
        '''
        self.kbbmi = self.myProfile.displaybBMI()
        self.knbmi = self.myProfile.displaynBMI()
        self.krmr1918, self.krmr1984, self.krmr1990 = self.myProfile.displayRMR()
        self.krmrml1918, self.krmrml1984, self.krmrml1990 = self.myProfile.displayRMRml()
        self.khbe1918, self.khbe1984, self.khbe1990 = self.myProfile.displayHBE()
        self.kqfp, self.kefp = self.myProfile.displayFAT()
    
    def doThingsBetweenScreen(self):
        '''
            save profiles when leaving some selectted tabs
        '''
        self.myProfile.computeAll()
        persistence.saveprofiles()
        self.refreshValuesToDisplayOnScreen()
        

    def on_stop(self):
        persistence.saveprofiles()

    def on_pause(self):
        persistence.saveprofiles()

    def load_all_kv_files(self, directory_kv_files):
        for kv_file in os.listdir(directory_kv_files):
            kv_file = os.path.join(directory_kv_files, kv_file)
            if os.path.isfile(kv_file):
                with open(kv_file, encoding='utf-8') as kv:
                    Builder.load_string(kv.read())

    def events_program(self, instance, keyboard, keycode, text, modifiers):
        if keyboard == 27:
            if self.nav_drawer.state == 'open':
                self.nav_drawer.toggle_nav_drawer()
            self.back_screen(event=keyboard)
        return True

    def back_screen(self, event=None):
        if event == 27:
            if self.manager.current == 'base':
                self.dialog_exit()
                return
            try:
                self.doThingsBetweenScreen()
                self.manager.current = self.list_previous_screens.pop()
            except:
                self.manager.current = 'base'
            self.screen.ids.action_bar.title = self.title
            self.screen.ids.action_bar.left_action_items = \
                [['menu', lambda x: self.nav_drawer.toggle_nav_drawer()]]

    def show_metrics(self, *args):
        self.nav_drawer.toggle_nav_drawer()
        self.manager.current = 'metrics'
        self.screen.ids.action_bar.left_action_items = \
            [['menu', lambda x: self.nav_drawer.toggle_nav_drawer()]]
        self.screen.ids.action_bar.right_action_items = \
            [['chevron-left', lambda x: self.back_screen(27)]]

    def show_onelist(self, *args):
        self.list_previous_screens.append('compendiumlist')
        self.manager.current = 'onelist'
        self.screen.ids.action_bar.left_action_items = \
            [['menu', lambda x: self.nav_drawer.toggle_nav_drawer()]]
        self.screen.ids.action_bar.right_action_items = \
            [['chevron-left', lambda x: self.back_screen(27)]]

    def show_compendium(self, *args):
        self.nav_drawer.toggle_nav_drawer()
        self.manager.current = 'compendiumlist'
        self.screen.ids.action_bar.left_action_items = \
            [['menu', lambda x: self.nav_drawer.toggle_nav_drawer()]]
        self.screen.ids.action_bar.right_action_items = \
            [['chevron-left', lambda x: self.back_screen(27)]]

    def show_about(self, *args):
        self.nav_drawer.toggle_nav_drawer()
        self.screen.ids.about.ids.label.text = \
            self.translation._(
                u'[size=20][b]keepupthepaceMD[/b][/size]\n\n'
                u'[b]Version:[/b] {version}\n'
                u'[b]License:[/b] MIT\n\n'
                u'[size=20][b]Developer[/b][/size]\n\n'
                u'[ref=SITE_PROJECT]'
                u'[color={link_color}]NAME_AUTHOR[/color][/ref]\n\n'
                u'[b]Source code:[/b] '
                u'[ref=REPO_PROJECT]'
                u'[color={link_color}]GitHub[/color][/ref]').format(
                version=__version__,
                link_color=get_hex_from_color(self.theme_cls.primary_color)
            )
        self.manager.current = 'about'
        self.screen.ids.action_bar.left_action_items = \
            [['menu', lambda x: self.nav_drawer.toggle_nav_drawer()]]
        self.screen.ids.action_bar.right_action_items = \
            [['chevron-left', lambda x: self.back_screen(27)]]

    def show_license(self, *args):
        self.nav_drawer.toggle_nav_drawer()
        self.screen.ids.license.ids.text_license.text = \
            self.translation._('%s') % open(
                os.path.join(self.directory, 'LICENSE'), encoding='utf-8').read()
        self.manager.current = 'license'
        self.screen.ids.action_bar.left_action_items = \
            [['menu', lambda x: self.nav_drawer.toggle_nav_drawer()]]
        self.screen.ids.action_bar.right_action_items = \
            [['chevron-left', lambda x: self.back_screen(27)]]
        self.screen.ids.action_bar.title = \
            self.translation._('MIT LICENSE')

    def select_locale(self, *args):
        def select_locale(name_locale):
            for locale in self.dict_language.keys():
                if name_locale == self.dict_language[locale]:
                    self.lang = locale
                    self.config.set('General', 'language', self.lang)
                    self.config.write()

        dict_info_locales = {}
        for locale in self.dict_language.keys():
            dict_info_locales[self.dict_language[locale]] = \
                ['locale', locale == self.lang]

        if not self.window_language:
            self.window_language = card(
                Lists(
                    dict_items=dict_info_locales,
                    events_callback=select_locale, flag='one_select_check'
                ),
                size=(.85, .55)
            )
        self.window_language.open()

    def dialog_exit(self):
        def check_interval_press(interval):
            self.exit_interval += interval
            if self.exit_interval > 5:
                self.exit_interval = False
                Clock.unschedule(check_interval_press)

        if self.exit_interval:
            sys.exit(0)
            
        Clock.schedule_interval(check_interval_press, 1)
        toast(self.translation._('Press Back to Exit'))

    def on_lang(self, instance, lang):
        self.translation.switch_lang(lang)
