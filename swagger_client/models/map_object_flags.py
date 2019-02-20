# coding: utf-8

"""
    RESTful-DOOM

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MapObjectFlags(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mf_special': 'bool',
        'mf_solid': 'bool',
        'mf_shootable': 'bool',
        'mf_nogravity': 'bool',
        'mf_noclip': 'bool',
        'mf_shadow': 'bool',
        'mf_corpse': 'bool'
    }

    attribute_map = {
        'mf_special': 'MF_SPECIAL',
        'mf_solid': 'MF_SOLID',
        'mf_shootable': 'MF_SHOOTABLE',
        'mf_nogravity': 'MF_NOGRAVITY',
        'mf_noclip': 'MF_NOCLIP',
        'mf_shadow': 'MF_SHADOW',
        'mf_corpse': 'MF_CORPSE'
    }

    def __init__(self, mf_special=None, mf_solid=None, mf_shootable=None, mf_nogravity=None, mf_noclip=None, mf_shadow=None, mf_corpse=None):  # noqa: E501
        """MapObjectFlags - a model defined in Swagger"""  # noqa: E501

        self._mf_special = None
        self._mf_solid = None
        self._mf_shootable = None
        self._mf_nogravity = None
        self._mf_noclip = None
        self._mf_shadow = None
        self._mf_corpse = None
        self.discriminator = None

        if mf_special is not None:
            self.mf_special = mf_special
        if mf_solid is not None:
            self.mf_solid = mf_solid
        if mf_shootable is not None:
            self.mf_shootable = mf_shootable
        if mf_nogravity is not None:
            self.mf_nogravity = mf_nogravity
        if mf_noclip is not None:
            self.mf_noclip = mf_noclip
        if mf_shadow is not None:
            self.mf_shadow = mf_shadow
        if mf_corpse is not None:
            self.mf_corpse = mf_corpse

    @property
    def mf_special(self):
        """Gets the mf_special of this MapObjectFlags.  # noqa: E501

        When this item is picked up, call P_SpecialThing  # noqa: E501

        :return: The mf_special of this MapObjectFlags.  # noqa: E501
        :rtype: bool
        """
        return self._mf_special

    @mf_special.setter
    def mf_special(self, mf_special):
        """Sets the mf_special of this MapObjectFlags.

        When this item is picked up, call P_SpecialThing  # noqa: E501

        :param mf_special: The mf_special of this MapObjectFlags.  # noqa: E501
        :type: bool
        """

        self._mf_special = mf_special

    @property
    def mf_solid(self):
        """Gets the mf_solid of this MapObjectFlags.  # noqa: E501

        Cannot be walked through  # noqa: E501

        :return: The mf_solid of this MapObjectFlags.  # noqa: E501
        :rtype: bool
        """
        return self._mf_solid

    @mf_solid.setter
    def mf_solid(self, mf_solid):
        """Sets the mf_solid of this MapObjectFlags.

        Cannot be walked through  # noqa: E501

        :param mf_solid: The mf_solid of this MapObjectFlags.  # noqa: E501
        :type: bool
        """

        self._mf_solid = mf_solid

    @property
    def mf_shootable(self):
        """Gets the mf_shootable of this MapObjectFlags.  # noqa: E501

        Takes damage when shot  # noqa: E501

        :return: The mf_shootable of this MapObjectFlags.  # noqa: E501
        :rtype: bool
        """
        return self._mf_shootable

    @mf_shootable.setter
    def mf_shootable(self, mf_shootable):
        """Sets the mf_shootable of this MapObjectFlags.

        Takes damage when shot  # noqa: E501

        :param mf_shootable: The mf_shootable of this MapObjectFlags.  # noqa: E501
        :type: bool
        """

        self._mf_shootable = mf_shootable

    @property
    def mf_nogravity(self):
        """Gets the mf_nogravity of this MapObjectFlags.  # noqa: E501

        Don't apply regular world gravity  # noqa: E501

        :return: The mf_nogravity of this MapObjectFlags.  # noqa: E501
        :rtype: bool
        """
        return self._mf_nogravity

    @mf_nogravity.setter
    def mf_nogravity(self, mf_nogravity):
        """Sets the mf_nogravity of this MapObjectFlags.

        Don't apply regular world gravity  # noqa: E501

        :param mf_nogravity: The mf_nogravity of this MapObjectFlags.  # noqa: E501
        :type: bool
        """

        self._mf_nogravity = mf_nogravity

    @property
    def mf_noclip(self):
        """Gets the mf_noclip of this MapObjectFlags.  # noqa: E501


        :return: The mf_noclip of this MapObjectFlags.  # noqa: E501
        :rtype: bool
        """
        return self._mf_noclip

    @mf_noclip.setter
    def mf_noclip(self, mf_noclip):
        """Sets the mf_noclip of this MapObjectFlags.


        :param mf_noclip: The mf_noclip of this MapObjectFlags.  # noqa: E501
        :type: bool
        """

        self._mf_noclip = mf_noclip

    @property
    def mf_shadow(self):
        """Gets the mf_shadow of this MapObjectFlags.  # noqa: E501

        Render this item with the flickering half-invisible shadow rendering  # noqa: E501

        :return: The mf_shadow of this MapObjectFlags.  # noqa: E501
        :rtype: bool
        """
        return self._mf_shadow

    @mf_shadow.setter
    def mf_shadow(self, mf_shadow):
        """Sets the mf_shadow of this MapObjectFlags.

        Render this item with the flickering half-invisible shadow rendering  # noqa: E501

        :param mf_shadow: The mf_shadow of this MapObjectFlags.  # noqa: E501
        :type: bool
        """

        self._mf_shadow = mf_shadow

    @property
    def mf_corpse(self):
        """Gets the mf_corpse of this MapObjectFlags.  # noqa: E501

        Don't respond to any action  # noqa: E501

        :return: The mf_corpse of this MapObjectFlags.  # noqa: E501
        :rtype: bool
        """
        return self._mf_corpse

    @mf_corpse.setter
    def mf_corpse(self, mf_corpse):
        """Sets the mf_corpse of this MapObjectFlags.

        Don't respond to any action  # noqa: E501

        :param mf_corpse: The mf_corpse of this MapObjectFlags.  # noqa: E501
        :type: bool
        """

        self._mf_corpse = mf_corpse

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MapObjectFlags, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MapObjectFlags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
