import random
import os

os.system('clear')

print("""  
                                   ////////////                                           //////////////            //   //
                                  //          //                                         //           //           //   //
                                 //          //                                        //           //           //   //
                                //          //    //   ///////  /////////             // //////////     //////  //   //
                               //          //    //   //       //      //            //          //   //    // //   //
                              //         //     //   //       /////////             //          //   //    // //   //
                             //        //      //   //       //                    //          //   //    // //   //
                            //////////        //   ///////  ////////              //          //   ///////  //   //

Welcome to my little program to teach my super, duper, awesome, wonderful, amazing, kids how to make a simple game.

--------------------MENU-------------------
1- Monster Dice Roll
2 - Smoke Check
3- Exit
""")
option = "0"

while option != "3":
    option = input()
    if option == "1":
        dice = random.randint(1,15)
        if dice <= 4:
          #print('A monster snake attacks!')
          print("""
        //////            ///////           /////////         ///////           /////////          /////////                  ///////////
      ///    ///        ///    ///       ///      ///      ///      //       //         //       //       //            //////  O    //////////////
    //         //     //        //    //           //    //          //    //           //    //          //         /////   /////////VVVVV
  //            /////           /////               ////              /////              //////             //////////""")
          option = "0"
    elif option == "2":
        dice = random.randint(1,15)
        if dice == 1:
          #print('A monster snake attacks!')
          print("""
          ****
         ****
          ***
         ***
        ***
        **
        *
""")
          option = "0"
        else:
           print("""

Nothing shows up, ph.

""")
           option = "0"

