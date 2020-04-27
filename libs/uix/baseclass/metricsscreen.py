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

import kivy
kivy.require('1.11.1')
from kivy.uix.screenmanager import Screen
import libs.applibs.profilem.enumandconst as enumandconst

class MetricsScreen(Screen):
    '''
        Screen to enter all the metrics related to a profile
    '''
    def initProfileUpdate(self, metricToSave, *args):
        '''
            Update (in memory only) the current Profile with the modified value
        '''
        if (metricToSave == 'heightIntegerPart'):
            valueToSave = int(self.ids.profile_height_integerpart.text)
            if (valueToSave >=0 and valueToSave <= 2):
                kivy.app.App.get_running_app().myProfile.heightIntegerPart = valueToSave

        if (metricToSave == 'profileName'):
            valueToSave = str(self.ids.profile_name.text)
            if (len(valueToSave) > 0):
                kivy.app.App.get_running_app().myProfile.profileName = valueToSave
                 
        if (metricToSave == 'heightDecimalPart'):
            valueToSave = int(self.ids.profile_height_decimalpart.text)
            if (valueToSave >= 0 and valueToSave <= 99):
                kivy.app.App.get_running_app().myProfile.heightDecimalPart = valueToSave

        if (metricToSave == 'weightIntegerPart'):
            valueToSave = int(self.ids.profile_weight_integerpart.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.weightIntegerPart = valueToSave

        if (metricToSave == 'weightDecimalPart'):
            valueToSave = int(self.ids.profile_weight_decimalpart.text)
            if (valueToSave >= 0 and valueToSave <= 99):
                kivy.app.App.get_running_app().myProfile.weightDecimalPart = valueToSave

        if (metricToSave == 'age'):
            valueToSave = int(self.ids.profile_age.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.age = valueToSave

        if (metricToSave == 'gender'):
            valueToSave = str(self.ids.profile_gender.text)
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllGenders()['0'])):
                 kivy.app.App.get_running_app().myProfile.gender = enumandconst.Gender.FEMALE
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllGenders()['1'])):
                 kivy.app.App.get_running_app().myProfile.gender = enumandconst.Gender.MALE

        if (metricToSave == 'activityFactor'):
            valueToSave = str(self.ids.profile_activityFactor.text)
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['1'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.SEDENTARY
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['2'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.LIGHTLYACTIVE
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['3'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.MODERATELYACTIVE
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['4'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.ACTIVE
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['5'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.VIGOROUS
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['6'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.VIGOROUSLYACTIVE

        if (metricToSave == 'femaletriceps'):
            valueToSave = int(self.ids.profile_female_triceps.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.triceps = valueToSave

        if (metricToSave == 'femalesuprailium'):
            valueToSave = int(self.ids.profile_female_suprailium.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.suprailium = valueToSave

        if (metricToSave == 'femalethigh'):
            valueToSave = int(self.ids.profile_female_thigh.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.thigh = valueToSave

        if (metricToSave == 'maletriceps'):
            valueToSave = int(self.ids.profile_male_triceps.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.triceps = valueToSave

        if (metricToSave == 'maleabdomen'):
            valueToSave = int(self.ids.profile_male_abdomen.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.abdomen = valueToSave

        if (metricToSave == 'malethigh'):
            valueToSave = int(self.ids.profile_male_thigh.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.thigh = valueToSave

    def on_focus(self, focused, metricToSave):
        '''
            Triggered by TextInput.
            Is intended to save the value when the focus is lost
        '''
        if focused:
            pass
        else:
            self.initProfileUpdate(metricToSave)

