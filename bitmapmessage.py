#!/usr/local/bin/python3
import sys

#source from https://inventwithpython.com/bitmapworld.txt
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

#loop over each line in the bitmap:
for line in bitmap.splitlines():
    # loop over each character in the line
    for i, bit in enumerate(line):
        if bit ==' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ',end='')
        else:
            # Print a character from the message
            print(message[i % len(message)], end='')
    print() # print a newline