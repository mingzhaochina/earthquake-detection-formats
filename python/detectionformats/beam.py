#!/usr/bin/env python

#stdlib imports
import json

# a conversion class used to create, parse, and validate beam data as part of
# detection data.
class Beam:
    BACKAZIMUTH_KEY = "BackAzimuth"
    SLOWNESS_KEY = "Slowness"
    POWERRATIO_KEY = "PowerRatio"
    BACKAZIMUTHERROR_KEY = "BackAzimuthError"
    SLOWNESSERROR_KEY = "SlownessError"
    POWERRATIOERROR_KEY = "PowerRatioError"

    # init
    def __init__(self, newBackAzimuth=None, newSlowness=None, newPowerRatio=None,
        newBackAzimuthError=None, newSlownessError=None,
        newPowerRatioError=None) :
        """Initialize the beam object. Constructs an empty object
           if all arguments are None

        Args:
            newBackAzimuth: a required Number containing the desired back
                azimuth measurement as a float
            newSlowness: a required Number containing the desired slowness
                measurement as a float
            newPowerRatio: an optional Number containing the desired power ratio
                measurement as a float
            newBackAzimuthError: an optional Number containing the desired back
                azimuth error measurement as a float
            newSlownessError: an optional Number containing the desired slowness
                error measurement as a float
            newPowerRatioError: an optional Number containing the desired power
                ratio error measurement as a float
        Returns:
            Nothing
        Raises:
            Nothing
        """
        # first required keys
        if newBackAzimuth is not None:
            self.backAzimuth = newBackAzimuth
        if newSlowness is not None:
            self.slowness = newSlowness

        # second optional keys
        if newPowerRatio is not None:
            self.powerRatio = newPowerRatio
        if newBackAzimuthError is not None:
            self.backAzimuthError = newBackAzimuthError
        if newSlownessError is not None:
            self.slownessError = newSlownessError
        if newPowerRatioError is not None:
            self.powerRatioError = newPowerRatioError

    # populate class from a json string
    def fromJSONString(self, jsonString) :
        """Populates the object from a json formatted string

        Args:
            jsonString: a required String containing the json formatted text
        Returns:
            Nothing
        Raises:
            Nothing
        """
        jsonObject = json.loads(jsonString)
        self.fromDict(jsonObject)

    # populate class from a dictonary
    def fromDict(self, aDict) :
        """Populates the object from a dictonary

        Args:
            aDict: a required Dictonary
        Returns:
            Nothing
        Raises:
            Nothing
        """
        # first required keys
        try:
            self.backAzimuth = aDict[self.BACKAZIMUTH_KEY]
            self.slowness = aDict[self.SLOWNESS_KEY]
        except (ValueError, KeyError, TypeError):
            print ("Dict format error")

        # second optional keys
        if self.POWERRATIO_KEY in aDict:
            self.powerRatio = aDict[self.POWERRATIO_KEY]
        if self.BACKAZIMUTHERROR_KEY in aDict:
            self.backAzimuthError = aDict[self.BACKAZIMUTHERROR_KEY]
        if self.SLOWNESSERROR_KEY in aDict:
            self.slownessError = aDict[self.SLOWNESSERROR_KEY]
        if self.POWERRATIOERROR_KEY in aDict:
            self.powerRatioError = aDict[self.POWERRATIOERROR_KEY]

    # convert class to a json string
    def toJSONString(self) :
        """Converts the object to a json formatted string

        Args:
            None
        Returns:
            The JSON formatted message as a String
        Raises:
            Nothing
        """
        jsonObject = self.toDict()

        return json.dumps(jsonObject, ensure_ascii=False)

    # convert class to a dictonary
    def toDict(self) :
        """Converts the object to a dictonary

        Args:
            None
        Returns:
            The Dictonary
        Raises:
            Nothing
        """
        aDict = {}

        # first required keys
        try:
            aDict[self.BACKAZIMUTH_KEY] = self.backAzimuth
            aDict[self.SLOWNESS_KEY] = self.slowness
        except NameError:
            print ("Missing data error")

        # second optional keys
        try:
            aDict[self.POWERRATIO_KEY] = self.powerRatio
        except:
            pass

        try:
            aDict[self.BACKAZIMUTHERROR_KEY] = self.backAzimuthError
        except:
            pass

        try:
            aDict[self.SLOWNESSERROR_KEY] = self.slownessError
        except:
            pass

        try:
            aDict[self.POWERRATIOERROR_KEY] = self.powerRatioError
        except:
            pass

        return aDict

    # test to see if class is valid
    def isValid(self) :
        """Checks to see if the object is valid

        Args:
            None
        Returns:
            True if the object is valid, False otherwise
        Raises:
            Nothing
        """
        errorList = self.getErrors()

        if len(errorList) == 0:
            return True
        else:
            return False

    # get list of validation errors
    def getErrors(self) :
        """Gets a list of object validation errors

        Args:
            None
        Returns:
            A List of Strings containing the validation error messages
        Raises:
            Nothing
        """
        errorList = []

        # first required keys
        try:
            if self.backAzimuth < 0:
                errorList.append('Invalid BackAzimuth in Beam Class.')
        except (NameError, AttributeError):
            errorList.append('No BackAzimuth in Beam Class.')

        try:
            if self.slowness < 0:
                errorList.append('Invalid Slowness in Beam Class.')
        except (NameError, AttributeError):
            errorList.append('No Slowness in Beam Class.')


        # second optional keys
        try:
            if self.powerRatio < 0:
                errorList.append('Invalid PowerRatio in Beam Class.')
        except:
            pass

        try:
            if self.backAzimuthError < 0:
                errorList.append('Invalid BackAzimuthError in Beam Class.')
        except:
            pass

        try:
            if self.slownessError < 0:
                errorList.append('Invalid SlownessError in Beam Class.')
        except:
            pass

        try:
            if self.powerRatioError < 0:
                errorList.append('Invalid PowerRatioError in Beam Class.')
        except:
            pass

        return errorList
