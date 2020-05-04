# coding: utf-8

"""
    CRM cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.cards.configuration import Configuration


class CardFetchBody(object):
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
    openapi_types = {"target_url": "str", "object_types": "list[CardObjectTypeBody]"}

    attribute_map = {"target_url": "targetUrl", "object_types": "objectTypes"}

    def __init__(
        self, target_url=None, object_types=None, local_vars_configuration=None
    ):  # noqa: E501
        """CardFetchBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target_url = None
        self._object_types = None
        self.discriminator = None

        self.target_url = target_url
        self.object_types = object_types

    @property
    def target_url(self):
        """Gets the target_url of this CardFetchBody.  # noqa: E501

        URL to a service endpoints that will respond with card details. HubSpot will call this endpoint each time a user visits a CRM record page where this card should be displayed.  # noqa: E501

        :return: The target_url of this CardFetchBody.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this CardFetchBody.

        URL to a service endpoints that will respond with card details. HubSpot will call this endpoint each time a user visits a CRM record page where this card should be displayed.  # noqa: E501

        :param target_url: The target_url of this CardFetchBody.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and target_url is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `target_url`, must not be `None`"
            )  # noqa: E501

        self._target_url = target_url

    @property
    def object_types(self):
        """Gets the object_types of this CardFetchBody.  # noqa: E501

        An array of CRM object types where this card should be displayed. HubSpot will call your data fetch URL whenever a user visits a record page of the types defined here.  # noqa: E501

        :return: The object_types of this CardFetchBody.  # noqa: E501
        :rtype: list[CardObjectTypeBody]
        """
        return self._object_types

    @object_types.setter
    def object_types(self, object_types):
        """Sets the object_types of this CardFetchBody.

        An array of CRM object types where this card should be displayed. HubSpot will call your data fetch URL whenever a user visits a record page of the types defined here.  # noqa: E501

        :param object_types: The object_types of this CardFetchBody.  # noqa: E501
        :type: list[CardObjectTypeBody]
        """
        if (
            self.local_vars_configuration.client_side_validation
            and object_types is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_types`, must not be `None`"
            )  # noqa: E501

        self._object_types = object_types

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
        if not isinstance(other, CardFetchBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CardFetchBody):
            return True

        return self.to_dict() != other.to_dict()
