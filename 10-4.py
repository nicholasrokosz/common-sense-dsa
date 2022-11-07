def recursive_print(arr):
    for i in arr:
        # print(type(i) is list)
        if type(i) is not list:
            print(i)
        else:
            recursive_print(i)









my_list = [ 1,
            2,
            3,
            [4, 5, 6],
            7,
            [8,
                [9, 10, 11,
                    [12, 13, 14]
                 ]
            ],
            [15, 16, 17, 18, 19,
                [20, 21, 22,
                    [23, 24, 25,
                        [26, 27, 29]
                    ], 30, 31
                ], 32
            ], 33
        ]

recursive_print(my_list)