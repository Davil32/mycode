#!/usr/bin/env python3

# Complete the if and elif statement!
print("Enter grade obtained in 5 subjects: ")
gradeOne = int(input())

tot = gradeOne+gradeTwo+gradeThree+gradeFour+gradeFive
avg = tot/1

      if avg>=90 and avg<=100:
          print("A")
      elif avg>=80 and avg<=89:
          print("B")
      elif avg>=70 and avg<=79:
          print("C")
      elif avg>=60 and avg<=69:
          print("D")
      elif: avg>=0 and avg<=59:
          print("F")
      else:
          print("Invalid Input!")
