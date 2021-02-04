# coding: utf-8

"""
    Calling Extensions API

    Provides a way for apps to add custom calling options to a contact record. This works in conjunction with the [Calling SDK](#), which is used to build your phone/calling UI. The endpoints here allow your service to appear as an option to HubSpot users when they access the *Call* action on a contact record. Once accessed, your custom phone/calling UI will be displayed in an iframe at the specified URL with the specified dimensions on that record.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.calling.configuration import Configuration


class SettingsRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "name": "str",
        "url": "str",
        "height": "int",
        "width": "int",
        "is_ready": "bool",
    }

    attribute_map = {
        "name": "name",
        "url": "url",
        "height": "height",
        "width": "width",
        "is_ready": "isReady",
    }

    def __init__(
        self,
        name=None,
        url=None,
        height=None,
        width=None,
        is_ready=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._url = None
        self._height = None
        self._width = None
        self._is_ready = None
        self.discriminator = None

        self.name = name
        self.url = url
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if is_ready is not None:
            self.is_ready = is_ready

    @property
    def name(self):
        """Gets the name of this SettingsRequest.  # noqa: E501

        The name of your calling service to display to users.  # noqa: E501

        :return: The name of this SettingsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SettingsRequest.

        The name of your calling service to display to users.  # noqa: E501

        :param name: The name of this SettingsRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this SettingsRequest.  # noqa: E501

        The URL to your phone/calling UI, built with the [Calling SDK](#).  # noqa: E501

        :return: The url of this SettingsRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SettingsRequest.

        The URL to your phone/calling UI, built with the [Calling SDK](#).  # noqa: E501

        :param url: The url of this SettingsRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and url is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `url`, must not be `None`"
            )  # noqa: E501

        self._url = url

    @property
    def height(self):
        """Gets the height of this SettingsRequest.  # noqa: E501

        The target height of the iframe that will contain your phone/calling UI.  # noqa: E501

        :return: The height of this SettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SettingsRequest.

        The target height of the iframe that will contain your phone/calling UI.  # noqa: E501

        :param height: The height of this SettingsRequest.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this SettingsRequest.  # noqa: E501

        The target width of the iframe that will contain your phone/calling UI.  # noqa: E501

        :return: The width of this SettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this SettingsRequest.

        The target width of the iframe that will contain your phone/calling UI.  # noqa: E501

        :param width: The width of this SettingsRequest.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def is_ready(self):
        """Gets the is_ready of this SettingsRequest.  # noqa: E501

        When true, your service will appear as an option under the *Call* action in contact records of connected accounts.  # noqa: E501

        :return: The is_ready of this SettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_ready

    @is_ready.setter
    def is_ready(self, is_ready):
        """Sets the is_ready of this SettingsRequest.

        When true, your service will appear as an option under the *Call* action in contact records of connected accounts.  # noqa: E501

        :param is_ready: The is_ready of this SettingsRequest.  # noqa: E501
        :type: bool
        """

        self._is_ready = is_ready

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
