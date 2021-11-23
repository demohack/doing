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


class InlineResponse20033(object):
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
        'clean_title': 'str',
        'image': 'str',
        'category': 'str',
        'breadcrumbs': 'list[str]',
        'usda_code': 'int'
    }

    attribute_map = {
        'clean_title': 'cleanTitle',
        'image': 'image',
        'category': 'category',
        'breadcrumbs': 'breadcrumbs',
        'usda_code': 'usdaCode'
    }

    def __init__(self, clean_title=None, image=None, category=None, breadcrumbs=None, usda_code=None):  # noqa: E501
        """InlineResponse20033 - a model defined in OpenAPI"""  # noqa: E501

        self._clean_title = None
        self._image = None
        self._category = None
        self._breadcrumbs = None
        self._usda_code = None
        self.discriminator = None

        self.clean_title = clean_title
        self.image = image
        self.category = category
        self.breadcrumbs = breadcrumbs
        self.usda_code = usda_code

    @property
    def clean_title(self):
        """Gets the clean_title of this InlineResponse20033.  # noqa: E501


        :return: The clean_title of this InlineResponse20033.  # noqa: E501
        :rtype: str
        """
        return self._clean_title

    @clean_title.setter
    def clean_title(self, clean_title):
        """Sets the clean_title of this InlineResponse20033.


        :param clean_title: The clean_title of this InlineResponse20033.  # noqa: E501
        :type: str
        """
        if clean_title is None:
            raise ValueError("Invalid value for `clean_title`, must not be `None`")  # noqa: E501
        if clean_title is not None and len(clean_title) < 1:
            raise ValueError("Invalid value for `clean_title`, length must be greater than or equal to `1`")  # noqa: E501

        self._clean_title = clean_title

    @property
    def image(self):
        """Gets the image of this InlineResponse20033.  # noqa: E501


        :return: The image of this InlineResponse20033.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this InlineResponse20033.


        :param image: The image of this InlineResponse20033.  # noqa: E501
        :type: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501
        if image is not None and len(image) < 1:
            raise ValueError("Invalid value for `image`, length must be greater than or equal to `1`")  # noqa: E501

        self._image = image

    @property
    def category(self):
        """Gets the category of this InlineResponse20033.  # noqa: E501


        :return: The category of this InlineResponse20033.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this InlineResponse20033.


        :param category: The category of this InlineResponse20033.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        if category is not None and len(category) < 1:
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `1`")  # noqa: E501

        self._category = category

    @property
    def breadcrumbs(self):
        """Gets the breadcrumbs of this InlineResponse20033.  # noqa: E501


        :return: The breadcrumbs of this InlineResponse20033.  # noqa: E501
        :rtype: list[str]
        """
        return self._breadcrumbs

    @breadcrumbs.setter
    def breadcrumbs(self, breadcrumbs):
        """Sets the breadcrumbs of this InlineResponse20033.


        :param breadcrumbs: The breadcrumbs of this InlineResponse20033.  # noqa: E501
        :type: list[str]
        """
        if breadcrumbs is None:
            raise ValueError("Invalid value for `breadcrumbs`, must not be `None`")  # noqa: E501

        self._breadcrumbs = breadcrumbs

    @property
    def usda_code(self):
        """Gets the usda_code of this InlineResponse20033.  # noqa: E501


        :return: The usda_code of this InlineResponse20033.  # noqa: E501
        :rtype: int
        """
        return self._usda_code

    @usda_code.setter
    def usda_code(self, usda_code):
        """Sets the usda_code of this InlineResponse20033.


        :param usda_code: The usda_code of this InlineResponse20033.  # noqa: E501
        :type: int
        """
        if usda_code is None:
            raise ValueError("Invalid value for `usda_code`, must not be `None`")  # noqa: E501

        self._usda_code = usda_code

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
        if not isinstance(other, InlineResponse20033):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
