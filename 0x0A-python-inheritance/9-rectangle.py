#!/usr/bin/python3
'''
    Class BaseGeometry
'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Represent a class Rectangle heritance from BaseGeometry
    '''
    def __init__(self, width, height):
        '''
            define width and height of Rectangle class
            call the method of the superclass
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''
            method to define the area of rectangle
        '''
        return self.__height * self.__width

    def __str__(self):
        '''
        print the rectangle width and height
        '''
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height
