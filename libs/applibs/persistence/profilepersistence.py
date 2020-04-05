# Module to persist (save/load) profiles created in the application Keep Up The Pace
import shelve
from random import randrange
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import libs.applibs.profilem.profile as profile
import libs.applibs.profilem.enumandconst as enumandconst

def loadprofiles():
    '''
        Load all the previous saved profiles in a list and return the list
    '''
    profilelist = []
    try:
        shelf = shelve.open("profileshelf")
        if (len(shelf) != 0):
            profilelist = list(shelf.values())
            #TODO iterate the list and populate the registry with all the profiles
            for p in profilelist:
                p.addToRegistry()
        return profilelist
    finally:
        shelf.close

def getDefaultProfileFromShelf():
    '''
        Load all the previous saved profiles in a list and extract the one market as default.
        Return both the list and the default profile
    '''
    pl = loadprofiles()
    profiletoreturn = None
    if (len(pl) !=0):
        for aProfile in pl:
            if aProfile.isdefault:
                profiletoreturn = aProfile
        if (profiletoreturn is None):
            #no default profile found, return the first one
            profiletoreturn = pl[0]
            profiletoreturn.isdefault = True
    return pl, profiletoreturn

def saveprofiles():
    '''
        Save all the instances of the class Profile
    '''
    try:
        shelf = shelve.open('profileshelf')
        for ProfileObject in profile.Profile._registry:
            id = str(ProfileObject.uid)
            shelf[id] = ProfileObject
    finally:
        shelf.close

def deleteprofile(Profileinstance):
    '''
        Delete an instance of the class Profile from the shelf
    '''
    if isinstance(Profileinstance, profile.Profile):
        try:
            shelf = shelve.open('profileshelf')
            if str(Profileinstance.id) in shelf:
                id = str(Profileinstance.uid)
                del shelf[id]
        finally:
            shelf.close

def clearProfiles():
    '''
        Clear all previously saved profiles
    '''
    try:
        shelf = shelve.open('profileshelf')
        if len(shelf) != 0:
            shelf.clear()
    finally:
        shelf.close


if __name__ == "__main__":
    
    # verify that the shelf is empty. Empty it otherwise
    clearProfiles()
    # create 2 profiles
    FirstProfile = profile.Profile('test1')
    FirstProfile.age = 35
    FirstProfile.isdefault = True
    FirstProfile.gender = enumandconst.Gender.FEMALE
    FirstProfile.weightIntegerPart = 60
    FirstProfile.weightDecimalPart = 0
    FirstProfile.heightIntegerPart = 1
    FirstProfile.heightDecimalPart = 68
    FirstProfile.metricChoice = enumandconst.MetricChoice.ISO
    FirstProfile.computeBMI()

    SecondProfile = profile.Profile('test2')
    SecondProfile.age = 35
    SecondProfile.gender = enumandconst.Gender.FEMALE
    SecondProfile.weightIntegerPart = 60
    SecondProfile.weightDecimalPart = 0
    SecondProfile.heightIntegerPart = 1
    SecondProfile.heightDecimalPart = 68
    SecondProfile.metricChoice = enumandconst.MetricChoice.ISO
    SecondProfile.computeBMI()

    # save then display saved profiles (2 expected)
    saveprofiles()
    profileList = loadprofiles()
    for pr in profileList:
        print(pr.profileName)
        if pr.isdefault:
            print('That one was default')

    # get the default one and print its name
    l, p = getDefaultProfileFromShelf()
    print(p.profileName)
    print('it was again the default')

    # delete one profile
    position = randrange(0, 1)
    aProfile = profileList[position]
    deleteprofile(aProfile)

    # display saved profiles (one expected)
    profileList = loadprofiles()
    for pr in profileList:
        print(pr.profileName)

    # delete all save profiles
    clearProfiles()