# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Arofarn
#
# SPDX-License-Identifier: BSD-3-Clause

import umetpy.constants as mpconsts

# pylint: disable=eval-used
print("List of all constants:\n")
for cst in dir(mpconsts):
    if cst[0] != "_":
        print("{:30s} = {:.12f}".format(cst, eval("{}.{}".format("mpconsts", cst))))
