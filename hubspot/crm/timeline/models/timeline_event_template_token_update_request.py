# coding: utf-8

"""
    Timeline events

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM object like contacts, companies, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.timeline.configuration import Configuration


class TimelineEventTemplateTokenUpdateRequest(object):
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
        "label": "str",
        "object_property_name": "str",
        "options": "list[TimelineEventTemplateTokenOption]",
    }

    attribute_map = {
        "label": "label",
        "object_property_name": "objectPropertyName",
        "options": "options",
    }

    def __init__(
        self,
        label=None,
        object_property_name=None,
        options=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """TimelineEventTemplateTokenUpdateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._object_property_name = None
        self._options = None
        self.discriminator = None

        self.label = label
        if object_property_name is not None:
            self.object_property_name = object_property_name
        self.options = options

    @property
    def label(self):
        """Gets the label of this TimelineEventTemplateTokenUpdateRequest.  # noqa: E501

        Used for list segmentation and reporting.  # noqa: E501

        :return: The label of this TimelineEventTemplateTokenUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TimelineEventTemplateTokenUpdateRequest.

        Used for list segmentation and reporting.  # noqa: E501

        :param label: The label of this TimelineEventTemplateTokenUpdateRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and label is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `label`, must not be `None`"
            )  # noqa: E501

        self._label = label

    @property
    def object_property_name(self):
        """Gets the object_property_name of this TimelineEventTemplateTokenUpdateRequest.  # noqa: E501

        The name of the CRM object property. This will populate the CRM object property associated with the event. With enough of these, you can fully build CRM objects via the Timeline API.  # noqa: E501

        :return: The object_property_name of this TimelineEventTemplateTokenUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._object_property_name

    @object_property_name.setter
    def object_property_name(self, object_property_name):
        """Sets the object_property_name of this TimelineEventTemplateTokenUpdateRequest.

        The name of the CRM object property. This will populate the CRM object property associated with the event. With enough of these, you can fully build CRM objects via the Timeline API.  # noqa: E501

        :param object_property_name: The object_property_name of this TimelineEventTemplateTokenUpdateRequest.  # noqa: E501
        :type: str
        """

        self._object_property_name = object_property_name

    @property
    def options(self):
        """Gets the options of this TimelineEventTemplateTokenUpdateRequest.  # noqa: E501

        If type is `enumeration`, we should have a list of options to choose from.  # noqa: E501

        :return: The options of this TimelineEventTemplateTokenUpdateRequest.  # noqa: E501
        :rtype: list[TimelineEventTemplateTokenOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this TimelineEventTemplateTokenUpdateRequest.

        If type is `enumeration`, we should have a list of options to choose from.  # noqa: E501

        :param options: The options of this TimelineEventTemplateTokenUpdateRequest.  # noqa: E501
        :type: list[TimelineEventTemplateTokenOption]
        """
        if (
            self.local_vars_configuration.client_side_validation and options is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `options`, must not be `None`"
            )  # noqa: E501

        self._options = options

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
        if not isinstance(other, TimelineEventTemplateTokenUpdateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimelineEventTemplateTokenUpdateRequest):
            return True

        return self.to_dict() != other.to_dict()
