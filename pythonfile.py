# Q1 GCD of two numbeers.
# def gcd(a, b):
#     if (a > b):
#         a, b = b, a
#     for i in range(1, a+1):
#         if (a % i == 0 and b % i == 0):
#             gcdn = i
#     print(f"Gcd of {a} and {b} is {gcdn}")


# n1 = int(input("Enter first number : "))
# n2 = int(input("Enter second number : "))
# gcd(n1, n2)

# Q2 Square root
# def squareroot(n, l):
#     x = n
#     count = 0
#     while (1):
#         count += 1
#         root = 0.5*(x+(n/x))
#         if (abs(root-x) < l):
#             break
#         x = root
#     return root


# n = int(input("Enter the no. you want to find sqrt. of : "))
# l = 0.00001
# a = squareroot(n, l)
# print(f"The square root of {n} is {a}")

# Q3 Exponentiation
# def exp(a, b):
#     c = a**b
#     print(f"The exponentiation of {a} to the power {b} is {c}")


# n1 = int(input("Enter the no. you want to find exponential of : "))
# n2 = int(input("Enter the power of exponentiation : "))
# exp(n1, n2)

# Q4 Maximum of a list of numbers.
# def listmax(l):
#     max = 0
#     for i in l:
#         if (i > max):
#             max = i
#     print(f"The maximum no in list {l} is {max}")


# n = int(input("Enter the no. of element in your list : "))
# ls = []
# for i in range(1, n+1):
#     a = int(input(f"Enter element {i} : "))
#     ls.append(a)
# listmax(ls)

# Q5 Linear search and binary search
# Linear
# def linear(l, n):
#     for i in range(len(l)):
#         if (l[i] == n):
#             return i
#     return -1


# def binary(l, n):
#     l.sort()
#     maxn = len(l)-1
#     minn = 0
#     while (maxn >= minn):
#         mid = (minn+maxn)//2
#         if (l[mid] == n):
#             return mid
#         elif (l[mid] < n):
#             minn = mid+1
#         else:
#             maxn = mid-1
#     return -1


# n = int(input("Enter the no. of element in your list : "))
# ls = []
# for i in range(1, n+1):
#     a = int(input(f"Enter element {i} : "))
#     ls.append(a)
# no = int(input("Enter the no. you want to search : "))
# # s = linear(ls, no)
# s = binary(ls, no)
# if (s >= 0):
#     print(f"The no {no} is found at index {s}")
# else:
#     print(f"The no {no} isn't found in the list {ls}")

# Q6 Sorting
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if (arr[j] < arr[min_index]):
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while (j >= 0 and key < arr[j]):
#             arr[j+1] = arr[j]
#             j -= 1
#             arr[j+1] = key


# n = int(input("Enter the no. of element in your list : "))
# ls = []
# for i in range(1, n+1):
#     a = int(input(f"Enter element {i} : "))
# ls.append(a)
# selection_sort(ls)
# insertion_sort(ls)
# print(f"Sorted List : {ls}")

# Merge Sort
# def merge(left, right):
#     result = []
#     i, j = 0, 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i = i + 1
#         else:
#             result.append(right[j])
#             j = j + 1

#     while i < len(left):
#         result.append(left[i])
#         i = i + 1

#     while j < len(right):
#         result.append(right[j])
#         j = j + 1

#     return result


# def merge_sort(l):
#     if len(l) < 2:
#         return l[:]
#     else:
#         middle = len(l) // 2
#         left = merge_sort(l[:middle])
#         right = merge_sort(l[middle:])

#         together = merge(left, right)
#         return together


# n = int(input("Enter the no. of element in your list : "))
# ls = []
# for i in range(1, n+1):
#     a = int(input(f"Enter element {i} : "))
#     ls.append(a)
# sls = merge_sort(ls)
# print(f"Sorted List : {sls}")

# First n prime nos.
# import math


# def is_Prime(n):
#     if (n <= 1):
#         return False
#     else:
#         for i in range(2, int(math.sqrt(n))+1):
#             if (n % i == 0):
#                 return False
#         return True


# def n_primes(no):
#     if (no > 0):
#         count = 0
#         num = 2
#         pnos = []
#         while (count < no):
#             if (is_Prime(num)):
#                 pnos.append(num)
#                 count += 1
#             num += 1
#         print(f"The first {no} prime nos. are {pnos}")


# no = int(input("Enter the no. until you want to print primes : "))
# n_primes(no)

# Multiplication of matrices

# def matrice_multiply(m1, m2):
#     if (len(m1[0]) != len(m2)):
#         print("Multiplication can't take place")
#         return None
#     result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
#     for i in range(len(m1)):
#         for j in range(len(m2[0])):
#             for k in range(len(m2)):
#                 result[i][j] += m1[i][k] * m2[k][j]
#     return result


# mat1r = int(input("No. of rows in matrix 1 : "))
# mat1c = int(input("No. of columns in matrix 1 : "))
# mat1 = [[0 for _ in range(mat1c)] for _ in range(mat1r)]
# for i in range(mat1r):
#     for j in range(mat1c):
#         inp = int(input(f"Enter element matrix 1 [{i}][{j}] : "))
#         mat1[i][j] = inp
# mat2r = int(input("No. of rows in matrix 2 : "))
# mat2c = int(input("No. of columns in matrix 2 : "))
# mat2 = [[0 for _ in range(mat2c)] for _ in range(mat2r)]
# for i in range(mat2r):
#     for j in range(mat2c):
#         inp = int(input(f"Enter element matrix 2 [{i}][{j}] : "))
#         mat2[i][j] = inp
# print("Multiplied Matrice : ")
# for i in matrice_multiply(mat1, mat2):
#     print(i)

# Command line args

# import sys
# print("This is the name of the script:", sys.argv[0])
# print("Number of arguments:", len(sys.argv))
# print("The arguments are:", str(sys.argv))

# Most frequent words in a text file
# with open("myfile.txt", "r") as f:
#     f_word = ""
#     freq = 0
#     words = []
#     for line in f:
#         l_word = line.lower().replace(',', '').replace('.', '').split(" ")
#         for w in l_word:
#             words.append(w)
#     for i in range(0, len(words)):
#         count = 1
#         for j in range(i+1, len(words)):
#             if (words[i] == words[j]):
#                 count += 1
#         if (count > freq):
#             f_word = words[i]
#             freq = count
#     print(f"Most repeated word : {f_word}")
#     print(f"Frequency : {freq}")
import pygame
import math
# Constants for the simulation
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
SUN_RADIUS = 30
PLANET_RADIUS = 10
ORBIT_SEMI_MAJOR_AXIS = 200
ORBIT_SEMI_MINOR_AXIS = 100
ORBIT_SPEED = 0.02
# Initialize Pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elliptical Orbit Simulation")
# Define colors
SUN_COLOR = (255, 255, 0)
PLANET_COLOR = (0, 0, 255)
# Initialize planet position and angle
planet_angle = 0
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Clear the screen
screen.fill(BACKGROUND_COLOR)
# Calculate the planet's position in the orbit
planet_x = SCREEN_WIDTH // 2 + ORBIT_SEMI_MAJOR_AXIS * math.cos(planet_angle)
planet_y = SCREEN_HEIGHT // 2 + ORBIT_SEMI_MINOR_AXIS * math.sin(planet_angle)
# Draw the sun
pygame.draw.circle(screen, SUN_COLOR, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                   SUN_RADIUS)

# Draw the planet
pygame.draw.circle(screen, PLANET_COLOR, (int(planet_x), int(planet_y)),
                   PLANET_RADIUS)
# Update the planet's angle (orbit)
planet_angle += ORBIT_SPEED
# Update the display
pygame.display.flip()
# Quit Pygame
pygame.quit()
