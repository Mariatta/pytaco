#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
"""How many tacos for a meetup?"""

__version__ = "1.0.0"


def main():
    rsvps = int(input("How many RSVPs? ") or 0)

    # Meetup Universal Constant)
    muc = 65

    muc_str = input(f"What percentage will show up? [{muc}] ")
    if muc_str.strip():
        muc = int(muc_str.strip())

    attending = int(rsvps * muc / 100)

    print()
    print(f"👪  {attending} people will show up (guess)")

    # 3 tacos per person
    # 60% meat taco
    # 40% veg taco
    # 6 tortillas per person

    total_taco = attending * 3
    meat_taco = 0.6 * total_taco
    veg_taco = 0.4 * total_taco

    tortillas = attending * 6

    print()
    print(f"{meat_taco:.0f} 🍖 🌮  meat tacos")
    print(f"{veg_taco:.0f} 🥒 🌮  veg tacos")
    print()
    print(f"{total_taco:.0f} 🌮  total tacos")
    print()
    print(f'{tortillas} 4" tortillas')

if __name__ == '__main__':
    main()
