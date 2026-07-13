# Python 3.10+ ONLY!
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:  # Default case (like default: in C++)
        # if day is not 1, 2, 3, 4, or 5, this block will execute
        # its just like else 
        print("Weekend")


        # in c++ 
        # switch (day) {
        #     case 1:
        #         cout << "Monday" << endl;
        #         break;
        #     case 2:
        #         cout << "Tuesday" << endl;
        #         break;
        #     case 3:
        #         cout << "Wednesday" << endl;
        #         break;
        #     case 4:
        #         cout << "Thursday" << endl;
        #         break;
        #     case 5:
        #         cout << "Friday" << endl;
        #         break;
        #     default:
        #         cout << "Weekend" << endl;
        # }
