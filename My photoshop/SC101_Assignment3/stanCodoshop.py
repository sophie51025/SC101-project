"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:the app combine four photos with different thing or person wanted to be removed into one clear photo.
"""

import os
import sys
from simpleimage import SimpleImage
from math import sqrt


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = sqrt((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    r_sum = 0
    g_sum = 0
    b_sum = 0

    for r in pixels:
        r_sum += r.red
    r_ave = r_sum // len(pixels)
    for g in pixels:
        g_sum += g.green
    g_ave = g_sum // len(pixels)
    for b in pixels:
        b_sum += b.blue
    b_ave = b_sum // len(pixels)

    return ([r_ave, g_ave, b_ave])



def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    ave_pixel = get_average(pixels)
    best_pixel = pixels[0]
    distance = 0

    for p in range(len(pixels)):
        pixel_dist = get_pixel_dist(pixels[p], ave_pixel[0], ave_pixel[1], ave_pixel[2])
        if p == 0:
            distance = pixel_dist
        elif pixel_dist < distance:
            distance = pixel_dist
            best_pixel = pixels[p]
    return best_pixel



def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    photo_number = len(images)
    pixels = []
    result = SimpleImage.blank(width, height)

    for i in range(height):
        for j in range(width):
            for k in range(photo_number):
                get_pixel = images[k].get_pixel(j, i)
                pixels.append(get_pixel)
            best = get_best_pixel(pixels)
            result_get = result.get_pixel(j, i)
            result_get.red = best.red
            result_get.green = best.green
            result_get.blue = best.blue
            pixels = []





    ######## YOUR CODE STARTS HERE #########

    # Write code to populate image and create the 'ghost' effect
    image_blank = SimpleImage.blank(width, height)
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
