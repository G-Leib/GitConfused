import packages
import webbrowser

if '__main__' == __name__:                  #pragma: no cover

    # **********************************************************************************************

    print('\n___Parse, pull, and assign header Bytecodes:___')
    H = packages.jvpm_opcodes.HeaderClass()               #pragma: no cover
    H.get_magic()                   #pragma: no cover
    H.get_minor()                   #pragma: no cover
    H.get_major()                   #pragma: no cover
    print("Constant Pool Count: " + str(H.get_const_pool_count() - 1))

    # **********************************************************************************************

    print('\n___Retrieve Constant Pool from .class, translate, and print to console:___')

    # print(H.get_const_pool())

    P = packages.pool_translate.PoolTranslate()                 #pragma: no cover
    N = P.translate()                   #pragma: no cover
    X = packages.pool_methods.TagTranslate()#pragma: no cover
    print("Constant Pool: ")
    print(N)                            #pragma: no cover
    print()                             #pragma: no cover
    print("Translated Constant Pool: ")
    for key in N:                       #pragma: no cover
        i = 1                            #pragma: no cover
        if (N[key][0]) == "01":         #pragma: no cover
            print(key + 1, " ", X.token_dict(N[key][0]), "\t\t\t", N[key][len(N[key]) - 1])
        else:
            print(key + 1, " ", X.token_dict(N[key][0]), "\t\t\t", N[key])
            
    print("\nInvokevirtual[] stack of 'Method References' from .class:\n"
          + str(packages.pool_translate.methodrefs))

    # **********************************************************************************************
    
    print('\n___Implement Method Opcodes from .class file.'
          ' Take input from the keybaord:___\n')

    packages.jvpm_opcodes.OpCodes().dict_search()
    
    # print(packages.pool_translate.cp_strings)

    # **********************************************************************************************

    print('\n___Print Hello World!:___')
    print()
    print("🎵🎶 Hello... Is it me your looking for? 🎶🎵")
    # webbrowser.open('https://www.youtube.com/watch?v=62XB9IbMnxQ')
    print()
    print("_________________________") 

    # **********************************************************************************************
