# coding: utf-8

"""
    spoonacular API

    The spoonacular Nutrition, Recipe, and Food API allows you to access over 380,000 recipes, thousands of ingredients, 800,000 food products, and 100,000 menu items. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \"gluten free brownies without sugar\" or \"low fat vegan cupcakes.\" You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what's in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: mail@spoonacular.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20013Ingredients(object):
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
        'id': 'int',
        'name': 'str',
        'localized_name': 'str',
        'image': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'localized_name': 'localizedName',
        'image': 'image'
    }

    def __init__(self, id=None, name=None, localized_name=None, image=None):  # noqa: E501
        """InlineResponse20013Ingredients - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._localized_name = None
        self._image = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.localized_name = localized_name
        self.image = image

    @property
    def id(self):
        """Gets the id of this InlineResponse20013Ingredients.  # noqa: E501


        :return: The id of this InlineResponse20013Ingredients.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20013Ingredients.


        :param id: The id of this InlineResponse20013Ingredients.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20013Ingredients.  # noqa: E501


        :return: The name of this InlineResponse20013Ingredients.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20013Ingredients.


        :param name: The name of this InlineResponse20013Ingredients.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def localized_name(self):
        """Gets the localized_name of this InlineResponse20013Ingredients.  # noqa: E501


        :return: The localized_name of this InlineResponse20013Ingredients.  # noqa: E501
        :rtype: str
        """
        return self._localized_name

    @localized_name.setter
    def localized_name(self, localized_name):
        """Sets the localized_name of this InlineResponse20013Ingredients.


        :param localized_name: The localized_name of this InlineResponse20013Ingredients.  # noqa: E501
        :type: str
        """
        if localized_name is None:
            raise ValueError("Invalid value for `localized_name`, must not be `None`")  # noqa: E501
        if localized_name is not None and len(localized_name) < 1:
            raise ValueError("Invalid value for `localized_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._localized_name = localized_name

    @property
    def image(self):
        """Gets the image of this InlineResponse20013Ingredients.  # noqa: E501


        :return: The image of this InlineResponse20013Ingredients.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this InlineResponse20013Ingredients.


        :param image: The image of this InlineResponse20013Ingredients.  # noqa: E501
        :type: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501
        if image is not None and len(image) < 1:
            raise ValueError("Invalid value for `image`, length must be greater than or equal to `1`")  # noqa: E501

        self._image = image

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20013Ingredients):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
